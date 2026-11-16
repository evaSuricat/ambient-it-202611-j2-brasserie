# E25 · Une charte qui se vérifie

**Point du programme** : atelier officiel « charte d'usage de l'IA » ; cadre, suivi des usages, normes.

**Durée** : 25 minutes.

## Ce qu'on fait

Une charte d'usage de l'IA est une page de règles que votre équipe s'engage à tenir. Une règle ne sert à rien si personne ne peut dire, plus tard, si elle a été tenue. Vous allez donc écrire **trois règles** seulement, et pour chacune deux choses : **qui** la tient, et **quelle preuve** on garde. Une règle sans preuve est un vœu : c'est bien d'en avoir, mais on le range à part.

Puis la formatrice montre **trois règles déjà testées pendant la journée**, pour voir à quoi ressemble une règle dont on a la preuve. Enfin deux chartes sont lues à voix haute.

Sans abonnement Claude Code, rien ne change : cet atelier se fait à la main, sans outil. Rien de personnel à l'écran.

### Étape 1 : dix règles qui ne se vérifient pas, deux qui se vérifient (5 min)

La formatrice projette `exercices/25-charte/depart/charte-exemple-ia.md` : une charte en dix règles, écrite pour l'exercice dans le style de ce qu'on obtient d'une IA en une phrase. Elles sonnent toutes sérieuses. Question pour la salle : **laquelle peut-on prouver demain qu'elle a été tenue ?**

Ce qui manque à chacune : un **qui** et une **preuve**. Deux exemples de règles qui les ont, les vôtres seront différentes :

- *Règle* : chaque demande de fusion de code (merge request) passe l'analyse SonarQube avant la relecture par une personne. *Qui* : l'auteur de la demande. *Preuve* : le rapport SonarQube lié à la demande.
- *Règle* : le code classé confidentiel n'est envoyé qu'à un fournisseur choisi par l'équipe (serveur interne, cloud de l'entreprise en région européenne avec conservation à zéro, ou fournisseur payant avec conservation à zéro vérifiée). *Qui* : le responsable technique. *Preuve* : la configuration de l'outil, avec le fournisseur et la région, relue à chaque mise à jour.

À l'inverse, « être prudent avec les données des clients » n'a ni qui ni preuve : c'est un vœu. Pour chaque règle que vous écrirez, posez-vous la question : **peut-on prouver demain qu'elle a été tenue ou violée ?**

### Étape 2 : écrire vos trois règles (8 min)

Copiez le modèle, depuis la racine de `stagiaire_J2` :

```
cp exercices/25-charte/depart/modele-charte.md exercices/25-charte/depart/charte-ia.md
```

Résultat attendu : aucun message, et le fichier `charte-ia.md` apparaît à côté de `modele-charte.md`. Remplissez `charte-ia.md` et laissez `modele-charte.md` intact.

Dans le tableau, trois lignes : la règle (une phrase avec un verbe), qui la tient, quelle preuve on garde. Vos règles viennent de votre journée : ce qui a fui à l'exercice 21, la fiche de l'exercice 19, la décision de l'exercice 22, la grille de l'exercice 24. Une idée que vous ne pouvez pas prouver va dans « Les vœux ». La section sur le suivi des usages est facultative.

### Étape 3 : regarder la démonstration des règles testées (6 min)

La formatrice montre trois règles qui ont été **essayées pour de vrai** pendant la journée. Pour chacune : la règle, qui la tient, la preuve, et ce qui s'est passé.

1. **À l'exercice 21, étape 8** : la règle d'`AGENTS.md` « n'envoie jamais à un modèle une donnée de `donnees/` ». Claude a refusé de lire un fichier de `donnees/` et a cité cette règle.
2. **À l'exercice 21, étape 11** : la règle d'`AGENTS.md` « aucune route publique ne lit les réservations ». Claude a refusé d'ajouter une route publique qui les lisait, en citant `AGENTS.md`.
3. **Un hook d'équipe** : un hook est un petit programme que Claude Code lance automatiquement à un moment précis, que le modèle le veuille ou non. Chez la formatrice, un hook a bloqué le lancement d'un sous-agent tant que le modèle et le coût n'étaient pas annoncés.

Regardez ce qui distingue ces trois règles : les deux premières reposent sur la bonne volonté de l'outil (un autre outil, ou un autre modèle, peut faire autrement : l'essai se refait quand l'outil change) ; la troisième est imposée par un programme. Question à vous poser : laquelle de vos trois règles pourrait être testée de l'une de ces façons ?

### Étape 4 : présenter (6 min)

Deux chartes sont lues à voix haute. Chacun dit ses trois règles, avec leur qui et leur preuve. La salle répond à une seule question par règle : peut-on prouver demain qu'elle a été tenue ?

### Pour enregistrer (facultatif)

Depuis la racine :

```
git add exercices/25-charte
```

```
git commit -m "E25 : charte d'usage de l'IA en trois règles"
```

Résultat attendu : une ligne « files changed » qui cite `charte-ia.md`.

## Livrable

`exercices/25-charte/depart/charte-ia.md` : une page, trois règles avec qui et preuve ; les vœux.

## Ce qu'on retient

- Une règle sans preuve est un vœu. La preuve distingue une charte d'une affiche.
- Trois règles qu'on tient valent mieux que dix qu'on oublie.
- Une règle écrite dans `AGENTS.md` guide l'outil sans l'obliger ; un hook, lui, s'impose. Dans les deux cas, on essaie la règle pour de vrai, et on refait l'essai quand l'outil change.

Pour aller plus loin chez vous : `tableau-normes.md` (normes citées, outils de suivi, et le témoignage d'un hook de la formatrice), `regles-testees-exemples.md` (trois façons de rendre une règle vérifiable) et `charte-exemple-ia.md` (les dix règles de l'étape 1, écrites pour l'exercice : à reformuler une par une avec un qui et une preuve) sont dans `exercices/25-charte/depart/`.
