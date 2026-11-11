# E18 · Avant d'exécuter

**Point du programme** : sécurité avant exécution du code ; hallucinations ; code dangereux.

**Durée** : 10 minutes.

## Ce qu'on fait

Un tri **à l'oral**, projeté par la formatrice, **sans outil IA** : ni Claude Code, ni Copilot, ni terminal. Aucun livrable, aucun commit.

`exercices/18-avant-d-executer/depart/reponse-ia.md` est une réponse figée d'un assistant à la question « comment sécuriser la table des réservations et nettoyer les anciennes ? ». Elle a l'air sérieuse. Elle contient du juste et du faux. Le fichier est écrit à la main pour l'exercice (voir `exercices/18-avant-d-executer/depart/SOURCES.md`) : il imite des erreurs réelles de ce type d'outil.

### Étape 1 : lire (3 minutes)

Chacun ouvre `exercices/18-avant-d-executer/depart/reponse-ia.md` (ou suit l'écran projeté) et le lit une fois en entier. Ne copiez aucune commande dans un terminal, n'installez rien.

### Étape 2 : noter quatre points (3 minutes)

Sur un brouillon (papier ou fichier hors du dépôt), notez les **quatre points** que vous jugez faux ou dangereux. Pour chacun, une phrase : pourquoi, et comment vous le vérifieriez (l'œil, le navigateur, une recherche, un essai sur une copie). Une règle : **vérifier ne veut jamais dire exécuter** ce qu'on n'a pas lu.

### Étape 3 : mise en commun à l'oral (4 minutes)

La formatrice fait le tour de la salle : chaque point nommé est discuté, avec son moyen de vérification. Elle ouvre ce qu'il faut ouvrir à l'écran (la page d'un index de paquets, une page de documentation, un domaine). Comparez votre liste à ce qui est dit : un point manqué n'est pas une faute, c'est l'intérêt de l'exercice.

Résultat attendu : à la fin, la salle s'accorde sur les quatre points, et sur le fait que certains éléments de la réponse sont justes (ils donnent confiance dans le faux).

## Ce qu'on retient

- Trois gestes qui ne dépendent d'aucun modèle : chercher le paquet sur l'index officiel, cliquer le lien, lire la commande avant de la lancer.
- Une réponse qui mêle du juste (paramètres `?`, copie de sauvegarde) et du faux est plus dangereuse qu'une réponse entièrement fausse : le juste donne confiance dans le faux.
- Un second agent qui relit avec la même confiance que le premier peut valider le faux. Il peut aider ; il ne remplace pas votre tri.
