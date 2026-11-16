# E22 · À qui est ce code ?

**Point du programme** : propriété du code, droits, licences, auditabilité.

**Durée** : 20 minutes, de 13 h 10 à 13 h 30 (à la reprise, après le déjeuner) : 15 minutes de discussion, puis 5 minutes pour un geste final.

## Ce qu'on fait

Cet exercice se fait en slides et en discussion (15 minutes, à 13 h 10) : on lit, on discute, on décide ensemble. Il se termine par un geste de 5 minutes, décrit plus bas, qui laisse un commit.

Les énoncés des trois cas sont dans `exercices/22-a-qui-est-ce-code/depart/cas.md`. Pour chaque cas, un fichier à ouvrir dans le même dossier `depart/` :

| Cas | La question | Le fichier à ouvrir |
|---|---|---|
| A | L'assistant propose du code qui porte en haut le nom d'un auteur et une licence. Qu'en fait-on ? | `extrait-licence.js` : seize lignes, six d'en-tête puis dix de code |
| B | Le client demande : « ce code est à moi ? » | `SOURCES.md` : ce que disent les textes lus (contrats du fournisseur, droit français, documentation GitHub) |
| C | Un audit demande quelles parties ont été écrites avec une IA, et qui les a relues | `journal-exemple.txt` : un historique Git fictif |

Une licence, ce sont les conditions auxquelles quelqu'un autorise la réutilisation de son code.

**Ceci n'est pas un avis juridique.** Les sources lues pour cet exercice sont dans `exercices/22-a-qui-est-ce-code/depart/SOURCES.md`.

## Le geste final : la trace, on l'écrit et on la teste (5 minutes)

**Le but.** Dans trois mois, un audit demandera quelles parties du code ont été écrites avec une IA, et qui les a relues. Aujourd'hui, l'historique Git ne le dit pas : il ne garde que le nom de la personne qui a enregistré. On ajoute une règle au projet, puis on vérifie que l'assistant la suit.

**1. Écrire la règle.** Dans VS Code, ouvrez `AGENTS.md`, le fichier tout en haut du dossier (pas dans `exercices`). Allez à la fin (`Ctrl+Fin`), ajoutez une ligne vide, collez ce bloc, puis enregistrez (`Ctrl+S`) :

```
## Trace de l'IA dans les commits

- Quand une modification a été écrite ou modifiée avec ton aide, termine le message du commit par ces trois lignes :
  Outil : le nom de l'outil
  Modèle : le nom du modèle
  Relu par : le prénom de la personne
- Ne remplis jamais « Relu par » toi-même : demande son prénom à la personne, et ne l'écris que si elle confirme avoir relu.
```

Un commit, c'est un enregistrement de vos modifications dans l'historique Git, avec un message qui dit ce qui a changé.

**2. Demander à l'assistant d'enregistrer.** Ouvrez une **nouvelle conversation** (l'assistant relit `AGENTS.md` au début d'une conversation) et collez ce prompt :

```
Enregistre dans Git la modification d'AGENTS.md, en suivant les règles du projet.
```

Résultat attendu : l'assistant vous demande si vous avez relu et quel prénom écrire. Répondez avec votre prénom (par exemple « Eva, j'ai relu »), même s'il propose « écrit sans l'IA » : on veut voir les trois lignes. Il propose alors un message de commit qui se termine par « Outil », « Modèle » et « Relu par », et demande la permission de lancer `git add` et `git commit`. Répondez **Yes**, pas « Yes, allow… for this project », qui donnerait une permission durable.

**3. Vérifier soi-même.** Dans le terminal de VS Code, à la racine du dépôt :

```
git log -1
```

Cette commande affiche le dernier commit. Résultat attendu : une ligne `Author:` à votre nom, puis votre message avec les trois lignes en bas. Si l'écran s'arrête sur `:` ou `(END)`, tapez `q` pour sortir.

**Ce qu'on regarde ensemble.** La ligne `Author:` porte votre nom, alors que c'est l'assistant qui a écrit le message : l'historique dit qui a enregistré, pas qui a écrit. L'assistant a-t-il suivi la règle ? A-t-il ajouté de lui-même une ligne `Co-Authored-By` ? Notez ce que vous voyez, avec l'outil et le modèle.

**Sans abonnement Claude Code** : le même prompt dans GitHub Copilot en mode Agent, ou écrivez les trois lignes à la main dans votre message de commit.

## Ce qu'on retient

- On ne conclut pas ce que les sources ne disent pas. « Ouvert » est une réponse d'équipe valable, si elle est écrite avec le nom de qui la lèvera.
- Une licence annoncée dans un extrait de code engage au moment où vous le gardez. Si du code arrive avec le nom de quelqu'un d'autre en haut : on ne le garde pas, on redemande autrement, et on l'écrit dans le message du commit.
- Vos droits et ceux de votre client viennent des mêmes textes et des mêmes contrats qu'avant. Le fournisseur de l'outil ne garde aucun droit sur le code produit.
- Ce que l'IA change : ce qui est généré et gardé tel quel n'a peut-être pas d'auteur, donc n'est peut-être pas protégé. La loi ne compte pas les lignes, elle demande si un humain a fait des choix.
- L'historique git dit qui a committé, pas qui a écrit. Pour l'audit, la trace se décide avant : un message de commit, une étiquette, une relecture notée. Une règle écrite dans `AGENTS.md` guide l'assistant sans l'obliger : on l'écrit, puis on la teste.
