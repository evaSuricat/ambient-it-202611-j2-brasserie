# Bonus · Écrire son propre sous-agent

**Point du programme** : bonus pour ceux qui ont fini avant les autres. Transformer une règle de votre charte (exercice 25) en un sous-agent qui la vérifie, lancé sur le dépôt, puis trié.

**Durée** : 20 à 30 minutes. Le bonus se fait seul ou à deux, après l'exercice 21 (le sous-agent `relecteur-code`) et de préférence après l'exercice 25. Rien n'y est obligatoire pour la suite.

## Ce qu'on fait

À l'exercice 21, vous avez utilisé `relecteur-code` : un fichier Markdown avec un en-tête (nom, description, outils autorisés, modèle) et un texte de consignes. Ici, vous écrivez le vôtre dans `.claude/agents/`, à la racine de `stagiaire_J2`, à partir de ce modèle, pour **une autre règle de votre charte**.

Exemple fil rouge : un sous-agent `verificateur-rgpd` qui vérifie qu'aucun fichier ne contient de téléphone ou de courriel en clair, en lecture seule. Vous pouvez le prendre tel quel ou choisir une autre règle (secrets dans un fichier, texte alternatif manquant sur une image, route qui lit des données).

Toutes les données du dépôt sont fictives : le sous-agent y trouvera donc des téléphones et des courriels (des `@example.com`), et c'est voulu. Le travail consiste à trier ce qu'il dit. Sans abonnement Claude Code : suivez sur l'écran partagé de la formatrice, ou voyez l'équivalent Copilot à l'étape 5.

### Étape 1 : lire le modèle et l'exemple

Ouvrez `exercices/bonus-sous-agent/depart/modele-sous-agent.md` et `.claude/agents/relecteur-code.md`. Repérez les quatre lignes de l'en-tête et la ligne `tools`. Un sous-agent en lecture seule ne reçoit que `Read, Grep, Glob` : sans `Edit` ni `Bash`, il ne peut ni écrire ni lancer de commande.

### Étape 2 : écrire le sous-agent

Depuis la racine, copiez le modèle à sa place :

```
python -c "import shutil; shutil.copy('exercices/bonus-sous-agent/depart/modele-sous-agent.md', '.claude/agents/verificateur-rgpd.md')"
```

Résultat attendu : aucun message, et le fichier `.claude/agents/verificateur-rgpd.md` existe. Une erreur `FileNotFoundError` : vous n'êtes pas à la racine (`pwd`) ou le dossier `.claude/agents/` manque. Si `python` n'existe pas, tapez `python3`. Choisissez un autre nom de fichier si vous avez une autre règle.

Ouvrez le fichier et complétez tout ce qui est entre `<à compléter ...>` : le `name` (le même que le nom du fichier, sans `.md`), la `description` (une phrase qui dit quand l'utiliser), le rôle, et ce qu'il faut chercher. Gardez `tools: Read, Grep, Glob`. Aucun tiret long, comme dans le reste du dépôt.

### Étape 3 : le lancer sur le dépôt

Dans Claude Code (ouvrez ou rouvrez la session si le fichier est le premier du dossier `.claude/agents/` : Claude Code le découvre au démarrage), envoyez, en remplaçant le nom par le vôtre :

```
Utilise le sous-agent verificateur-rgpd sur le dossier ressources/.
```

Résultat attendu : la réponse montre qu'un sous-agent a tourné, puis liste des fichiers avec gravité et correction, par exemple `ressources/reservations.csv` qui contient des courriels et des téléphones. La formulation exacte change d'une exécution à l'autre. S'il répond que le sous-agent n'existe pas : le fichier n'est pas dans `.claude/agents/` à la racine, ou la session est plus ancienne que le fichier : fermez-la et rouvrez-la.

### Étape 4 : trier sa sortie

Dans un nouveau fichier `exercices/bonus-sous-agent/depart/tri-sous-agent.md`, notez l'outil et le modèle, puis pour chacun de ses trois premiers points : **juste** (un vrai défaut), **faux** (il se trompe ou invente), **à ignorer** (vrai, mais voulu : ici, des données fictives de test). Une ligne pour dire ce qu'il a **raté**. Il propose, vous décidez.

### Étape 5 : l'équivalent Copilot, si disponible

GitHub Copilot propose des agents personnalisés dans `.github/agents/<nom>.agent.md`. **L'offre nécessaire (Free, Pro ou autre) est à vérifier** : la consigne ne l'a pas vérifiée à l'écran. Si votre compte le permet, créez `.github/agents/verificateur-rgpd.agent.md` avec le même texte de consignes, lancez-le sur `ressources/` et comparez la sortie avec celle de Claude Code. Sinon, écrivez « indisponible sur mon offre » dans votre tri.

### Étape 6 : enregistrer

Depuis la racine :

```
git add .claude exercices/bonus-sous-agent
```

```
git commit -m "Bonus : un sous-agent écrit à partir de relecteur-code"
```

Résultat attendu : une ligne « files changed » qui cite `.claude/agents/verificateur-rgpd.md` et `tri-sous-agent.md`. Un commit se défait : rien n'est perdu.

## Livrable

Un sous-agent dans `.claude/agents/`, sa sortie triée dans `tri-sous-agent.md`, un commit.

## Ce qu'on retient

- Une règle de charte se transforme en fichier : un sous-agent ne coûte qu'un en-tête et quelques lignes de consignes.
- Les outils listés sont la vraie limite : un sous-agent sans `Edit` ni `Bash` ne peut ni modifier ni exécuter. La phrase « tu ne modifies rien » seule n'est qu'une consigne.
- Sa sortie est une donnée de plus à trier : il peut voir juste, se tromper, ou signaler du voulu.
