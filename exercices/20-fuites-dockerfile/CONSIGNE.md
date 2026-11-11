# E20 · Trois fuites dans un Dockerfile

**Point du programme** : publication d'images Docker et confidentialité des données d'entreprise.

**Durée** : 10 minutes.

## Ce qu'on fait

Une image Docker se publie : celui qui la télécharge reçoit tout ce qu'elle contient, y compris ce qu'on a cru supprimer. `exercices/20-fuites-dockerfile/depart/` contient le `Dockerfile` d'un Pigala qui n'a rien d'un vrai déploiement, et la sortie réelle de `docker history`. Vous lisez, vous trouvez trois fuites, vous écrivez la version corrigée.

**Docker n'est exigé de personne.** Tout se fait en lisant les fichiers. Les jetons sont de faux jetons visiblement faux. Si vous avez Docker, un chemin facultatif à l'étape 5 refait le relevé ; il télécharge l'image de base `ubuntu:24.04` (environ 78 Mo une fois installée). La formatrice fait la démonstration sur son poste sans afficher la liste de ses images.

Dix minutes pour huit gestes, c'est court : un **seul commit**, à la fin (étape 7), et l'étape 6 (le prompt à l'outil) ne se fait que si le temps le permet. Les étapes 1 à 4 sont le cœur de l'exercice.

### Étape 1 : lire le Dockerfile, sans l'IA

Ouvrez `exercices/20-fuites-dockerfile/depart/Dockerfile`. Sept lignes. Avant tout outil, ouvrez `exercices/20-fuites-dockerfile/depart/reponses.md` et notez, dans la section « Étape 1 » : à quel endroit, selon vous, un secret peut rester dans l'image ? Quelques minutes, pas plus.

### Étape 2 : lire ce que l'image raconte d'elle-même

Ouvrez `exercices/20-fuites-dockerfile/depart/historique-docker.txt`. C'est la sortie réelle de `docker history --no-trunc`, qui affiche chaque commande qui a construit l'image. Cherchez-y le faux jeton (« jeton-factice-pigala-0000 ») et la ligne « cle-factice ». Résultat attendu : le faux jeton apparaît dans **deux** lignes (celle de l'`ARG` et celle de la commande `RUN` qui l'utilise), et la clé factice dans la ligne `ENV`. Toute personne qui peut télécharger l'image peut lancer cette commande.

### Étape 3 : ce que la copie embarque

Regardez la ligne `COPY . .` puis la liste des fichiers du dossier `depart/` : `app.py`, `reservations.csv`, `secrets.env`. Il n'existe pas de fichier `.dockerignore`. Que contient donc l'image à cet endroit ? Écrivez la réponse en une phrase dans `reponses.md` (section « Étape 3, première question »).

Puis la ligne `RUN ... rm secrets.env` : le fichier est supprimé. Pensez-vous que le jeton a disparu de l'image ? Écrivez votre réponse dans `reponses.md` (section « Étape 3, seconde question ») avant l'étape suivante.

### Étape 4 : la preuve

Ouvrez `exercices/20-fuites-dockerfile/depart/preuve-couches.txt`. C'est un relevé réel du 02/11/2026. Lisez-le : le fichier supprimé est toujours dans la couche 3. La suppression de la couche 4 n'ajoute qu'une marque par-dessus. Comparez avec votre réponse de l'étape 3.

### Étape 5 (facultative, si Docker est installé) : refaire le relevé

Depuis la racine. Le premier relevé construit l'image, le second affiche son historique, le troisième la supprime par son nom (rien d'autre n'est touché) :

```
docker build -t pigala-demo:fuite exercices/20-fuites-dockerfile/depart
```

```
docker history --no-trunc --format "{{.CreatedBy}}" pigala-demo:fuite
```

```
docker rmi pigala-demo:fuite
```

Résultat attendu : le deuxième affiche les mêmes lignes que `historique-docker.txt`. Si le démon répond « Cannot connect to the Docker daemon », Docker Desktop n'est pas démarré : sautez cette étape, rien n'a été construit. N'utilisez jamais `docker images` devant le groupe : votre poste peut afficher les images d'un autre projet.

### Étape 6 (seulement si le temps le permet) : écrire la version corrigée

Si le temps manque, passez directement à l'étape 7 : les réponses des étapes 1 et 3 sont l'essentiel, la version corrigée peut se faire plus tard.

Dans Claude Code ou Copilot en mode Agent (vérifiez le sélecteur après un « New Chat ») :

```
Dans exercices/20-fuites-dockerfile/depart/, lis le Dockerfile et historique-docker.txt. Crée Dockerfile.corrige et .dockerignore : plus aucun secret dans ARG, ENV ni COPY ; le jeton est lu par un secret de build (RUN --mount=type=secret) ; seul app.py est copié ; le .dockerignore écarte secrets.env, reservations.csv, les fichiers .db et le dossier .git. N'exécute aucune commande Docker.
```

Relisez le résultat avec votre grille : le jeton est-il écrit quelque part en clair ? Reste-t-il un `ARG` ou un `ENV` qui porte une valeur secrète ? Le `COPY` est-il limité à ce qui sert ? L'outil peut corriger deux fuites sur trois et en oublier une : c'est à vous de compter.

### Étape 7 : enregistrer (le seul commit de l'exercice)

Depuis la racine de `stagiaire_J2` :

```
git add exercices/20-fuites-dockerfile
```

```
git commit -m "E20 : réponses, Dockerfile corrigé et .dockerignore"
```

Résultat attendu : une ligne « N files changed ». `git show --stat` affiche la liste des fichiers : `reponses.md`, et `Dockerfile.corrige` et `.dockerignore` si vous avez fait l'étape 6. « nothing to commit » signifie qu'aucun fichier n'a changé : `reponses.md` est-il rempli et enregistré dans l'éditeur ?

## Livrable

`reponses.md` avec vos réponses des étapes 1 et 3, et un seul commit. `Dockerfile.corrige` et `.dockerignore` s'y ajoutent si le temps a permis l'étape 6.

## Ce qu'on retient

- `ARG` et `ENV` restent dans l'historique de l'image : un secret ne s'y met jamais.
- `COPY . .` embarque tout le dossier. Sans `.dockerignore`, une base de clients part avec l'image.
- Supprimer un fichier dans une couche suivante ne l'enlève pas de la couche d'avant.
- Une image publiée est une copie que vous ne contrôlez plus.
