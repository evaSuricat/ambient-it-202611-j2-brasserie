"""Calcule le taux d'absence dans historique.csv. Bibliothèque standard seulement.

    python calcul.py                       # absences par code postal, par créneau, puis croisé
    python calcul.py code_postal           # un seul regroupement
    python calcul.py code_postal heure     # un croisement de votre choix

Les colonnes utilisables : jour, heure, couverts, code_postal. Une absence est une ligne où
la colonne « venue » vaut « non ». Le fichier est fictif et les codes postaux 99001 à 99004
n'existent pas (voir SOURCES.md).
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

FICHIER = Path(__file__).resolve().parent / "historique.csv"


def lire():
    with open(FICHIER, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def taux(lignes, colonnes):
    groupes = defaultdict(lambda: [0, 0])
    for l in lignes:
        cle = tuple(l[c] for c in colonnes)
        groupes[cle][0] += 1
        if l["venue"] == "non":
            groupes[cle][1] += 1
    return dict(sorted(groupes.items()))


def afficher(lignes, colonnes):
    print(" x ".join(colonnes))
    for cle, (total, absences) in taux(lignes, colonnes).items():
        print(f"  {' | '.join(cle):<20} {absences:>3} absence(s) sur {total:>3} demandes : {100 * absences / total:5.1f} %")
    print()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lignes = lire()
    demandes = sys.argv[1:]
    if demandes:
        afficher(lignes, demandes)
        return
    total = sum(1 for l in lignes if l["venue"] == "non")
    print(f"Ensemble : {total} absence(s) sur {len(lignes)} demandes : {100 * total / len(lignes):.1f} %\n")
    afficher(lignes, ["code_postal"])
    afficher(lignes, ["heure"])
    afficher(lignes, ["code_postal", "heure"])


if __name__ == "__main__":
    main()
