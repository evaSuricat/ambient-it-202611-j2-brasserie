"""Tests du formulaire de réservation robuste. Bibliothèque standard seulement.

    python -m unittest test_formulaire -v        (depuis ce dossier)

Chaque test démarre son propre serveur, dans une COPIE temporaire de ce dossier, sur un port
libre : votre base n'est jamais modifiée. Au départ, quatre tests échouent et un passe
(« une demande valide est acceptée ») : c'est le point de départ voulu.

Ce que le serveur doit faire (contrat de l'exercice) :
- un champ piège « site_web », invisible pour une personne, rempli : répondre comme si tout
  allait bien (201), sans rien enregistrer ;
- un champ « ouvert_a » (heure d'ouverture de la page, en millisecondes) : refuser (400) un envoi
  fait moins de 3 secondes après ;
- au plus 5 envois par minute et par adresse : refuser le suivant (429) ;
- une réponse 400 contient, par champ fautif, un message lisible : {"champs": {"couverts": "..."}}.
"""
import json
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path

ICI = Path(__file__).resolve().parent
VALIDE = {"nom": "Essai Test", "telephone": "06 39 98 00 00", "email": "essai@example.com",
          "date": "2026-12-12", "couverts": 2, "commentaire": ""}


def port_libre():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class TestsFormulaire(unittest.TestCase):
    def setUp(self):
        self.temp = Path(tempfile.mkdtemp(prefix="pigala-form-"))
        self.copie = self.temp / "site"
        shutil.copytree(ICI, self.copie, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))
        self.port = port_libre()
        self.serveur = subprocess.Popen(
            [sys.executable, "servir.py", str(self.port)], cwd=self.copie,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        for _ in range(50):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{self.port}/").read()
                break
            except OSError:
                time.sleep(0.1)
        else:
            raise RuntimeError("Le serveur de test n'a pas démarré.")

    def tearDown(self):
        self.serveur.terminate()
        self.serveur.wait(timeout=5)
        shutil.rmtree(self.temp, ignore_errors=True)

    def envoyer(self, donnees):
        requete = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/api/reservations",
            data=json.dumps(donnees).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(requete, timeout=5) as reponse:
                return reponse.status, json.loads(reponse.read())
        except urllib.error.HTTPError as erreur:
            try:
                return erreur.code, json.loads(erreur.read())
            except ValueError:
                return erreur.code, {}

    def nombre(self):
        total = 0
        for fichier in self.copie.rglob("*.db"):
            with sqlite3.connect(fichier) as c:
                if c.execute("SELECT name FROM sqlite_master WHERE name='reservations'").fetchone():
                    total += c.execute("SELECT COUNT(*) FROM reservations").fetchone()[0]
        return total

    def ancien(self):
        """Heure d'ouverture de la page il y a dix secondes."""
        return int(time.time() * 1000) - 10_000

    def test_une_demande_valide_est_acceptee(self):
        avant = self.nombre()
        statut, _ = self.envoyer({**VALIDE, "ouvert_a": self.ancien()})
        self.assertEqual(statut, 201)
        self.assertEqual(self.nombre(), avant + 1)

    def test_le_champ_piege_rempli_n_enregistre_rien(self):
        avant = self.nombre()
        statut, _ = self.envoyer({**VALIDE, "ouvert_a": self.ancien(), "site_web": "http://exemple.invalid"})
        self.assertEqual(statut, 201, "on répond comme si tout allait bien")
        self.assertEqual(self.nombre(), avant, "mais rien ne doit être enregistré")

    def test_un_envoi_trop_rapide_est_refuse(self):
        avant = self.nombre()
        statut, _ = self.envoyer({**VALIDE, "ouvert_a": int(time.time() * 1000)})
        self.assertEqual(statut, 400)
        self.assertEqual(self.nombre(), avant)

    def test_le_sixieme_envoi_en_une_minute_est_refuse(self):
        statuts = [self.envoyer({**VALIDE, "ouvert_a": self.ancien()})[0] for _ in range(7)]
        self.assertIn(429, statuts)
        self.assertLessEqual(self.nombre() - 30, 5)

    def test_chaque_champ_fautif_a_son_message(self):
        statut, corps = self.envoyer({**VALIDE, "ouvert_a": self.ancien(), "couverts": 99, "email": "pas-un-courriel"})
        self.assertEqual(statut, 400)
        champs = corps.get("champs", {})
        self.assertIn("couverts", champs)
        self.assertIn("email", champs)
        self.assertNotIn("nom", champs)
        for message in champs.values():
            self.assertGreater(len(message), 10, "un message lisible, pas un code")


if __name__ == "__main__":
    unittest.main()
