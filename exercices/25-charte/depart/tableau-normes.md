# Repères pour une charte

Les normes ci-dessous sont des **repères**. Les textes payants n'ont pas été lus : seul le résumé public de chacune l'a été (02/11/2026). Ne prêtez à une norme aucune exigence que ce tableau ne dit pas.

## A. Normes et référentiels

| Référence | Ce que dit la page lue | Limite de ce qui a été lu |
|---|---|---|
| [ISO/IEC 27034-1:2011](https://www.iso.org/standard/44378.html) | Norme confirmée en 2022. Texte payant : 204 CHF. Lisez le résumé sur la page ISO avant de lui prêter un contenu | Résumé seul. Les autres parties de la série n'ont pas été lues |
| [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) | 26 pages. Texte payant : 155 CHF. Lisez le résumé sur la page ISO avant de lui prêter un contenu | Résumé seul : le texte n'a pas été lu |
| [OWASP Top 10 pour les applications LLM, 2025](https://genai.owasp.org/llm-top-10/) | Liste LLM01 à LLM10 | Liste lue, pas le détail de chaque risque |
| [CNIL, IA et RGPD : recommandations](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable) | Page du 07/02/2025 | Annonce lue, pas chaque fiche |
| [RGPD, EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679) | Article 5 (limitation de la conservation), article 22 (décision automatisée), article 33 (notification, 72 heures au plus tard si possible) | Articles cités seulement |

## B. Outils de suivi des usages

| Outil | Ce qu'on en sait | Vérifié |
|---|---|---|
| Claude Code, export OpenTelemetry | La documentation dit que Claude Code exporte des métriques (sessions, coût, jetons, lignes de code modifiées) et des événements (prompts, résultats d'outils, requêtes) quand la variable `CLAUDE_CODE_ENABLE_TELEMETRY=1` est posée. Page `https://code.claude.com/docs/en/monitoring-usage`, lue le 02/11/2026 en partie (les 100 000 premiers caractères) | Documentation, pas essayé |
| Claude Code, commande `/usage` | Citée dans le plan de la formation | **Non vérifiée à l'écran** : à tester avant de l'écrire dans une charte |
| Copilot, jauges d'usage | Citées dans le plan de la formation | **Non vérifiées à l'écran** : à chercher dans l'interface avant de l'écrire dans une charte |

Une charte qui promet « nous suivons les usages » doit nommer l'outil que quelqu'un lit vraiment.

## C. Un témoignage : un crochet qui bloque l'installation

La formatrice a mis en place un crochet (« hook ») : une commande que l'outil exécute automatiquement à un moment précis, ici avant qu'une installation soit lancée. La documentation de Claude Code décrit les hooks comme des commandes shell définies par l'utilisateur, exécutées à des points précis du cycle de vie de l'outil. **[Description du crochet de la formatrice et de son faux positif : à ajouter par elle avant la formation.]**
