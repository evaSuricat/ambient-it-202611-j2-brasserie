# Bonus · Un formulaire de réservation robuste

**Point du programme** : bonus pour ceux qui ont fini avant les autres. Mettre le formulaire du Pigala à l'épreuve : messages d'erreur accessibles, frein anti-spam, tests.

**Durée** : 20 à 30 minutes. Le bonus se fait seul ou à deux, après l'exercice 21 ou 23. Rien n'y est obligatoire pour la suite.

## Ce qu'on fait

Le formulaire de l'exercice 17 enregistre une réservation. Trois choses lui manquent pour tenir en vrai : dire clairement à la personne ce qui ne va pas dans sa saisie, y compris avec un lecteur d'écran ou au clavier seul ; ne pas se laisser inonder par des robots ; avoir des tests qui le disent. Vous complétez la page et le serveur jusqu'à ce que `test_formulaire.py` passe, puis vous essayez le résultat.

Le dossier de départ est la solution de l'exercice 21 (serveur sécurisé), plus `test_formulaire.py`. Tout est fictif. Sans abonnement Claude Code : Copilot Free en mode **Agent** (« New Chat » repasse en Ask : remettez Agent), ou suivez sur l'écran partagé. Mode de permissions **Manual**.

### Étape 0 : enregistrer le point de départ

Depuis la racine de `stagiaire_J2` :

```
git add exercices/bonus-formulaire
```

```
git commit -m "Bonus : état avant le formulaire robuste"
```

Résultat attendu : « nothing to commit » est normal.

### Étape 1 : les tests, au rouge

```
cd exercices/bonus-formulaire/depart
```

```
python -m unittest test_formulaire -v
```

Résultat attendu : `Ran 5 tests`, `FAILED (failures=4)`. Un test passe : « une demande valide est acceptée ». Lisez le début de `test_formulaire.py` : il décrit le contrat du serveur (champ piège, délai minimal, cinq envois par minute, un message par champ fautif). Si `python` n'existe pas, tapez `python3`.

### Étape 2 : le serveur

```
Dans exercices/bonus-formulaire/depart/, lis AGENTS.md à la racine du dépôt, servir.py et test_formulaire.py. Modifie servir.py pour que test_formulaire.py passe, sans casser test_securite.py : champ piège « site_web » (rempli : répondre 201 sans rien enregistrer), refus (400) d'un envoi moins de 3 secondes après « ouvert_a », au plus 5 envois par minute et par adresse (429 au suivant), et une réponse 400 qui contient un message lisible par champ fautif dans « champs ». Ne lance pas le serveur.
```

Relisez avant d'accepter : le champ piège répond-il bien comme si tout allait bien ? La limite par minute est-elle stockée en mémoire (elle repart à zéro quand le serveur redémarre) ? Puis :

```
python -m unittest test_formulaire test_securite
```

Résultat attendu : `OK`, onze tests. Si `test_securite` échoue, la modification du serveur a ouvert une faille : corrigez avant d'aller plus loin.

### Étape 3 : la page

```
Dans exercices/bonus-formulaire/depart/, lis AGENTS.md à la racine du dépôt, index.html, reservations.js et css/reservation.css. Améliore le formulaire de réservation : attribut novalidate ; contrôle des champs dans reservations.js avec, sous chaque champ fautif, un message lié par aria-describedby et un aria-invalid ; un résumé des erreurs en haut du formulaire (role="alert", focus placé dessus) dont chaque ligne est un lien vers son champ ; un champ piège « site_web » invisible pour une personne et ignoré des lecteurs d'écran (aria-hidden, tabindex -1) ; l'envoi de « ouvert_a » (heure d'ouverture de la page en millisecondes) ; l'affichage des messages par champ renvoyés par le serveur. Une erreur ne se signale jamais par la couleur seule. Respecte les conventions d'AGENTS.md. Ne lance pas le serveur.
```

### Étape 4 : essayer au clavier seul

Dans le deuxième terminal (`cd exercices/bonus-formulaire/depart`, puis `python servir.py`), ouvrez http://127.0.0.1:8000/ dans Chrome. **Sans la souris** : Tab jusqu'au bouton d'envoi, Entrée avec le formulaire vide.

Résultat attendu : le focus passe sur le résumé des erreurs, qui compte les champs à corriger ; chaque ligne est un lien (Entrée) qui amène sur son champ ; sous chaque champ fautif un message commence par un mot qui n'est pas une couleur. Corrigez les champs, renvoyez : « Votre demande est enregistrée. » Attendez-vous à une erreur « Envoi trop rapide » si vous envoyez dans les trois secondes qui suivent le chargement de la page : c'est le frein du serveur. Dites ce que vous ressentez : un humain pressé est-il pénalisé ? `Ctrl+C` arrête le serveur.

### Étape 5 : enregistrer

Depuis la racine :

```
cd ../../..
```

```
git add exercices/bonus-formulaire
```

```
git commit -m "Bonus : formulaire robuste, messages accessibles, anti-spam, tests"
```

Résultat attendu : une ligne « files changed » qui cite `servir.py`, `reservations.js` et `index.html`.

## Livrable

`test_formulaire.py` et `test_securite.py` au vert (onze tests), un formulaire utilisable au clavier avec messages d'erreur, un ou deux commits : avant, quand quelque chose a changé, et après.

## Ce qu'on retient

- Les contrôles côté navigateur améliorent l'expérience ; seul le serveur protège. Il revalide tout.
- Un champ piège, un délai minimal et une limite par minute écartent les robots naïfs. Aucun n'arrête un attaquant déterminé : ce sont des freins, pas des barrières.
- Un message d'erreur accessible se relie à son champ, se lit sans la couleur, et se retrouve au clavier.
