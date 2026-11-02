"""Crée carte.db (SQLite) et la remplit depuis carte.csv.

Relançable : la table est vidée avant chaque chargement.

    python charger.py
"""
import csv
import sqlite3
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
CSV = DOSSIER / "carte.csv"
DB = DOSSIER / "carte.db"


def main():
    with sqlite3.connect(DB) as connexion:
        connexion.execute(
            """
            CREATE TABLE IF NOT EXISTS carte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categorie TEXT NOT NULL,
                nom TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                prix REAL NOT NULL
            )
            """
        )
        connexion.execute("DELETE FROM carte")
        with open(CSV, encoding="utf-8", newline="") as fichier:
            lignes = [
                (l["categorie"], l["nom"], l["description"], float(l["prix"]))
                for l in csv.DictReader(fichier)
            ]
        connexion.executemany(
            "INSERT INTO carte (categorie, nom, description, prix) VALUES (?, ?, ?, ?)",
            lignes,
        )
        nombre = connexion.execute("SELECT COUNT(*) FROM carte").fetchone()[0]
    print(f"{nombre} lignes dans {DB.name}")


if __name__ == "__main__":
    main()
