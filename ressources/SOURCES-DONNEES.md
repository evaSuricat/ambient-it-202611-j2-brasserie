# D'où viennent les données de ce dépôt

Règle du dépôt : une donnée absente d'un fichier du dossier, un modèle l'invente. Chaque exercice contient donc ses données, et chaque `depart/` a un `SOURCES.md` qui dit d'où elles viennent. Voici la vue d'ensemble.

| Donnée | Où | Origine |
|---|---|---|
| Le Pigala (nom, adresse, horaires, téléphone) | `brief.md` | Inventé pour la formation. Le téléphone du restaurant, 01 99 00 12 34, est un numéro de fiction pris dans la tranche 01 99 00 que l'Arcep réserve aux œuvres audiovisuelles (voir plus bas) |
| La carte | `ressources/carte.csv`, `carte.md` | Inventée pour la formation (jour 1) |
| 30 réservations | `ressources/reservations.csv` et `exercices/17-reservations/depart/reservations.csv` | Inventées pour la formation : noms fictifs choisis, sans correspondance recherchée avec des personnes réelles, courriels en `@example.com`, téléphones dans les tranches que l'Arcep réserve à la fiction audiovisuelle (01 99 00 et 06 39 98, voir ci-dessous). Les commentaires piégés (un tiers nommé, un numéro de tiers, une allergie, une instruction cachée) sont écrits exprès |
| Historique de 120 demandes de réservation | `exercices/24-revue-user-story/depart/historique.csv` | Inventé pour la formation. Les codes postaux 99001 à 99004 n'existent pas : ils ne désignent aucune commune réelle |
| Réponse « d'un assistant » | `exercices/18-avant-d-executer/depart/reponse-ia.md` | Texte écrit pour l'exercice, pas une vraie sortie de modèle |
| Sortie de `docker history` | `exercices/20-fuites-dockerfile/depart/historique-docker.txt` | Sortie réelle, relevée le 02/11/2026 avec Docker 25.0.3 sur une image construite pour l'occasion, avec un faux jeton visiblement faux |
| Trois cas de propriété du code | `exercices/22-a-qui-est-ce-code/depart/cas.md` | Inventés pour la formation |

## Les numéros de téléphone

Les téléphones des réservations sont dans les tranches que l'Arcep réserve aux œuvres audiovisuelles : racines 01 99 00, 02 61 91, 03 53 01, 04 65 71, 05 36 49 et 06 39 98. Source : Arcep, décision n° 2018-0881, annexe, rubrique « Numéros pour œuvres audiovisuelles », document chargé sur arcep.fr le 02/11/2026. Ces numéros ne peuvent pas faire l'objet d'une attribution par l'Arcep. Un outil de validation de numéros peut les refuser (constat d'un site tiers, non vérifié ici) : un message « numéro invalide » pendant un essai n'est pas forcément un bug de votre code.

## Les courriels

Tous les courriels sont en `@example.com`, domaine réservé aux exemples : aucun message n'arrivera à une vraie personne.
