# E23 · La fiche et la purge

**Point du programme** : RGPD, traçabilité, données, conservation, appliqués au Pigala.

**Durée** : 25 minutes.

## Ce qu'on fait

Deux livrables. Une **fiche de traitement** qui décrit ce que fait réellement votre projet avec les données des clients (pourquoi, lesquelles, qui y accède, combien de temps). Un script **`purger.py`** qui supprime les réservations passées, sans jamais agir à l'aveugle. Les deux se complètent : une durée de conservation qui n'est écrite que dans une fiche ne supprime rien.

Cette fiche est un exercice utile dans tous les cas. Elle ne dit pas si Le Pigala est tenu de tenir un registre au sens de l'article 30 du RGPD : le texte de l'article n'a pas été lu pour cet exercice (`SOURCES.md`). Ce n'est pas un avis juridique.

Sans abonnement Claude Code : mêmes prompts dans Copilot Free en mode **Agent** (« New Chat » repasse en Ask : remettez Agent), ou suivez sur l'écran partagé. Mode de permissions **Manual** : lisez chaque permission avant de l'accepter.

### Étape 0 : reprendre votre dossier de l'exercice 21

Depuis la racine de `stagiaire_J2`. Cette ligne copie votre dossier de l'exercice 21 (page, serveur, base séparée, tests) dans celui de l'exercice 23, sans écraser les fichiers propres à l'exercice 23. Si votre exercice 21 n'a pas abouti (tests au rouge, pas de dossier `donnees/`), ne la lancez pas : le dossier fourni est la solution.

```
python -c "import shutil; shutil.copytree('exercices/21-securiser-workflow/depart', 'exercices/23-fiche-et-purge/depart', dirs_exist_ok=True, ignore=shutil.ignore_patterns('SOURCES.md', '__pycache__', 'tri-revue.md', 'extrait-anonyme.md'))"
```

Résultat attendu : aucun message. Une erreur `FileNotFoundError` : le dossier de l'exercice 21 n'est pas là, rien n'a été écrit, gardez le dossier fourni. Puis :

```
git add exercices/23-fiche-et-purge
```

```
git commit -m "E23 : état avant la fiche et la purge"
```

Résultat attendu : une ligne « files changed ». « nothing to commit » est normal si rien n'a changé (dossier fourni gardé).

### Étape 1 : les tests de la purge, au rouge

```
cd exercices/23-fiche-et-purge/depart
```

```
python -m unittest test_purge -v
```

