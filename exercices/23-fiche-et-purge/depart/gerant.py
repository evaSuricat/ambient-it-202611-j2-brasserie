"""Outil du gérant : chercher une réservation par nom, sur ce poste seulement.

    python gerant.py Lemaire        # les réservations dont le nom contient « Lemaire »
    python gerant.py                # toutes les réservations à venir, par date

Ce script lit donnees/reservations.db en lecture seule. Il n'est pas un serveur : personne
d'autre que la personne qui l'ouvre sur ce poste ne peut l'interroger.
"""
import sqlite3
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent / "donnees" / "reservations.db"


def chercher(nom):
    # Le texte cherché passe par un paramètre « ? » : il n'est jamais interprété comme du SQL.
    with sqlite3.connect(f"file:{BASE}?mode=ro", uri=True) as connexion:
        connexion.row_factory = sqlite3.Row
        return connexion.execute(
            "SELECT id, nom, telephone, date, couverts, commentaire "
            "FROM reservations WHERE nom LIKE ? ORDER BY date",
            (f"%{nom}%",),
        ).fetchall()


def main():
    nom = sys.argv[1] if len(sys.argv) > 1 else ""
    lignes = chercher(nom)
    for l in lignes:
        print(f"{l['id']:>3} | {l['date']} | {l['couverts']} pers. | {l['nom']} | {l['telephone']} | {l['commentaire']}")
    print(f"{len(lignes)} réservation(s).")


if __name__ == "__main__":
    main()
