"""Tests de sécurité du serveur du Pigala. Bibliothèque standard seulement.

    python -m unittest              (depuis ce dossier)
    python -m unittest -v           (une ligne par test)

Le test démarre lui-même le serveur sur un port libre, dans une COPIE temporaire de ce
dossier. Votre base n'est jamais modifiée, et vous n'avez rien à lancer avant.
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
# Un texte qui n'apparaît que dans les données de réservations (courriels fictifs).
MARQUEUR_DONNEES = "example.com"


def port_libre():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def nombre_reservations(dossier):
    """Compte les réservations, où que la base soit rangée dans la copie."""
    total = 0
    for fichier in dossier.rglob("*.db"):
        with sqlite3.connect(fichier) as c:
            table = c.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='reservations'"
            ).fetchone()
            if table:
                total += c.execute("SELECT COUNT(*) FROM reservations").fetchone()[0]
    return total


class TestsSecurite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = Path(tempfile.mkdtemp(prefix="pigala-test-"))
        cls.copie = cls.temp / "site"
        shutil.copytree(ICI, cls.copie, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))
        cls.port = port_libre()
        cls.serveur = subprocess.Popen(
            [sys.executable, "servir.py", str(cls.port)],
            cwd=cls.copie,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(50):
            try:
                cls.demander("/")
                break
            except OSError:
                time.sleep(0.1)
        else:
            raise RuntimeError("Le serveur de test n'a pas démarré.")

    @classmethod
    def tearDownClass(cls):
        cls.serveur.terminate()
        cls.serveur.wait(timeout=5)
        shutil.rmtree(cls.temp, ignore_errors=True)

    @classmethod
    def demander(cls, chemin, donnees=None):
        """Renvoie (statut, corps en texte). Un statut d'erreur n'est pas une exception."""
        requete = urllib.request.Request(f"http://127.0.0.1:{cls.port}{chemin}")
        if donnees is not None:
            requete.data = json.dumps(donnees).encode("utf-8")
            requete.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(requete, timeout=5) as reponse:
                return reponse.status, reponse.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as erreur:
            return erreur.code, erreur.read().decode("utf-8", "replace")

    # --- Ce qui doit être fermé -------------------------------------------------

    def test_la_base_ne_se_telecharge_pas(self):
        for chemin in ("/carte.db", "/reservations.db", "/donnees/reservations.db", "/reservations.csv"):
            statut, _ = self.demander(chemin)
            self.assertNotEqual(statut, 200, f"{chemin} se télécharge")

    def test_le_code_ne_se_telecharge_pas(self):
        for chemin in ("/servir.py", "/charger.py", "/charger_reservations.py"):
            statut, _ = self.demander(chemin)
            self.assertNotEqual(statut, 200, f"{chemin} se télécharge")

    def test_l_injection_ne_renvoie_pas_la_table(self):
        # Adresse d'injection : nom=' OR 1=1 -- (encodée)
        statut, corps = self.demander("/api/reservations?nom=%27%20OR%201%3D1%20--%20")
        self.assertFalse(MARQUEUR_DONNEES in corps, "l'injection renvoie les réservations")

    def test_la_recherche_n_est_pas_publique(self):
        statut, corps = self.demander("/api/reservations?nom=Lemaire")
        self.assertIn(statut, (401, 403, 404, 405), "la recherche répond à n'importe qui")
        self.assertFalse(MARQUEUR_DONNEES in corps, "la recherche renvoie des réservations")

    # --- Ce qui doit continuer à marcher ----------------------------------------

    def test_une_reservation_valide_s_enregistre(self):
        avant = nombre_reservations(self.copie)
        statut, _ = self.demander(
            "/api/reservations",
            {"nom": "Essai Test", "telephone": "06 39 98 00 00", "email": "essai@example.com",
             "date": "2026-12-12", "couverts": 2, "commentaire": ""},
        )
        self.assertEqual(statut, 201)
        self.assertEqual(nombre_reservations(self.copie), avant + 1)

    def test_la_carte_s_affiche(self):
        statut, corps = self.demander("/api/carte")
        self.assertEqual(statut, 200)
        self.assertGreaterEqual(len(json.loads(corps)), 10)
        statut, page = self.demander("/")
        self.assertEqual(statut, 200)
        self.assertIn("Pigala", page)


if __name__ == "__main__":
    unittest.main()
