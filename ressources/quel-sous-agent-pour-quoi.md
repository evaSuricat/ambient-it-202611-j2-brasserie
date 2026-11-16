# Quel sous-agent pour quoi

Un sous-agent est un assistant spécialisé que Claude Code lance à votre demande, avec ses propres consignes et ses propres outils. Les fichiers qui les décrivent sont dans `.claude/agents/`, à la racine du dépôt. Les trois sous-agents de cette formation sont en lecture seule : ils lisent, ils ne modifient rien et ne lancent aucune commande.

| | `relecteur-code` | `detecteur-coordonnees` | `pre-analyse-juridique` |
|---|---|---|---|
| Ce qu'il regarde | Un fichier de code | Un dossier de fichiers | Les textes rangés dans `ressources/sources-juridiques/` |
| Ce qu'il cherche | Des failles : requêtes SQL fabriquées par collage, fichiers ou routes exposés | Des téléphones et des courriels écrits en clair | Ce que les textes disent d'une question |
| Ce qu'il rend | Une liste de défauts, avec gravité et correction | Une liste de fichiers, sans recopier les valeurs | Des citations, ce que les textes ne disent pas, trois questions pour un juriste |
| Quand le lancer | Avant de corriger du code | Avant de committer un dossier de données ou de documents | Avant d'écrire à un juriste, ou quand quelqu'un dit « c'est la loi » |
| Cite-t-il la loi | Non | Non | Oui, mot pour mot, et seulement cela |
| Ce qu'il ne dit jamais | Que le code est sûr | Que le projet respecte le RGPD | Ce que vous devez faire |
| Où on le voit | Exercice 21 | Bonus « Écrire son propre sous-agent » | Exercices 24 et 25 |

## Pour choisir en une question

- « Ce code a-t-il une faille ? » : `relecteur-code`.
- « Ce dossier contient-il des coordonnées de personnes ? » : `detecteur-coordonnees`.
- « Que dit le texte, et que faut-il demander au juriste ? » : `pre-analyse-juridique`.
- « Sommes-nous en règle ? » : aucun des trois. C'est la question d'un juriste. `pre-analyse-juridique` aide à la lui poser.

## Ce que « rien trouvé » veut dire

`detecteur-coordonnees` ne lit aucune loi : il cherche des numéros de téléphone et des adresses de courriel. C'est un détecteur, pas un contrôle de conformité. S'il ne trouve rien, cela veut dire qu'il n'a vu aucune coordonnée dans les fichiers qu'il a pu lire. Cela ne dit rien du respect du RGPD par le projet. Un détecteur de fumée qui se tait ne prouve pas qu'il n'y a pas le feu.

## Comment en lancer un

Dans Claude Code, écrivez « Utilise le sous-agent » suivi de son nom, puis ce que vous lui confiez. Par exemple : « Utilise le sous-agent relecteur-code sur exercices/21-securiser-workflow/depart/servir.py. »

Claude Code lit les sous-agents au démarrage : après avoir ajouté ou modifié un fichier de `.claude/agents/`, fermez la session et ouvrez-en une nouvelle.

## Ce qui vaut pour les trois

- Leur réponse est une proposition : vous la relisez et vous décidez.
- Ils répondent différemment d'une fois sur l'autre. Ce qu'ils disent se vérifie.
- Les outils listés dans leur en-tête (`Read, Grep, Glob`) sont leur vraie limite : sans `Edit` ni `Bash`, ils ne peuvent ni écrire ni exécuter.
