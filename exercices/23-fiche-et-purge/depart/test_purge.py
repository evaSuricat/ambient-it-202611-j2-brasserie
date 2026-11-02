"""Tests de purger.py. Bibliothèque standard seulement.

    python -m unittest test_purge -v        (depuis ce dossier)

Chaque test travaille sur une COPIE temporaire de donnees/reservations.db : votre base n'est
jamais modifiée. Au départ, purger.py n'existe pas : les quatre tests échouent. C'est voulu.
"""
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ICI = Path(__file__).resolve().parent
BASE = ICI / "donnees" / "reservations.db"
AUJOURDHUI = "2026-12-01"
JOURS = 7                      # limite = 2026-11-24
LIMITE = "2026-11-24"


def purger(*arguments):
    return subprocess.run(
        [sys.executable, str(ICI / "purger.py"), *arguments],
        capture_output=True, text=True, encoding="utf-8", cwd=ICI,
    )


class TestsPurge(unittest.TestCase):
    def setUp(self):
        self.assertTrue((ICI / "purger.py").exists(), "purger.py n'existe pas encore")
        self.temp = Path(tempfile.mkdtemp(prefix="pigala-purge-"))
        self.copie = self.temp / "reservations.db"
        shutil.copy(BASE, self.copie)

    def tearDown(self):
        shutil.rmtree(self.temp, ignore_errors=True)

    def compter(self, condition="1=1", valeurs=()):
        with sqlite3.connect(self.copie) as c:
            return c.execute(f"SELECT COUNT(*) FROM reservations WHERE {condition}", valeurs).fetchone()[0]

    def arguments(self, *en_plus):
        return ["--conserver-jours", str(JOURS), "--aujourdhui", AUJOURDHUI, "--base", str(self.copie), *en_plus]

    def test_la_simulation_ne_supprime_rien(self):
        avant = self.compter()
        resultat = purger(*self.arguments())
        self.assertEqual(resultat.returncode, 0, resultat.stderr)
        self.assertEqual(self.compter(), avant)

    def test_appliquer_supprime_seulement_les_anciennes(self):
        avant = self.compter()
        anciennes = self.compter("date < ?", (LIMITE,))
        self.assertGreater(anciennes, 0)
        self.assertLess(anciennes, avant)
        resultat = purger(*self.arguments("--appliquer"))
        self.assertEqual(resultat.returncode, 0, resultat.stderr)
        self.assertEqual(self.compter(), avant - anciennes)
        self.assertEqual(self.compter("date < ?", (LIMITE,)), 0)

    def test_refuse_de_tourner_sans_duree(self):
        avant = self.compter()
        resultat = purger("--base", str(self.copie), "--appliquer")
        self.assertNotEqual(resultat.returncode, 0)
        self.assertEqual(self.compter(), avant)

    def test_le_journal_ne_contient_aucune_donnee_personnelle(self):
        with sqlite3.connect(self.copie) as c:
            noms = [l[0] for l in c.execute("SELECT nom FROM reservations")]
            telephones = [l[0] for l in c.execute("SELECT telephone FROM reservations")]
        purger(*self.arguments("--appliquer"))
        journaux = list(self.temp.glob("*.log")) + list(self.temp.rglob("purge.log"))
        self.assertTrue(journaux, "aucun journal de purge trouvé à côté de la base")
        texte = "\n".join(j.read_text(encoding="utf-8") for j in journaux)
        for valeur in noms + telephones:
            self.assertNotIn(valeur, texte, "le journal recopie une donnée personnelle")


if __name__ == "__main__":
    unittest.main()
