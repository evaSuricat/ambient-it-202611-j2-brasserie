"""Sépare les réservations de la carte : une seule fois.

Copie la table reservations de carte.db vers donnees/reservations.db, vérifie que le nombre
de lignes est identique, puis supprime la table de carte.db. Relançable : si la table
n'est plus dans carte.db, il ne fait rien.

    python separer_base.py
"""
import sqlite3
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
CARTE = DOSSIER / "carte.db"
RESERVATIONS = DOSSIER / "donnees" / "reservations.db"

SCHEMA = """
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


def main():
    with sqlite3.connect(CARTE) as source:
        existe = source.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='reservations'"
        ).fetchone()
        if not existe:
            print("Rien à faire : carte.db ne contient plus de table reservations.")
            return
        lignes = source.execute(
            "SELECT id, nom, telephone, email, date, couverts, commentaire, cree_le FROM reservations"
        ).fetchall()

    RESERVATIONS.parent.mkdir(exist_ok=True)
    with sqlite3.connect(RESERVATIONS) as cible:
        cible.execute(SCHEMA)
        cible.execute("DELETE FROM reservations")
        cible.executemany("INSERT INTO reservations VALUES (?, ?, ?, ?, ?, ?, ?, ?)", lignes)
        copiees = cible.execute("SELECT COUNT(*) FROM reservations").fetchone()[0]

    if copiees != len(lignes):
        raise SystemExit(f"Copie incomplète ({copiees} sur {len(lignes)}) : carte.db n'est pas modifiée.")

    with sqlite3.connect(CARTE) as source:
        source.execute("DROP TABLE reservations")
    with sqlite3.connect(CARTE) as source:
        source.execute("VACUUM")
    print(f"{copiees} réservations copiées dans {RESERVATIONS.relative_to(DOSSIER)}, table retirée de carte.db.")


if __name__ == "__main__":
    main()
