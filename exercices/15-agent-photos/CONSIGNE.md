# E15 · L'agent fait le sale boulot

**Point du programme** : agents IA, automatisation de tâches en autonomie ; atelier officiel « automatiser une tâche répétitive avec un agent IA ». Chronométré.

**Durée** : 20 minutes chronométrées. C'est le **premier exercice de la journée** : il vérifie aussi que votre poste marche (Git, Python, votre outil, Chrome).

## Ce qu'on fait

`exercices/15-agent-photos/depart/photos/` contient huit images de 1600 pixels de large. La page les attend à deux endroits (« Photo de la façade, à venir », « Photo de la terrasse, à venir ») et peut en montrer d'autres dans l'esprit du lieu. Tâche répétitive : trois tailles par image, les balises, les textes alternatifs.

Le point de départ est la page fournie dans `exercices/15-agent-photos/depart/`, la même pour tout le monde. L'exercice 17 fournit sa propre page : ce que vous produisez ici n'est pas repris plus loin.

Claude Code demande un abonnement payant. Sans abonnement, faites le même prompt dans le chat de GitHub Copilot Free (sélecteur sur **Agent**), ou suivez sur l'écran partagé de la formatrice. Mode de permissions **Manual** dans Claude Code : lisez chaque permission avant de l'accepter.

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
git add exercices/15-agent-photos
```

```
git commit -m "E15 : état avant les photos"
```

Résultat attendu : une ligne « files changed » ; « nothing to commit » est normal si rien n'a changé depuis le clonage.

### Étape 1 : lancer le chrono et envoyer un seul prompt

**Lancez un chrono** (téléphone ou montre), puis donnez un seul prompt à Claude Code. Il crée l'environnement virtuel `.venv` à la **racine** du dépôt, là où VS Code le retrouve tout seul :

```
Dans exercices/15-agent-photos/depart/photos/, huit images. Écris exercices/15-agent-photos/depart/redimensionner.py qui produit pour chacune trois largeurs (480, 960, 1600) dans exercices/15-agent-photos/depart/photos/petit, exercices/15-agent-photos/depart/photos/moyen et exercices/15-agent-photos/depart/photos/grand, en JPEG qualité 85, puis lance-le. Ensuite remplace les deux blocs « photo à venir » de exercices/15-agent-photos/depart/index.html par des images responsives (srcset et sizes) avec un texte alternatif qui décrit l'image, et ajoute une galerie de quatre photos dans la section « L'esprit du lieu ». Propose ensuite un message de commit. Si tu as besoin d'une bibliothèque, crée un environnement virtuel .venv à la racine du dépôt (pas dans depart/) et installe-la dedans, avec un requirements.txt à côté de redimensionner.py.
```

### Étape 2 : regarder l'agent travailler

Il va créer `.venv`, installer Pillow, écrire le script, le lancer, modifier la page. Chaque permission demandée se lit avant d'être accordée : c'est le moment où une installation se décide, par vous.

Si la permission d'installer est refusée, ou si l'agent n'y arrive pas, créez l'environnement vous-même, depuis la racine, puis redonnez le prompt.

Sous **Windows (PowerShell)** :

```
python -m venv .venv
```

```
.venv\Scripts\Activate.ps1
```

Résultat attendu : aucun message pour la première ; pour la seconde, l'invite du terminal commence par `(.venv)`. Si PowerShell répond que l'exécution de scripts est désactivée, ne changez pas ce réglage : demandez à la formatrice, ou passez par le chemin direct `.venv\Scripts\python.exe -m pip install pillow`. Si l'activation est bloquée, le `python -m pip freeze` de l'étape suivante utiliserait le Python global : prenez alors la variante en chemin direct, donnée plus bas.

Sous **Ubuntu** :

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

Résultat attendu : aucun message pour la première ; l'invite commence par `(.venv)` après la seconde. Si la première répond « ensurepip is not available », le paquet `python3-venv` manque : c'est une installation sur le poste, ne la faites pas sans l'accord de la formatrice (sur un poste d'entreprise, c'est souvent interdit). Rien n'a été créé, vous pouvez continuer sur l'écran partagé.

Dans les deux cas, ensuite :

```
python -m pip install pillow
```

```
python -m pip freeze > exercices/15-agent-photos/depart/requirements.txt
```

Résultat attendu : une ligne « Successfully installed pillow-... », puis un fichier `requirements.txt` qui contient une ligne `pillow==...`. (`python3` à la place de `python` sous Ubuntu si `python` n'existe pas ; dans un `.venv` activé, `python` existe toujours.)

**Si l'activation du `.venv` est bloquée** (Windows), utilisez le Python du `.venv` par son chemin, pour l'installation comme pour le gel des versions :

```
.venv\Scripts\python.exe -m pip install pillow
```

```
.venv\Scripts\python.exe -m pip freeze > exercices/15-agent-photos/depart/requirements.txt
```

Résultat attendu : les mêmes que ci-dessus, une ligne « Successfully installed pillow-... », puis un `requirements.txt` qui contient une ligne `pillow==...`. Sans cette variante, un `python -m pip freeze` lancé hors du `.venv` écrirait la liste du Python global, bien plus longue.

### Étape 3 : vérifier dans Chrome

Dans un **deuxième terminal** (bouton **+** du panneau Terminal) :

```
cd exercices/15-agent-photos/depart
```

```
pwd
```

```
python servir.py
```

Résultat attendu : `pwd` affiche un chemin qui se termine par `exercices/15-agent-photos/depart`, puis le serveur affiche une adresse et reste en attente (`Ctrl+C` l'arrête). Ouvrez http://127.0.0.1:8000/. Les images s'affichent. Réduisez d'abord la largeur de la fenêtre, puis F12, onglet Réseau, cochez « Disable cache » et rechargez la page : la variante chargée (480, 960 ou 1600 pixels) dépend de la largeur. Sur un écran à haute densité, Chrome choisit souvent la plus grande : c'est normal. « Ce site est inaccessible » : le serveur n'est pas lancé ; un 404 ou un 500 dans la console : le serveur tourne et l'adresse ou le code est faux.

### Étape 4 : lire les textes alternatifs

`AGENTS.md`, à la racine du dépôt, les exige : vérifiez qu'ils décrivent vraiment ce qu'on voit sur la photo, pas le nom du fichier.

### Étape 5 : vérifier que `.venv` n'est pas suivi par Git

Depuis la racine, dans le premier terminal :

```
git status
```

Résultat attendu : `.venv` n'apparaît pas, il est ignoré par git. Les fichiers listés sont `redimensionner.py`, `requirements.txt`, `index.html`, `style.css`, et les trois dossiers de photos.

### Étape 6 : arrêter le chrono et enregistrer

**Arrêtez le chrono et notez le temps.** Relisez le message de commit proposé : s'il cite un fichier qui n'existe pas (par exemple `requirements.txt` si l'installation a été refusée), corrigez-le. Puis, depuis la racine :

```
git add exercices/15-agent-photos
```

```
git commit -m "Photos : trois tailles par image, galerie et images responsives"
```

Remplacez le message par celui de l'agent, relu et corrigé, s'il est meilleur. Résultat attendu : une ligne « N files changed » (le nombre de fichiers touchés) et la liste des fichiers créés. `git show --stat` affiche la liste complète, y compris `redimensionner.py`, `requirements.txt` et `index.html`. Un commit se défait : rien n'est perdu.

## Livrable

`redimensionner.py`, `requirements.txt` (dans `exercices/15-agent-photos/depart/`), 24 images dans `photos/petit`, `photos/moyen` et `photos/grand`, la page avec ses photos, un commit, le temps du chrono. Le `.venv` est à la racine du dépôt.

## Ce qu'on retient

- L'agent a enchaîné six gestes qu'on aurait faits à la main en une heure. Le chrono le dit.
- Il a eu besoin d'installer quelque chose : c'est le moment où on lit avant d'accepter. Sur le poste d'une entreprise, c'est souvent interdit, et il faut le savoir avant.
- Le texte alternatif est exigé par `AGENTS.md` : l'outil l'a écrit. Reste à vérifier qu'il décrit vraiment la photo. Une règle écrite vaut mieux qu'une correction après coup, et elle ne dispense pas de relire.
- Cet exercice a aussi servi à vérifier votre poste : si quelque chose a coincé, c'est le bon moment pour le dire.
