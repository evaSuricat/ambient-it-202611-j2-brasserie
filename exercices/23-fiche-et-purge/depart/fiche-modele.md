# Fiche de traitement : réservations du Pigala

À remplir à partir de ce que fait **réellement** votre projet (`servir.py`, `donnees/`, `index.html`), pas de ce qu'on suppose. Une fiche qui décrit autre chose que le code est pire qu'une fiche absente. Écrivez « à décider » plutôt que d'inventer.

Cette fiche est un exercice utile dans tous les cas : savoir ce que l'on traite, pourquoi, combien de temps et qui y accède sert à n'importe quelle structure, qu'elle ait ou non l'obligation de tenir un registre. Elle ne dit pas si Le Pigala y est tenu : l'exercice ne tranche pas ce point.

## 1. Finalité

À quoi servent les données ? (une phrase par finalité, sans « et autres usages »)

-

## 2. Personnes concernées

-

## 3. Données collectées

Pour chaque champ du formulaire : le champ, pourquoi on en a besoin, obligatoire ou non. Vérifiez dans `index.html` : le formulaire demande-t-il plus que nécessaire ? Le champ « commentaire » est un texte libre : quelles données peut-il contenir en pratique, y compris des données de santé ?

| Champ | Pourquoi | Obligatoire |
|---|---|---|
| | | |

## 4. Qui accède aux données

(Le serveur public, le gérant avec `gerant.py`, les outils d'IA, un hébergeur, un prestataire. Qui ne doit pas y accéder.)

-

## 5. Durée de conservation

Durée choisie, et **la raison de ce choix** au regard de la finalité. Une durée copiée sans justification ne vaut rien.

- Durée :
- Justification :
- Ce qui se passe à l'échéance (suppression, archivage) :

## 6. Sécurité

Ce qui est en place dans le projet (renvoyez à l'exercice 21 et à ses tests), et ce qui manque.

-

## 7. Droits des personnes et incident

- Comment une personne obtient-elle la suppression de sa réservation ? (Qui le fait, avec quel outil ?)
- Si la base fuit : qui est prévenu, dans quel délai ? (Renseignez-vous à la source : article 33 du RGPD, voir `SOURCES.md`.)

## 8. Ce qui reste à décider ou à vérifier

-