Résultat attendu : `Ran 4 tests`, puis `FAILED (failures=4)` : `purger.py` n'existe pas encore. Les tests travaillent sur une copie temporaire de la base : la vôtre n'est jamais modifiée. Si `python` n'existe pas, tapez `python3`. `can't open file` ou `ModuleNotFoundError` : vous n'êtes pas dans le bon dossier (`pwd` doit finir par `exercices/23-fiche-et-purge/depart`).

### Étape 2 : remplir la fiche à partir du code

Copiez le modèle, depuis la racine, puis ouvrez la copie :

```
cp exercices/23-fiche-et-purge/depart/fiche-modele.md exercices/23-fiche-et-purge/depart/fiche-traitement.md
```

Remplissez les sections 1 à 4 et 6 **en lisant le code**, pas de mémoire : `index.html` (que demande le formulaire, et sont-ils tous nécessaires ?), `servir.py` (qui reçoit, qui écrit où), `gerant.py` (qui lit), `donnees/` (où vit la base). Le champ « commentaire » est un texte libre : l'exercice 21 y a montré une allergie, un nom de tiers, un numéro de téléphone. Écrivez ce qu'il peut contenir. Écrivez « à décider » quand vous ne savez pas.

### Étape 3 : la durée de conservation

Demandez d'abord à votre outil, dans Claude Code ou Copilot en mode Agent :

```
Quelle est la durée légale de conservation des réservations d'un restaurant ? Cite tes sources.
```

Notez l'outil et le modèle, le chiffre donné s'il y en a un, et si une source est citée, laquelle. Puis ouvrez la page de la CNIL sur les durées de conservation : `https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees` (page du 02/04/2026). Elle distingue trois temps (base active, archivage intermédiaire, archivage définitif) et ne fournit pas un chiffre unique pour tous les cas : la durée se fixe et se justifie selon la finalité. Un chiffre « légal » donné sans source par un outil est une affirmation à vérifier, pas un fait. Fixez **votre** durée dans la section 5 de la fiche, avec sa justification (à quoi servent les données une fois la date de réservation passée ?). Résultat attendu : un nombre de jours et une phrase de justification. Les données de ce projet sont fictives ; le raisonnement est le vrai.

### Étape 4 : écrire la purge

```
Dans exercices/23-fiche-et-purge/depart/, lis AGENTS.md à la racine du dépôt et test_purge.py. N'ouvre pas le dossier donnees/ ni son contenu. Voici ce qu'il te faut de la base : le fichier donnees/reservations.db, une base SQLite avec une table reservations aux colonnes id (entier, clé primaire), nom, telephone, email, date (texte AAAA-MM-JJ), couverts (entier), commentaire et cree_le (texte). Écris purger.py : il supprime de la table reservations de donnees/reservations.db les réservations dont la date est antérieure à (aujourd'hui moins N jours). Options : --conserver-jours N (obligatoire : sans elle le script refuse de tourner), --base chemin (base à purger, par défaut donnees/reservations.db), --aujourdhui AAAA-MM-JJ (pour les tests), --appliquer. Sans --appliquer, le script ne supprime rien : il affiche combien de réservations seraient supprimées. Avec --appliquer, il supprime et journalise la purge dans un fichier purge.log placé dans le même dossier que la base. Ne lance pas le script sur la vraie base.
```

Le prompt donne lui-même le schéma de la table : la base contient des données personnelles, et la règle d'`AGENTS.md` posée à l'exercice 21 (« n'envoie jamais à un modèle une donnée de donnees/ ») comme la règle de refus de lecture `Read(**/donnees/**)` demandent que l'outil n'ait pas à l'ouvrir. En mode Manual, lisez chaque permission : si l'outil demande à lire `donnees/`, refusez.

### Étape 5 : relire avant de lancer

Vérifiez dans `purger.py` : la suppression a-t-elle un `WHERE` ? Le script refuse-t-il vraiment de tourner sans `--conserver-jours` ? Que contient une ligne de `purge.log` ? L'outil a-t-il essayé de lire `donnees/` malgré la consigne ? **Un journal qui recopie des noms ou des téléphones est lui-même un fichier de données personnelles**, sans fiche et sans durée. Puis les tests :

```
python -m unittest test_purge -v
```

Résultat attendu : `OK`, quatre tests. Si le test du journal échoue, c'est que le journal recopie des données personnelles : corrigez avec l'outil, relisez.

### Étape 6 : essayer sur une copie, jamais sur la vraie base

```
python -c "import shutil; shutil.copy('donnees/reservations.db', 'donnees/copie.db')"
```

```
python purger.py --conserver-jours 7 --aujourdhui 2026-12-01 --base donnees/copie.db
```

Résultat attendu : un message de simulation qui annonce 10 réservations (celles antérieures au 24/11/2026), sans rien supprimer. La formulation exacte dépend de votre script. Puis la vraie suppression, sur la copie :

```
python purger.py --conserver-jours 7 --aujourdhui 2026-12-01 --base donnees/copie.db --appliquer
```

Résultat attendu : un message qui annonce 10 réservations supprimées, et une ligne dans `donnees/purge.log`. Lisez cette ligne. Relancez la commande de simulation : elle annonce maintenant 0. Supprimez la copie et le journal d'essai pour ne pas les committer :

```
rm donnees/copie.db
```

```
rm donnees/purge.log
```

### Étape 7 : finir la fiche et enregistrer

Complétez les sections 5 (durée), 7 (suppression à la demande d'une personne, incident) et 8 (ce qui reste à décider). Dans la section 5, ajoutez la commande exacte qui applique votre durée. Puis, depuis la racine :

```
cd ../../..
```

```
git add exercices/23-fiche-et-purge
```

```
git commit -m "E23 : fiche de traitement et purge des réservations"
```

Résultat attendu : une ligne « files changed » qui cite `fiche-traitement.md`, `purger.py` et `test_purge.py`.

## Livrable

`fiche-traitement.md`, `purger.py` avec ses quatre tests au vert, un ou deux commits : avant, quand quelque chose a changé, et après.

## Ce qu'on retient

- Une durée de conservation se décide et se justifie ; un outil qui en annonce une « légale » sans source est à vérifier.
- Une purge sans `WHERE` vide la table. Elle se simule d'abord, et se teste sur une copie.
- Un journal qui recopie des noms recrée le problème qu'il devait résoudre.
- La fiche décrit le code : s'ils divergent, l'un des deux est faux.
