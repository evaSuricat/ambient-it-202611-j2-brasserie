# E11 · La carte en base

**Point du programme** : le vibe coding et SQL ; la page devient une petite application.

**Durée** : 15 minutes.

**Premier exercice du Jour 2** : il reprend l'exercice 11 du Jour 1, et il vérifie aussi que votre poste marche (Git, Python, votre outil, Chrome).

## Ce qu'on fait

`exercices/11-carte-en-base/depart/` contient la page du Pigala (la même pour tout le monde) et `carte.csv`. Vous travaillez à la racine du dépôt cloné, dans VS Code, et chaque commande de cet exercice se lance depuis la racine de `stagiaire_J2` sauf quand la consigne dit de faire `cd`. La carte, aujourd'hui écrite dans le HTML, va vivre dans une base SQLite servie par Python. SQLite est inclus dans Python : rien à installer.

Claude Code demande un abonnement payant. Sans abonnement, faites les mêmes prompts dans le chat de GitHub Copilot Free (sélecteur sur **Agent**), ou suivez sur l'écran partagé de la formatrice. Mode de permissions **Manual** dans Claude Code : lisez chaque permission avant de l'accepter.

### Étape 0 : vérifier le poste, puis enregistrer le point de départ

Depuis la racine de `stagiaire_J2`, dans un terminal de VS Code, une ligne après l'autre :

```
git --version
```

```
python --version
```

Résultat attendu : une ligne `git version 2...`, puis `Python 3.12.x`. Si `python` n'existe pas (Mac, certains Linux), tapez `python3` ici et partout dans cet exercice. Une erreur « n'est pas reconnu » ou « command not found » : l'outil n'est pas installé ou pas dans le chemin ; ne l'installez pas vous-même, dites-le à la formatrice. Un `Python 3.10` ou `3.14` n'empêche pas l'exercice, notez-le.

```
git add exercices/11-carte-en-base
```

```
git commit -m "E11 : état de départ"
```

Résultat attendu : une ligne « files changed » ; « nothing to commit » est normal si rien n'a changé depuis le clonage.

### Étape 1 : se placer dans le dossier de l'exercice

```
cd exercices/11-carte-en-base/depart
```

```
pwd
```

Résultat attendu : un chemin qui se termine par `exercices/11-carte-en-base/depart`. Sinon, revenez à la racine avec `cd ../../..` et recommencez.

### Étape 2 : trois prompts, envoyés un par un

Dans Claude Code, envoyez-les l'un après l'autre : attendez sa réponse avant le suivant.

Premier prompt :

```
Dans exercices/11-carte-en-base/depart/, écris charger.py : il crée carte.db (SQLite) avec une table carte (id, categorie, nom, description, prix) et la remplit depuis carte.csv. Relançable : il vide la table avant de recharger.
```

Deuxième prompt :

```
Dans exercices/11-carte-en-base/depart/, écris servir.py : un serveur http.server sur 127.0.0.1:8000 (le port peut être donné en argument : python servir.py 8001) qui sert ce dossier sans cache, et répond sur /api/carte avec la carte en JSON, triée par catégorie puis par nom. Ne lance pas le serveur toi-même : je le lancerai dans mon terminal.
```

Troisième prompt :

```
Dans exercices/11-carte-en-base/depart/index.html, la carte est écrite en deux listes HTML : « Bières et cidre » et « À manger ». Remplace ces listes par des listes vides, une par catégorie de carte.csv, remplies par un script.js qui appelle /api/carte. Garde la carte actuelle dans un <noscript>. Si l'appel échoue, la page affiche : La carte n'a pas pu être chargée. Pas de bibliothèque.
```

### Étape 3 : lire avant de lancer

**Lisez chaque requête SQL avant de lancer** : `CREATE TABLE`, `INSERT`, `SELECT`. Demandez « explique la requête » au moindre doute. Lisez aussi le texte ajouté pour les erreurs : c'est vous qui le validez.

