# Sources de l'exercice 21

| Fichier | Origine |
|---|---|
| `carte.db`, `reservations.csv`, `servir.py`, `reservations.js`, la page | La solution de l'exercice 17 : mêmes 30 réservations fictives, même serveur. Les failles du serveur (fichiers servis sans filtre, recherche par concaténation et sans contrôle d'accès) sont posées exprès |
| `test_securite.py` | Écrit pour la formation, bibliothèque standard seulement. Il copie ce dossier dans un dossier temporaire et y lance le serveur : votre base n'est jamais modifiée |
| `afficher_extrait.py`, `anonymiser_regex.py` | Écrits pour la formation |
| Règle de refus de lecture de Claude Code | [Documentation Claude Code, permissions](https://code.claude.com/docs/en/permissions), lue le 02/11/2026 : la règle `Read` s'applique aux outils de fichiers de Claude et aux commandes reconnues comme `cat`, `head`, `tail`, `sed`, `tee` ; elle ne s'applique pas à une commande qui lit des fichiers sans les nommer (par exemple `grep -r` lancé dans le dossier), ni à un script Python ou Node qui ouvre le fichier lui-même. Pour une garantie au niveau du système, la documentation renvoie au mode bac à sable (sandbox) |
| Injection SQL | [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) : les requêtes préparées sont la défense n° 1 |
| Risques des applications à base de modèles | [OWASP Top 10 LLM 2025](https://genai.owasp.org/llm-top-10/), liste LLM01 à LLM10 |
| Anonymisation | [CNIL, L'anonymisation de données personnelles](https://www.cnil.fr/fr/lanonymisation-de-donnees-personnelles), page du 19/05/2020 : trois critères, et la pseudonymisation est réversible |
