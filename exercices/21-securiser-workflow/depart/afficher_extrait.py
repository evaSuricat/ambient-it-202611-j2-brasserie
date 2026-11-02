"""Affiche sept réservations fictives (les lignes 1, 2, 4, 9, 12, 15 et 21), en lecture seule.

    python afficher_extrait.py

Sert à l'étape « anonymiser un extrait » de l'exercice 21. Cherche la table reservations
dans carte.db, puis dans donnees/reservations.db si elle y a été déplacée.
"""
import sqlite3
import sys
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
LIGNES = (1, 2, 4, 9, 12, 15, 21)


def trouver_base():
    for chemin in (DOSSIER / "carte.db", DOSSIER / "donnees" / "reservations.db"):
        if chemin.exists():
            with sqlite3.connect(f"file:{chemin}?mode=ro", uri=True) as c:
                if c.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='reservations'"
                ).fetchone():
                    return chemin
    raise SystemExit("Aucune table reservations trouvée.")


def lire_extrait():
    """Renvoie les lignes de l'extrait, une chaîne par réservation."""
    base = trouver_base()
    with sqlite3.connect(f"file:{base}?mode=ro", uri=True) as c:
        marques = ",".join("?" * len(LIGNES))
        lignes = c.execute(
            f"SELECT id, nom, telephone, email, date, couverts, commentaire "
            f"FROM reservations WHERE id IN ({marques}) ORDER BY id",
            LIGNES,
        ).fetchall()
    return [" | ".join(str(v) for v in ligne) for ligne in lignes]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(lire_extrait()))