### Étape 4 : charger la base

Dans le terminal où vous êtes (le dossier `depart`) :

```
python charger.py
```

Résultat attendu : une ligne qui annonce vingt lignes chargées, et `carte.db` qui apparaît dans l'explorateur. Vous pouvez le relancer sans risque : il vide la table avant de recharger.

### Étape 5 : lancer le serveur dans son propre terminal

Un serveur ne rend jamais la main : si Claude Code le lance à votre place, la conversation reste bloquée. Si cela arrive, `Ctrl+C` dans le terminal, ou dites à Claude Code de ne pas lancer le serveur. Ouvrez un deuxième terminal (bouton **+** en haut à droite du panneau Terminal), puis :

```
cd exercices/11-carte-en-base/depart
```

```
python servir.py
```

Résultat attendu : une adresse affichée, puis le terminal reste en attente. C'est normal. `Ctrl+C` l'arrête. Si le port 8000 est pris, relancez avec `python servir.py 8001` et changez le numéro dans l'adresse de Chrome.

### Étape 6 : regarder dans Chrome

Ouvrez http://127.0.0.1:8000/. La carte s'affiche, triée par ordre alphabétique, le tri demandé (`carte.md` suit un autre ordre). F12, onglet **Network** (Réseau), F5 : une ligne `carte` apparaît, avec le statut 200. Cliquez dessus : **Preview** montre les vingt plats, **Initiator** montre que c'est `script.js` qui les a demandés.

### Étape 7 : la preuve que la carte vient de la base

Changez un prix dans la base et rechargez la page. Dans le premier terminal (celui qui n'est pas occupé par le serveur) :

```
python -c "import sqlite3; c=sqlite3.connect('carte.db'); c.execute('UPDATE carte SET prix=3.9 WHERE nom=?', ('Pigala Blonde',)); c.commit()"
```

Résultat attendu : aucune réponse à l'écran, puis, après rechargement, Pigala Blonde à 3,90 €, sans que `index.html` ait changé. Le changement est déjà enregistré dans la base. Remettez ensuite le vrai prix :

```
python charger.py
```

Attention : `charger.py` efface la table et la recharge depuis `carte.csv`. Tout changement fait seulement dans la base est alors perdu. Où est la vérité : dans le CSV ou dans la base ?

### Étape 8 : le cas d'erreur

Arrêtez le serveur (`Ctrl+C` dans son terminal), puis F5 dans Chrome : « Ce site est inaccessible ». C'est normal, le serveur envoyait toute la page. Ouvrez maintenant `exercices/11-carte-en-base/depart/index.html` par double-clic : la page s'affiche, avec le message « La carte n'a pas pu être chargée. » à la place de la carte.

### Étape 9 : enregistrer

Depuis la racine, dans le premier terminal :

```
cd ../../..
```

```
git add exercices/11-carte-en-base
```

```
git commit -m "E11 : carte en base SQLite, servie par Python et lue par script.js"
```

Résultat attendu : une ligne « files changed », avec `charger.py`, `servir.py` et `script.js`. Un commit se défait : rien n'est perdu.

## Livrable

`charger.py`, `carte.db`, `servir.py`, `script.js`, la page branchée sur l'API. F12, onglet Réseau : la requête `/api/carte` apparaît.

## Ce qu'on retient

À partir d'ici, le double-clic ne suffit plus : la carte passe par le serveur, il faut `python servir.py` pour voir la page complète. L'IA écrit du SQL juste la plupart du temps, et faux de temps en temps, avec la même assurance. Cet exercice a aussi servi à vérifier votre poste : si quelque chose a coincé, c'est le bon moment pour le dire. La suite de la journée reprend cette base : l'exercice 15 ajoute les photos à la page, puis les exercices 17 et 21 y ajoutent les réservations, dans la même base, avec des données personnelles : ce qu'on envoie au modèle, ce qu'on anonymise.
