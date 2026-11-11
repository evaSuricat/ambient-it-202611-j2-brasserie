# E17 · Les réservations arrivent

**Point du programme** : le fil rouge reprend. La page du Pigala va enregistrer des noms, des téléphones et des courriels : des données personnelles.

**Durée** : 15 minutes.

## Ce qu'on fait

Vous partez de la page fournie dans `exercices/17-reservations/depart/` (la même pour tout le monde), vous lui ajoutez un formulaire de réservation, et vous vérifiez qu'une ligne arrive bien dans la base. Le serveur et la base des réservations (30 réservations fictives) sont fournis dans `exercices/17-reservations/depart/` : l'exercice porte sur la page, pas sur le serveur. Toutes les données sont fictives (voir `exercices/17-reservations/depart/SOURCES.md`). N'écrivez jamais vos vraies coordonnées dans le formulaire.

Claude Code demande un abonnement payant. Sans abonnement, faites les mêmes prompts dans le chat de GitHub Copilot Free (sélecteur sur **Agent**), ou suivez sur l'écran partagé de la formatrice. Mode de permissions **Manual** dans Claude Code : lisez chaque permission avant de l'accepter, une par une.

### Étape 1 : lancer le serveur, dans son propre terminal

Un serveur ne rend jamais la main. Ouvrez un deuxième terminal (bouton **+** du panneau Terminal), puis :

```
cd exercices/17-reservations/depart
```

```
pwd
```

```
python servir.py
```

Résultat attendu : `pwd` affiche un chemin qui se termine par `exercices/17-reservations/depart`, puis le serveur affiche `Le Pigala sur http://127.0.0.1:8000/` et reste en attente. Ouvrez cette adresse dans Chrome : la page s'affiche, sans formulaire. `Ctrl+C` arrête le serveur. Si le port 8000 est pris, `python servir.py 8001` et `8001` dans l'adresse.

Deux situations à ne pas confondre dans Chrome. « Ce site est inaccessible » : le serveur n'est pas lancé, rien n'écoute. Une ligne rouge **404** ou **500** dans la console (F12, onglet Console) : le serveur tourne, et c'est le code ou l'adresse qui est faux. Un 404 sur `favicon.ico` est normal : la page n'a pas d'icône.

### Étape 2 : demander le formulaire

Dans Claude Code (ou Copilot en mode Agent), ouvrez `exercices/17-reservations/depart/index.html` pour que l'outil sache de quel dossier on parle, puis envoyez ce prompt :

```
Dans exercices/17-reservations/depart/, lis AGENTS.md à la racine du dépôt et reservations.js. Ajoute à index.html, juste avant la section d'id venir, une section « Réserver une table » avec un formulaire. De reservations.js tu prends seulement les identifiants que le script attend : le formulaire a l'id form-reservation, ses champs ont pour name nom, telephone, email, date, couverts et commentaire, et un paragraphe d'id reservation-message avec role="status" affiche le résultat. Ne modifie pas reservations.js. Ajoute la balise script qui le charge, et une feuille css/reservation.css reliée dans le head, qui réutilise les variables de couleur déjà déclarées dans style.css. Nom, téléphone, date et nombre de personnes sont obligatoires ; courriel et commentaire sont facultatifs. Ne lance pas le serveur.
```

### Étape 3 : relire avant d'essayer

`AGENTS.md` exige un `label` par champ, un `autocomplete` adapté, les commentaires `DÉBUT` et `FIN` autour de la section, et une feuille dans `css/`. Une règle écrite ne garantit pas qu'elle soit appliquée : cochez chacune dans `index.html`. Vérifiez aussi que la balise `<script src="reservations.js">` est présente, et que les `name` des champs sont exactement ceux du prompt. Un `name` faux ne produit aucune erreur : le champ part vide.

### Étape 4 : envoyer une réservation fictive

Rechargez la page dans Chrome (F5). Remplissez le formulaire avec des valeurs inventées, par exemple le nom « Essai Stagiaire », le téléphone `06 39 98 00 00`, une date en décembre 2026, 2 personnes. Cliquez sur le bouton d'envoi.

Résultat attendu : sous le formulaire, le message « Votre demande est enregistrée (numéro 31). » (31 la première fois, 32 la suivante) et le formulaire se vide. Dans le terminal du serveur, une ligne `POST /api/reservations ... 201`.

Si la page se recharge et que l'adresse contient `?nom=Essai...` : le script n'est pas relié, le navigateur a envoyé le formulaire à sa façon, **avec vos données dans l'adresse**. Rien n'a été enregistré. Reprenez l'étape 3. Si un message d'erreur rouge s'affiche, voir l'étape 6.

### Étape 5 : voir la ligne dans la base

Dans le premier terminal (celui où le serveur ne tourne pas), à la racine puis dans le dossier de l'exercice :

```
cd exercices/17-reservations/depart
```

```
python -c "import sqlite3; c=sqlite3.connect('carte.db'); print(c.execute('SELECT id, nom, date, couverts FROM reservations ORDER BY id DESC LIMIT 1').fetchone())"
```

Résultat attendu : `(31, 'Essai Stagiaire', '2026-12-12', 2)`, avec vos valeurs. La commande lit seulement, elle ne modifie rien. `python charger_reservations.py` remet les 30 réservations d'origine si besoin.

### Étape 6 : le cas d'échec

Arrêtez le serveur (`Ctrl+C`), renvoyez le formulaire. Résultat attendu : « Votre demande n'a pas pu être envoyée. Appelez le 01 99 00 12 34. », et dans la console (F12) une erreur réseau, pas un 404. Relancez le serveur ensuite. Un 404 sur `/api/reservations` avec le serveur lancé voudrait dire que l'adresse du `fetch` est fausse.

### Étape 7 : enregistrer le résultat

Depuis la racine :

```
cd ../../..
```

```
git add exercices/17-reservations
```

```
git commit -m "E17 : formulaire de réservation branché sur /api/reservations"
```

Résultat attendu : une ligne « N files changed » et la liste des fichiers créés. `git show --stat` affiche la liste complète, dont `index.html`, `css/reservation.css` et la base `carte.db`. Un commit se défait : rien n'est perdu.

## Livrable

La page avec son formulaire, une ligne de plus dans la table `reservations`, un commit.

## Ce qu'on retient

- Le formulaire marche, et c'est tout ce qu'on a vérifié. On n'a pas demandé qui peut lire cette table maintenant qu'elle contient des noms, des téléphones et des courriels. Même fictifs, ils sont traités ici comme des vrais. On y revient à l'exercice 21.
- Une règle de `AGENTS.md` non appliquée ne produit aucune erreur : seule la relecture la voit.
