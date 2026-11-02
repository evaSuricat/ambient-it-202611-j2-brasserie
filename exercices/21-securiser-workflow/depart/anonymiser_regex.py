"""Masque les courriels et les numéros de téléphone de l'extrait, avec des expressions régulières.

    python anonymiser_regex.py

C'est l'outil rapide qu'on écrit en premier. L'étape 5 de l'exercice 21 consiste à lire sa
sortie et à compter ce qu'il a laissé passer.
"""
import re
import sys

from afficher_extrait import lire_extrait

COURRIEL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
TELEPHONE = re.compile(r"(?:\+33|0)\s?[1-9](?:[\s.-]?\d{2}){4}")


def masquer(texte):
    texte = COURRIEL.sub("[COURRIEL]", texte)
    return TELEPHONE.sub("[TÉLÉPHONE]", texte)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for ligne in lire_extrait():
        print(masquer(ligne))
