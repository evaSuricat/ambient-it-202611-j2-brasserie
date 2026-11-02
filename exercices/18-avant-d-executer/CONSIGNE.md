# E18 · Avant d'exécuter

**Point du programme** : sécurité avant exécution du code ; hallucinations ; code dangereux.

**Durée** : 15 minutes.

## Ce qu'on fait

`exercices/18-avant-d-executer/depart/reponse-ia.md` est une réponse figée d'un assistant à la question « comment sécuriser la table des réservations et nettoyer les anciennes ? ». Elle a l'air sérieuse. Elle contient du juste et du faux. Votre travail : trier, **sans rien exécuter ni installer**, et savoir dire comment vous avez vérifié chaque point. Le fichier est écrit pour l'exercice (voir `SOURCES.md`) : ce n'est pas une vraie sortie de modèle, mais il imite des erreurs réelles de ce type d'outil.

Cet exercice se fait sans abonnement : le navigateur et vos yeux suffisent. L'étape 6 utilise votre outil, Claude Code ou Copilot Free, et peut se suivre sur l'écran partagé.

### Étape 0 : enregistrer le point de départ

Depuis la racine de `stagiaire_J2` :

```
git add exercices/18-avant-d-executer
```

```
git commit -m "E18 : état avant le tri"
```

Résultat attendu : « nothing to commit » est normal si vous n'avez rien changé depuis le clonage. Sinon, une ligne « files changed ».

### Étape 1 : lire en entier, sans rien copier

Ouvrez `exercices/18-avant-d-executer/depart/reponse-ia.md` et `exercices/18-avant-d-executer/depart/tri.md`. Lisez la réponse une fois en entier. Ne copiez aucune commande dans un terminal.

### Étape 2 : premier tri, à l'œil

Dans `tri.md`, remplissez la colonne « Verdict » pour chaque ligne avec ce que vous pensez **avant toute vérification** (juste, faux, à ignorer). Notez-vous une certitude de 1 à 3 à côté. Vous la comparerez à la fin.

### Étape 3 : le paquet existe-t-il ?

Dans Chrome, ouvrez cette adresse (elle interroge l'index officiel des paquets Python, sans rien installer) :

```
https://pypi.org/pypi/sqlite3-reservation-guard/json
```

Résultat attendu : une page qui dit « Not Found » (code 404) : le paquet n'existe pas sur PyPI. Relevé le 02/11/2026 à 20 h 14 UTC. **N'installez rien.** Si la page affiche des données de paquet à la place, quelqu'un l'a déposé depuis : c'est le vrai danger de ce piège (un nom inventé par un modèle peut être réservé par un tiers qui y met du code malveillant), et le verdict devient « suspect : à ne pas installer sans enquête ». Dans les deux cas, ne lancez pas `pip install`.

### Étape 4 : l'adresse de documentation existe-t-elle ?

Dans Chrome :

```
https://docs.python.org/3/library/sqlite3-secure.html
```

Résultat attendu : une page d'erreur 404 (relevé le 02/11/2026). La vraie page du module est `https://docs.python.org/3/library/sqlite3.html`, que vous pouvez ouvrir pour comparer : un modèle peut inventer une adresse plausible sur un site réel. Un lien dans une réponse d'IA se clique avant de s'y fier.

### Étape 5 : les deux commandes dangereuses

**Le `curl | bash`.** Ne le lancez pas. Regardez le nom de domaine : `installer.pigala.invalid`. Le suffixe `.invalid` est réservé pour ne jamais exister (RFC 2606) : la commande échouerait, mais avec un vrai domaine, elle téléchargerait un script et l'exécuterait sans que vous l'ayez lu. Notez dans `tri.md` ce que vous auriez fait avec un vrai domaine (télécharger d'abord dans un fichier, le lire, puis décider).

**Le `DELETE FROM reservations;`.** Lisez-la : où est le `WHERE` ? Prouvez l'effet, sur une **copie** de la base. Depuis la racine :

```
python -c "import shutil; shutil.copy('exercices/17-reservations/depart/carte.db', 'exercices/18-avant-d-executer/depart/copie.db')"
```

```
python -c "import sqlite3; c=sqlite3.connect('exercices/18-avant-d-executer/depart/copie.db'); c.execute('DELETE FROM reservations'); c.commit(); print(c.execute('SELECT COUNT(*) FROM reservations').fetchone())"
```

Résultat attendu : `(0,)` : toutes les réservations de la copie ont disparu. Votre vraie base n'a pas été touchée. Supprimez ensuite la copie :

```
rm exercices/18-avant-d-executer/depart/copie.db
```

Si `python` n'existe pas, tapez `python3`. Si la première ligne répond `FileNotFoundError`, vous n'avez pas encore de `carte.db` dans l'exercice 17 : faites d'abord l'exercice 17, ou clonez le dépôt à nouveau.

### Étape 6 : un agent en renfort

Ouvrez `exercices/18-avant-d-executer/depart/relecture-agent.md` : c'est le verdict d'un second agent, écrit pour l'exercice, qui trouve la réponse correcte. Ensuite, demandez à votre propre outil de relire la réponse. Dans Claude Code ou Copilot en mode Agent (vérifiez le sélecteur après un « New Chat », qui repasse en Ask) :

```
Lis exercices/18-avant-d-executer/depart/reponse-ia.md et dis ce qui est faux ou dangereux. N'exécute rien et n'installe rien.
```

Notez dans `tri.md`, en bas, **l'outil et le modèle** utilisés et ce qu'il a trouvé. Sa réponse est une donnée de plus à trier, pas un verdict : il peut oublier un piège, en inventer un, ou valider le faux avec aplomb. Avec Copilot Free, GitHub choisit le modèle : notez ce que l'interface affiche.

### Étape 7 : remplir le tri et enregistrer

Complétez `tri.md` (verdict, pourquoi, comment vérifié) et ses trois lignes de conclusion. Comparez avec votre premier tri de l'étape 2 : sur quels points avez-vous changé d'avis, et grâce à quoi ? Depuis la racine :

```
git add exercices/18-avant-d-executer
```

```
git commit -m "E18 : tri de la réponse de l'assistant"
```

Résultat attendu : une ligne « files changed » qui cite `tri.md`.

## Livrable

`exercices/18-avant-d-executer/depart/tri.md` rempli : juste, faux, à ignorer, et pourquoi, avec le moyen de vérification de chaque ligne.

## Ce qu'on retient

- Trois gestes qui ne dépendent d'aucun modèle : chercher le paquet sur l'index officiel, cliquer le lien, lire la commande avant de la lancer.
- Une réponse qui mêle du juste (paramètres `?`, copie de sauvegarde) et du faux est plus dangereuse qu'une réponse entièrement fausse : le juste donne confiance dans le faux.
- Un second agent relit avec la même confiance que le premier. Il peut aider ; il ne remplace pas votre tri.
