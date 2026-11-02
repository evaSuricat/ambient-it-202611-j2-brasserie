# Trois façons de rendre une règle vérifiable

Une règle de charte devient vérifiable quand quelque chose la contrôle et laisse une preuve. Trois exemples, tirés des exercices du jour. Ce sont des modèles de raisonnement : vos règles seront les vôtres.

## 1. Une ligne d'AGENTS.md

- Règle de charte : « Aucune donnée personnelle de client n'est envoyée à un modèle. »
- Traduction : la ligne « N'envoie jamais à un modèle une donnée de donnees/, même fictive » de l'exercice 21.
- Qui : chaque développeur, dans son outil.
- Contrôle : demander à l'outil, dans une session neuve, de faire exactement ce que la règle interdit, et lire ce qu'il fait.
- Preuve : la phrase d'`AGENTS.md`, le prompt d'essai, outil et modèle, le résultat. Un résultat peut changer d'un outil à l'autre : l'essai se refait quand l'outil change.
- Limite : `AGENTS.md` guide l'outil, il ne le bloque pas.

## 2. Une règle de refus de lecture

- Règle de charte : « Le dossier des données clients n'est pas lisible par l'assistant. »
- Traduction : `Read(**/donnees/**)` dans `.claude/settings.json` (exercice 21).
- Contrôle : demander la lecture d'un fichier du dossier, vérifier le refus ; puis chercher le contournement (la documentation de Claude Code dit qu'une commande qui lit sans nommer le fichier, ou un script, n'est pas couvert).
- Preuve : le refus constaté et le contournement constaté.
- Limite : pour une garantie au niveau du système, la documentation renvoie au mode bac à sable.

## 3. Un test qui reste

- Règle de charte : « Le serveur ne publie ni la base ni le code. »
- Traduction : `test_securite.py` (exercice 21).
- Contrôle : `python -m unittest`, à chaque modification du serveur.
- Preuve : la sortie du test, rouge puis verte, dans l'historique du dépôt.
- Limite : un test vérifie ce qu'il teste, pas le reste.
