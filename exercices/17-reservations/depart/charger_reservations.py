"""Crée la table reservations dans carte.db et la remplit depuis reservations.csv.

Les 30 réservations sont fictives (voir SOURCES.md). Relançable : la table est vidée avant
chaque chargement. La table carte n'est pas touchée.

    python charger_reservations.py
"""
import csv
import sqlite3
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
CSV = DOSSIER / "reservations.csv"
DB = DOSSIER / "carte.db"


def main():
    with sqlite3.connect(DB) as connexion:
        connexion.execute(
            """
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                telephone TEXT NOT NULL DEFAULT '',
                email TEXT NOT NULL DEFAULT '',
                date TEXT NOT NULL,
                couverts INTEGER NOT NULL,
                commentaire TEXT NOT NULL DEFAULT '',
                cree_le TEXT NOT NULL
            )
            """
        )
        connexion.execute("DELETE FROM reservations")
        connexion.execute("DELETE FROM sqlite_sequence WHERE name = 'reservations'")
        with open(CSV, encoding="utf-8", newline="") as fichier:
            lignes = [
                (l["nom"], l["telephone"], l["email"], l["date"],
                 int(l["couverts"]), l["commentaire"], l["cree_le"])
                for l in csv.DictReader(fichier)
            ]
        connexion.executemany(
            "INSERT INTO reservations (nom, telephone, email, date, couverts, commentaire, cree_le) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            lignes,
        )
        nombre = connexion.execute("SELECT COUNT(*) FROM reservations").fetchone()[0]
    print(f"{nombre} réservations dans {DB.name}")


if __name__ == "__main__":
    main()
