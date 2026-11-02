# User story : « Le tri automatique des réservations »

Texte proposé par le gérant du Pigala à son équipe. Il est fictif et écrit pour l'exercice.

**En tant que** gérant du Pigala, **je veux** qu'une IA trie les demandes de réservation et rédige la réponse, **afin de** ne plus y passer mes soirées.

## Détails

- Le formulaire de la page ajoute un champ **code postal**, obligatoire.
- À chaque demande, l'IA lit : nom, téléphone, courriel, code postal, date, nombre de personnes et commentaire.
- Pour estimer le risque que la personne ne vienne pas, l'IA s'appuie sur l'historique des 120 dernières demandes (`historique.csv`).
- Si le risque d'absence est jugé élevé, l'IA **refuse** la demande. Sinon, elle l'accepte.
- L'IA rédige la réponse au client et **l'envoie automatiquement** par courriel, sans relecture.
- Exemple de réponse rédigée par l'IA : « Bonjour, votre table de 6 personnes est réservée samedi à 21 h 30 au Pigala. À samedi ! »

## Critères d'acceptation (version du gérant)

- Le gérant n'a plus rien à faire.
- Le client reçoit une réponse en moins d'une minute.
- Le taux d'absence baisse.
