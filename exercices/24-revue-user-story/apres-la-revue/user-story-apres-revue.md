# User story après la revue : « Les réservations du Pigala »

Une réécriture possible de la user story du gérant, après la revue en salle. Ce n'est pas « la » bonne réponse : c'est un exemple de ce que donne une demande quand on a écouté des personnes de métiers différents. Tout est fictif, comme le reste de l'exercice. Aucun avis juridique.

## Ce qui a changé, en quatre lignes

- La demande du gérant faisait tout d'un coup. Elle est découpée en **trois petites user stories**.
- **Compter les tables est un travail du code**, pas de l'IA.
- **L'IA ne décide plus rien et n'envoie plus rien.** Il lui reste une tâche : rédiger les phrases d'accompagnement d'un brouillon de réponse.
- **Le code postal a disparu**, et avec lui le refus selon le quartier.

## Ce que le gérant a décidé (exemples fictifs)

Ces chiffres ne se devinent pas : il a fallu les demander au gérant.

| Décision | Valeur |
|---|---|
| Tables du restaurant | 30 : 14 tables de 2, 12 tables de 4, 4 tables de 6 |
| Services | un le midi (12 h 30), deux le soir (19 h 30 et 21 h 30) |
| Tables gardées à chaque service pour les clients sans réservation | 7 : 4 tables de 2, 2 tables de 4, 1 table de 6 |
| Tables ouvertes à la réservation, par service | 23 : 10 tables de 2, 10 tables de 4, 3 tables de 6 |
| Groupes de plus de 6 personnes | par téléphone, avec le gérant |

## User story 1 : savoir s'il reste une table

**En tant que** gérant du Pigala, **je veux** que chaque demande de réservation soit comparée aux tables encore libres pour ce service, **afin de** ne jamais promettre une table que je n'ai pas.

- Le programme compte, pour la date et le service demandés, les tables déjà réservées, par taille.
- Une demande prend une table de la plus petite taille qui convient (1 ou 2 personnes : table de 2 ; 3 ou 4 : table de 4 ; 5 ou 6 : table de 6). S'il n'en reste pas, elle prend une table plus grande.
- Les 7 tables gardées ne sont jamais proposées à la réservation.
- S'il ne reste aucune table qui convient, la demande va en **liste d'attente**. Personne n'est refusé par un programme.
- Aucune IA dans cette story : c'est un calcul.

Critères d'acceptation, à vérifier par oui ou par non :

- Avec 10 tables de 2 déjà réservées pour un service, une onzième demande de 2 personnes reçoit une table de 4 s'il en reste, sinon elle va en liste d'attente.
- Aucune demande ne reçoit une des 7 tables gardées (test avec un service complet).
- Le formulaire n'a pas de champ « code postal ».
- Une demande de 7 personnes ou plus reçoit le message « appelez-nous », avec le numéro.

## User story 2 : répondre au client

**En tant que** gérant du Pigala, **je veux** un brouillon de réponse prêt à valider pour chaque demande, **afin d'** y passer moins de temps sans laisser partir une erreur à mon nom.

- Dès que la demande arrive, le client reçoit un accusé de réception au texte fixe : « Votre demande est bien reçue. » Ce texte ne promet ni table ni délai.
- La phrase qui annonce le résultat (« votre table est réservée » ou « vous êtes en liste d'attente »), la date, le nombre de personnes et le numéro du restaurant sont écrits par le programme, à partir de la story 1. L'IA ne peut pas les changer.
- L'IA rédige seulement les phrases d'accompagnement du brouillon, à partir de quatre informations : la date, le service, le nombre de personnes et le résultat de la story 1 (table disponible, ou liste d'attente).
- L'IA ne reçoit ni le nom, ni le téléphone, ni le courriel, ni le commentaire. Le commentaire est affiché au gérant, et à lui seul.
- Le gérant relit, corrige si besoin, et clique pour envoyer. Rien ne part sans ce clic.
- La réponse donne la date complète, le nombre de personnes, le moyen d'annuler et le numéro du restaurant.
- Le formulaire dit, avant l'envoi : « Votre réponse est préparée avec l'aide d'une IA et relue par une personne. Vous pouvez aussi nous appeler. »

Critères d'acceptation :

- Aucun courriel de confirmation n'est parti sans un clic du gérant (le journal montre qui a validé, et quand).
- Ce qui est envoyé au modèle ne contient ni nom, ni téléphone, ni courriel, ni commentaire (test sur la requête envoyée).
- Un commentaire piégé (la réservation n° 15 et trois variantes) ne change ni le brouillon ni le résultat.
- La phrase de résultat d'une réponse est toujours l'une des deux phrases fixes du programme, et elle correspond au résultat de la story 1 (test sur un service complet et sur un service libre).

## User story 3 : les annulations et les absences

**En tant que** gérant du Pigala, **je veux** enregistrer une annulation et rappeler les clients la veille, **afin de** libérer les tables et de réduire les absences sans trier les clients.

- Le gérant enregistre une annulation (reçue par téléphone ou par courriel) : la table redevient libre dans le compte de la story 1.
- La première demande en liste d'attente pour ce service est alors proposée au gérant.
- Tous les clients reçoivent un rappel la veille, quel que soit leur quartier, avec le moyen d'annuler.
- Après le service, le gérant note **combien** de tables réservées sont restées vides. Il ne note pas qui : ce compte par service n'est relié à aucun nom.

Critères d'acceptation :

- Après une annulation, une nouvelle demande pour le même service et la même taille obtient la table libérée (test).
- Le rappel part pour toutes les réservations du lendemain, sans exception.
- Le taux d'absence est calculé par service, par un script qu'on peut relancer, sur deux mois, et comparé aux chiffres de départ : 16,7 % en tout, 32,6 % à 21 h 30 (`historique.csv`).
- Aucun calcul ne donne un taux par personne ni par zone, et aucun écran ne relie un nom à une absence.

## Ce qui reste à décider

- Le placement est volontairement simple : on compte les tables par taille. On ne cherche pas le meilleur plan de salle, on ne rapproche pas deux tables.
- Combien de temps dure un service, et peut-on réserver à 20 h 30 ?
- Que fait-on d'une table gardée restée vide à 21 h 45 ?
- Combien de temps garde-t-on une réservation passée et le relevé des absences ? (Voir la fiche de l'exercice 23.)
- Avec 120 demandes, un taux par service reste fragile : à partir de combien de demandes décide-t-on quelque chose ?
- Question pour un juriste, laissée ouverte : dans cette version, où le gérant valide chaque réponse, que reste-t-il à vérifier au regard des règles sur les décisions automatisées ?

## D'où viennent ces idées

| Idée | Qui l'a apportée |
|---|---|
| Compter les tables libres par service, garder des tables pour les clients sans réservation, enregistrer les annulations | Une personne qui connaît le métier (répétition du 16/11/2026) |
| L'écart entre quartiers vient surtout de l'heure ; un rappel la veille pour tout le monde | Le calcul, puis l'IA |
| Refuser des clients fait baisser le taux d'absence sans rien régler | L'IA |
| Le nombre de tables et la règle des tables gardées | Le gérant : personne d'autre ne pouvait le savoir |

À compléter avec ce que votre salle a trouvé.
