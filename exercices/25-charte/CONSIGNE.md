# E25 · Une charte qui se vérifie

**Point du programme** : atelier officiel « charte d'usage de l'IA » ; cadre, suivi des usages, normes.

**Durée** : 45 minutes.

## Ce qu'on fait

Vous écrivez une charte d'usage de l'IA pour votre équipe : **une page, dix règles au plus**, et pour chaque règle trois choses : **qui** la tient, **comment on la contrôle**, **quelle preuve** on garde. Une règle sans contrôle (« être prudent ») va dans la section des vœux. Puis vous **testez une règle** pour de bon : vous essayez de la violer et vous notez ce qui se passe. Les deux ou trois premières minutes servent à lire les repères, pas à tout lire.

Sans abonnement Claude Code : le chat de Copilot Free fait l'étape 2, et l'étape 4 se fait avec un test écrit à la main (exemple 3 de `regles-testees-exemples.md`) ou se suit sur l'écran partagé. Sans aucune IA, `charte-exemple-ia.md` remplace la réponse de l'étape 2.

### Étape 0 : enregistrer le point de départ

Depuis la racine de `stagiaire_J2` :

```
git add exercices/25-charte
```

```
git commit -m "E25 : état avant la charte"
```

Résultat attendu : « nothing to commit » est normal si rien n'a changé depuis le clonage.

### Étape 1 : lire les repères (5 min)

Ouvrez `exercices/25-charte/depart/modele-charte.md`, `tableau-normes.md` et `regles-testees-exemples.md`. Dans `tableau-normes.md`, relevez ce qui est dit des normes ISO : seul leur résumé public a été lu, leur texte est payant. Une charte qui écrit « conforme à l'ISO/IEC 23894 » sans avoir lu la norme dit plus que ce qu'on sait. Rouvrez aussi votre fiche de l'exercice 19 (`exercices/19-ce-que-mes-outils-gardent/depart/fiche-outils.md`) : ses parties B et C donnent des faits pour vos règles (ce que les outils gardent, ce que vous n'envoyez plus).

### Étape 2 : demander une charte à l'IA, puis la trier (10 min)

Dans Claude Code, ou dans le chat de Copilot en mode **Ask** :

```
Écris une charte d'usage de l'IA en dix règles pour une équipe de développement de cinq personnes qui utilise des assistants de code. Pour chaque règle : qui la tient, comment on la contrôle, quelle preuve on garde. Ne cite aucune norme ni aucun article de loi.
```

Notez l'outil et le modèle. Puis **ne recopiez rien tel quel**. Pour chaque règle, une question : peut-on prouver, demain, qu'elle a été tenue ou violée ? Marquez chaque règle : vérifiable, à reformuler, ou vœu. Si vous n'avez pas d'IA, appliquez le même tri aux dix règles de `charte-exemple-ia.md` : lesquelles se vérifient ? (Indice : la règle 7, « signaler tout incident dans les meilleurs délais », se vérifie quand on sait à qui, par quel moyen et en combien de temps. Comparez avec l'article 33 du RGPD cité dans `tableau-normes.md`, qui prévoit une notification à l'autorité de contrôle « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance ».)

### Étape 3 : écrire votre charte (15 min)

Dans `exercices/25-charte/depart/modele-charte.md`, remplissez le tableau : dix règles au plus, chacune avec **qui**, **contrôle**, **preuve**. Vos règles viennent de votre journée : les failles de l'exercice 21, la fiche de l'exercice 19, la grille de l'exercice 24, la décision de l'exercice 22.

Deux exemples de règles qui se vérifient, avec leur preuve (les vôtres seront différentes) :

- Chaque merge request passe l'analyse SonarQube avant revue humaine (preuve : le rapport Sonar lié à la MR).
- Le code classé confidentiel n'est envoyé qu'à un fournisseur choisi par l'équipe : serveur interne, cloud de l'entreprise en région européenne avec conservation à zéro, ou fournisseur payant en ZDR vérifié (preuve : la configuration du harnais, fournisseur et région, relue à chaque mise à jour).

Remplissez la partie « Comment nous suivons les usages » avec un outil de la partie B de `tableau-normes.md` que quelqu'un lit vraiment, ou écrivez « à décider » : la commande `/usage` de Claude Code et les jauges de Copilot n'ont pas été vérifiées à l'écran pour cette formation, ne les citez qu'après les avoir vues.

Renommez le fichier quand vous avez fini, depuis la racine :

```
cp exercices/25-charte/depart/modele-charte.md exercices/25-charte/depart/charte-ia.md
```

(Faites la copie avant de remplir si vous préférez travailler directement dans `charte-ia.md`.) Résultat attendu : un fichier `charte-ia.md` d'une page, dix lignes au plus dans le tableau.

### Étape 4 : tester une règle (10 min)

Choisissez **une** règle de votre tableau et prouvez-la, comme à l'exercice 21 :

- Si la règle peut s'écrire dans `AGENTS.md`, écrivez-la, ouvrez une session neuve, demandez à l'outil de faire exactement ce que la règle interdit, et notez : outil, modèle, ce qu'il a fait. Un résultat peut changer d'un outil à l'autre.
- Si la règle peut devenir une règle de refus de lecture, écrivez-la dans `.claude/settings.json`, essayez de la violer, cherchez le contournement et notez les deux.
- Si la règle peut devenir un test, écrivez-le (ou demandez-le à l'outil) et lancez-le, rouge puis vert.

Remplissez la section « La règle que j'ai testée » de `charte-ia.md`, et la colonne « Testée ? » de cette ligne. Résultat attendu : une preuve écrite, avec un résultat réel de votre poste. Si la règle a résisté, dites jusqu'où ; si elle a cédé, dites comment la renforcer.

### Étape 5 : se préparer à présenter (5 min)

Pour la mise en commun, deux minutes par groupe : vos trois règles les plus solides et la règle que vous avez testée avec son résultat.

### Étape 6 : enregistrer

Depuis la racine :

```
git add exercices/25-charte AGENTS.md .claude
```

```
git commit -m "E25 : charte d'usage de l'IA et une règle testée"
```

Résultat attendu : une ligne « files changed » qui cite `charte-ia.md`. Si `AGENTS.md` ou `.claude` n'ont pas changé, `git add` ne dit rien.

## Livrable

`exercices/25-charte/depart/charte-ia.md` : une page, dix règles au plus avec qui, contrôle, preuve ; la règle testée avec son résultat réel ; les vœux ; le suivi des usages.

## Ce qu'on retient

- Une règle sans contrôle est un vœu. La preuve distingue une charte d'une affiche.
- Une charte écrite par l'IA et recopiée sans tri est une liste de vœux bien rédigée.
- Une règle en `AGENTS.md` ou en refus de lecture se teste, et on cherche sa limite.
- Une norme dont on n'a lu que le résumé se cite comme telle.
