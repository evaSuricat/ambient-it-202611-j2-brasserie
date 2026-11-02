# E22 · À qui est ce code ?

**Point du programme** : propriété du code, droits, licences, auditabilité.

**Durée** : 15 minutes.

## Ce qu'on fait

Trois cas du Pigala, sur une page : ce que l'équipe décide, la trace de la décision, ce qui reste ouvert. **Ceci n'est pas un avis juridique**, et la consigne ne vous demande pas de conclure sur le droit d'auteur : les sources lues pour cet exercice (voir `exercices/22-a-qui-est-ce-code/depart/SOURCES.md`) ne le tranchent pas. Vous apprenez à écrire une décision d'équipe qui s'appuie sur ce qu'on sait, et à nommer ce qu'on ne sait pas.

Cet exercice se fait sans IA et sans abonnement. L'étape 5 propose, si vous voulez, de relire votre texte avec votre outil.

### Étape 0 : enregistrer le point de départ

Depuis la racine de `stagiaire_J2` :

```
git add exercices/22-a-qui-est-ce-code
```

```
git commit -m "E22 : état avant les décisions"
```

Résultat attendu : « nothing to commit » est normal si rien n'a changé depuis le clonage.

### Étape 1 : lire les trois cas

Ouvrez `exercices/22-a-qui-est-ce-code/depart/cas.md` et `exercices/22-a-qui-est-ce-code/depart/extrait-licence.js`. Cinq minutes de lecture, pas plus. Dans l'extrait, trouvez l'en-tête de licence : auteur, année, licence.

### Étape 2 : le cas A, l'extrait de code avec licence

Dans `exercices/22-a-qui-est-ce-code/depart/decisions-code.md`, écrivez ce que vous faites des dix lignes de code (seize avec l'en-tête de licence). Trois options existent : les retirer et les réécrire sans les avoir sous les yeux, les garder en respectant la licence annoncée (ce qui a des conséquences sur le reste du code), les remplacer par une bibliothèque standard. Choisissez, et écrivez **ce que vous ne savez pas** : l'en-tête est-il authentique ? Le code vient-il vraiment de cet auteur ? Qui peut le vérifier ?

Regardez ensuite le réglage de votre compte GitHub, si vous en avez un : dans les réglages Copilot, cherchez une rubrique qui parle de suggestions qui correspondent à du code public. L'intitulé exact change (libellé non vérifié à l'écran au moment d'écrire cette consigne). Notez la valeur que vous voyez, ou « absent ». **Ne changez rien** sauf choix personnel. La documentation GitHub (page « Code suggestions », lue le 02/11/2026) dit : pour les suggestions en ligne, seules celles acceptées sans modification sont comparées à l'index de code public ; dans le chat, une référence peut s'afficher sous la réponse si le réglage l'autorise ; les journaux de session d'agent portent un lien vers le code correspondant ; les correspondances sont rares (moins d'un pour cent des suggestions en ligne). Notez ce que la page dit du chat et des agents, et ce qu'elle ne dit pas.

### Étape 3 : le cas C, l'historique de votre dépôt

Depuis la racine :

```
git log -n 8 --format="%h | %an | %ad | %s" --date=short
```

Résultat attendu : jusqu'à huit lignes, avec le numéro court de chaque commit, l'auteur (vous), la date et le message. Si une ligne vous demande d'appuyer sur `q`, tapez `q`. Si l'historique est trop court, lisez `journal-exemple.txt`. Regardez ensuite le texte complet d'un de vos commits :

```
git log -n 1 --format=%B
```

Résultat attendu : le message complet du dernier commit. Certains outils ajoutent une ligne du type « Co-Authored-By » : cherchez-en une dans vos messages, et notez si elle y est ou non. Que permet de répondre cet historique à la question « quelle part vient d'une IA, de quel outil, relue par qui » ?

### Étape 4 : le cas B, la réponse au gérant

Dans `decisions-code.md`, écrivez la réponse au gérant : quelques lignes, vouvoiement, deux affirmations au plus, chacune appuyée par une source citée. Écrivez aussi ce que la réponse ne dit pas, volontairement. Piège : la phrase d'Anthropic contient « (if any) » : l'éditeur cède les droits qu'il a, **s'il en a**. Cela ne dit pas si le code est protégé, ni qui est auteur au sens du droit. Une phrase qui commencerait par « Vous êtes propriétaire de ce code » dirait plus que les sources.

### Étape 5 (facultative) : relire avec votre outil

```
Lis exercices/22-a-qui-est-ce-code/depart/decisions-code.md. Pour chaque affirmation, dis si elle est appuyée par les sources citées dans exercices/22-a-qui-est-ce-code/depart/SOURCES.md, ou si elle va plus loin. Ne cite aucune autre source et n'invente aucune règle de droit.
```

Notez l'outil et le modèle. Si l'outil cite une règle de droit ou un article qui n'est pas dans `SOURCES.md`, c'est une affirmation à vérifier à la source, pas un fait.

### Étape 6 : enregistrer

```
git add exercices/22-a-qui-est-ce-code
```

```
git commit -m "E22 : décisions sur le code produit avec une IA"
```

Résultat attendu : une ligne « files changed » qui cite `decisions-code.md`.

## Livrable

`decisions-code.md` rempli, un ou deux commits : avant, quand quelque chose a changé, et après.

## Ce qu'on retient

- On ne conclut pas ce que les sources ne disent pas. « Ouvert » est une réponse d'équipe valable, si elle est écrite avec le nom de qui la lèvera.
- Une licence annoncée dans un extrait de code engage au moment où vous le gardez.
- L'historique git dit qui a committé, pas qui a écrit. Pour l'audit, la trace se décide avant : un message de commit, une étiquette, une relecture notée.
