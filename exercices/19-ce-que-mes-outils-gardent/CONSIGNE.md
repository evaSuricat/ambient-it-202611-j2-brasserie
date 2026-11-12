# E19 · Ce que mes outils gardent de moi

**Point du programme** : fuite de données et conservation. Qu'est-ce qu'un outil d'IA garde de ce que vous lui avez écrit, combien de temps, et qui peut le revoir ?

**Durée** : 15 minutes.

## Ce qu'on fait

Chacun ouvre les réglages de son compte Claude et remplit `exercices/19-ce-que-mes-outils-gardent/depart/fiche-outils.md`. **Un seul outil pendant les 15 minutes : Claude** (claude.ai, ou Claude Code). Sans compte Claude, prenez la colonne GitHub Copilot. Les autres colonnes du tableau B sont pour chez vous, après la formation : le tableau de comparaison reste complet pour ça. Le travail est un relevé, sur votre écran, de ce qui existe réellement aujourd'hui, sans écrire de code. La consigne ne vous dit pas où cliquer parce que les menus changent. Elle vous dit quoi chercher.

**Rien de personnel à l'écran.** Si vous partagez votre écran, ouvrez les réglages, jamais la liste de vos conversations : fermez le panneau d'historique avant. La formatrice fait de même sur le sien. **On regarde sans rien changer**, sauf un choix personnel que vous notez dans la dernière ligne du tableau B.

Cet exercice se fait sans abonnement payant : un compte gratuit Claude suffit, et sans compte Claude la colonne GitHub Copilot fait le même travail. La colonne « sans compte » est pour qui n'a ni l'un ni l'autre : la formatrice la remplit sur son écran partagé.

### Étape 0 : enregistrer le point de départ

Depuis la racine de `stagiaire_J2` :

```
git add exercices/19-ce-que-mes-outils-gardent
```

```
git commit -m "E19 : état avant la fiche"
```

Résultat attendu : « nothing to commit » est normal si rien n'a changé depuis le clonage.

### Étape 1 : lire le tableau A

Ouvrez `exercices/19-ce-que-mes-outils-gardent/depart/fiche-outils.md`. Le tableau A donne les durées annoncées par Anthropic, GitHub et OpenAI, avec la date de chaque page. Repérez deux phrases à retenir : celle qui dit qu'un pouce peut servir à l'entraînement même après refus (OpenAI), et celle qui dit que la durée pour le compte individuel GitHub n'a pas été trouvée. Une durée absente de la documentation ne veut pas dire « zéro ». Retenez aussi ceci pour les deux colonnes ajoutées : la ZDR (zéro conservation de données) est une clause du fournisseur, celui qui fait tourner le modèle, jamais une option du harnais, l'outil dans VS Code. Changer d'outil dans VS Code ne change donc pas ce que le fournisseur garde ; seul le contrat ou l'accord avec le fournisseur le change.

### Étape 2 : chercher les réglages, outil par outil

Pour votre outil (Claude, ou Copilot sans compte Claude), dans cet ordre de recherche :

1. Les **réglages du compte**, puis une rubrique qui parle de confidentialité, de données ou d'entraînement.
2. L'endroit où se **voit et s'efface la mémoire** de l'outil, s'il en a une.
3. L'**export** de vos données. Ne le demandez pas pendant l'exercice, sauf choix personnel : un export est un fichier qui contient toutes vos conversations, donc des données personnelles à ranger **hors du dépôt Git**, jamais dans `stagiaire_J2`.
4. Les **partages** : liens de conversation, artefacts ou pages publiés. Listez-les, sans les ouvrir si vous craignez qu'ils contiennent quelque chose de personnel.

Pour Claude, cherchez dans le menu de votre profil (en bas ou en haut à gauche selon l'interface), puis « Paramètres » ou « Settings » : l'intitulé exact change. Pour GitHub Copilot, les réglages se trouvent sur votre compte GitHub, rubrique Copilot : l'intitulé exact change aussi. ChatGPT, chez vous, suit le même chemin que Claude. **Écrivez le chemin que vous avez vraiment suivi.** Si un réglage n'existe pas, écrivez « absent » : c'est une réponse valable.

Pour Claude Code, la page `https://code.claude.com/docs/en/data-usage` dit ce qui est conservé côté éditeur et en local. Les transcriptions locales sont lisibles en clair sur votre poste (tableau A).

### Étape 3 : remplir le tableau B

Une case par question, dans la colonne de votre outil (Claude, ou Copilot). Pour la ligne « combien de temps garde-t-on une conversation supprimée », reprenez la valeur du tableau A et notez-la avec la date de la source. Pour la dernière ligne, décidez : laisser tel quel, changer un réglage (vous le faites alors vraiment, et vous le notez), ou changer ce que vous envoyez.

Résultat attendu : chaque case de votre colonne contient une valeur lue sur votre écran, ou « absent ». Une case que vous remplissez de mémoire plutôt que d'après l'écran est une case à refaire. Si un réglage vous surprend (par sa valeur par défaut, par son emplacement), notez-le aussi dans la partie D.

### Étape 4 : ce que je ne mets plus dans un prompt

Remplissez la partie C : trois types de contenu que vous décidez de ne plus envoyer. Pensez aux exercices 17 et 18 : des clients, un secret, une base entière.

### Étape 5 : enregistrer

Depuis la racine :

```
git add exercices/19-ce-que-mes-outils-gardent
```

```
git commit -m "E19 : fiche de ce que mes outils gardent"
```

Résultat attendu : une ligne « files changed » qui cite `fiche-outils.md`. Vérifiez avant de committer que la fiche ne contient aucune donnée personnelle (pas de nom de conversation, pas de courriel, pas de capture). Un commit se défait : `git reset --soft HEAD~1` annule le dernier sans perdre vos fichiers.

## Livrable

`fiche-outils.md` remplie : partie B pour un outil (la colonne Claude, ou Copilot sans compte Claude), parties C et D. Les autres colonnes de B se remplissent chez vous.

## Ce qu'on retient

- Ce que l'éditeur annonce (tableau A) et ce que votre écran montre (tableau B) ne coïncident pas toujours. Les deux comptent, mais seule la fiche B est à vous.
- Supprimer une conversation n'efface pas tout de suite : le tableau A donne les délais annoncés, pas une garantie.
- Un export, un pouce, un partage public sont des endroits où des données quittent la conversation. Un export est lui-même un fichier à protéger.
