# E24 · Revue d'une user story

**Point du programme** : atelier officiel « user story » : biais, risques, décisions automatisées. Public mixte (développeurs, sécurité, chefs de projet, autres métiers) : **on ne code pas**.

**Durée** : 20 minutes, **en plénière** : toute la salle ensemble, sur l'écran partagé de la formatrice. Vous parlez, vous n'écrivez rien d'obligatoire.

## Le contexte en trois phrases

Le gérant du Pigala veut qu'une IA trie les demandes de réservation et écrive la réponse aux clients, pour ne plus y passer ses soirées. Il a écrit sa demande sous forme de **user story** : une courte phrase qui décrit ce qu'on veut, du point de vue de la personne qui s'en servira (« en tant que..., je veux..., afin de... »). Elle est suivie de ses **critères d'acceptation** : les conditions qui disent que la demande est réussie, et qui doivent pouvoir se vérifier par oui ou par non.

Tout est fictif (`exercices/24-revue-user-story/depart/SOURCES.md`). Les codes postaux 99001 à 99004 n'existent pas.

## Ce qu'on regarde

La formatrice, sur son écran :

1. lit la user story (`exercices/24-revue-user-story/depart/user-story.md`) ;
2. lance `python calcul.py`, qui compte les absences des 120 dernières demandes par code postal et par créneau horaire ;
3. demande à une IA de lister les risques de la user story.

La salle repère les risques à l'oral. Ensuite la formatrice projette une user story réécrite après la revue : on y cherche ce que vous avez dit, et ce qui manque encore. Vous repartez avec ce texte : `exercices/24-revue-user-story/apres-la-revue/user-story-apres-revue.md`. Ne l'ouvrez pas avant la discussion, vous vous priveriez de l'exercice. Si vous voulez suivre par écrit, le fichier `grille-risques.md` du dossier `depart/` est là, c'est facultatif.

## Les questions à se poser à l'oral

- Le code postal sert-il à réserver une table ?
- Refuser une table selon le quartier, est-ce juste ? Le calcul montre des taux d'absence plus élevés dans deux zones : que se passe-t-il pour les gens qui y habitent ?
- La réservation n° 15 (`ressources/reservations.csv`) contient une instruction cachée dans son commentaire. Que se passe-t-il si une IA qui lit cette ligne a le pouvoir d'accepter ou de refuser ?
- « Le taux d'absence baisse » : comment le vérifier ? Qui mesure, sur quoi, comparé à quoi ?
- Quelles données envoie-t-on au modèle, et sont-elles toutes nécessaires ? (Revoyez l'exercice 21.)
- Sur quoi l'IA s'appuie-t-elle pour dire qu'il reste une table ? Cherchez dans la user story : les tables déjà réservées pour ce service, et celles qu'un restaurant garde pour les clients qui viennent sans réserver.

## L'article 22 du RGPD, en une phrase

Cet article pose qu'une personne a le droit de ne pas faire l'objet d'une décision prise **uniquement** par un traitement automatique, quand cette décision a des effets importants sur elle, avec quelques exceptions (texte : [EUR-Lex, règlement 2016/679](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679), lu le 02/11/2026). La consigne ne dit pas qu'il s'applique au Pigala : refuser une table a-t-il un effet important ? C'est une question à garder ouverte, et à poser à un juriste.

## Le message à retenir

L'IA propose, les personnes trient : ce qu'elle oublie se voit avec des yeux de métiers différents. Un code postal n'est pas neutre. Un critère d'acceptation se mesure. Une décision automatique qui touche une personne se discute avant d'être construite.
