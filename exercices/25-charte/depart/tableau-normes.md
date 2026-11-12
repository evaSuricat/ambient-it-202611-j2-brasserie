# Repères pour une charte

Les normes ci-dessous sont des **repères**. Les textes payants n'ont pas été lus : seul le résumé public de chacune l'a été (02/11/2026). Ne prêtez à une norme aucune exigence que ce tableau ne dit pas.

## A. Normes et référentiels

| Référence | Ce que dit la page lue | Limite de ce qui a été lu |
|---|---|---|
| [ISO/IEC 27034-1:2011](https://www.iso.org/standard/44378.html) | Norme confirmée en 2022. Texte payant : 204 CHF. Lisez le résumé sur la page ISO avant de lui prêter un contenu | Résumé seul. Les autres parties de la série n'ont pas été lues |
| [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) | 26 pages. Texte payant : 155 CHF. Lisez le résumé sur la page ISO avant de lui prêter un contenu | Résumé seul : le texte n'a pas été lu |
| [OWASP Top 10 pour les applications LLM, 2025](https://genai.owasp.org/llm-top-10/) | Liste LLM01 à LLM10 | Liste lue, pas le détail de chaque risque |
| [CNIL, IA et RGPD : recommandations](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable) | Page du 07/02/2025 | Annonce lue, pas chaque fiche |
| [RGPD, EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679) | Article 5 (limitation de la conservation), article 22 (décision automatisée), article 33 (notification à l'autorité de contrôle « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance ») | Articles 22 et 33 : paragraphes cités lus sur EUR-Lex le 02/11/2026. Article 5 : mention seulement |

## B. Outils de suivi des usages

| Outil | Ce qu'on en sait | Vérifié |
|---|---|---|
| Claude Code, export OpenTelemetry | La documentation dit que Claude Code exporte des métriques (sessions, coût, jetons, lignes de code modifiées) et des événements (prompts, résultats d'outils, requêtes) quand la variable `CLAUDE_CODE_ENABLE_TELEMETRY=1` est posée. Page `https://code.claude.com/docs/en/monitoring-usage`, lue le 02/11/2026 en partie (les 100 000 premiers caractères) | Documentation, pas essayé |
| Claude Code, commande `/usage` | Commande de Claude Code, non vérifiée à l'écran pour cette formation | **À tester** : avant de l'écrire dans une charte |
| Copilot, jauges d'usage | Jauges de Copilot, non vérifiées à l'écran pour cette formation | **À chercher** : dans l'interface avant de l'écrire dans une charte |

Une charte qui promet « nous suivons les usages » doit nommer l'outil que quelqu'un lit vraiment.

## C. Un témoignage : un garde-fou (hook) qui demande le GO avant toute installation

Témoignage de la formatrice, écrit d'après son journal du 23/10/2026. Un hook est un petit script que Claude Code lance à un moment précis, ici juste avant chaque commande de terminal. Il n'existe pas chez les stagiaires.

**La règle.** Depuis le 23/10/2026, le fichier `AGENTS.md` de son poste dit : avant d'installer un langage ou une bibliothèque, lister ce qui existe déjà, dire ce qui manque et pourquoi, attendre le GO. La règle vient de deux Python installés le même jour d'octobre 2025 sans qu'aucun projet ne dise lequel il attendait : personne ne l'a vu passer.

**Le contrôle.** Une règle écrite dépend de la mémoire de l'assistant. Le jour même, elle est devenue un hook `PreToolUse` déclaré dans `.claude/settings.json` : un script PowerShell lit chaque commande avant son exécution ; s'il reconnaît une installation (`pip install`, `winget install`, `npm install -g`, `apt install`, un `.exe` silencieux, un script téléchargé envoyé droit dans un shell…), il répond « ask » et la fenêtre de permission s'affiche avec la raison, même en mode automatique. Toute autre commande passe sans rien afficher.

**La preuve.** Le script est versionné dans le dépôt de la formatrice, et un jeu de treize commandes de test le rejoue après chaque modification.

**Ce qui s'est passé.** Le jour même, la fenêtre s'est ouverte sur un `winget install --help` : la commande ne faisait que lire l'aide, le motif ne fait pas la différence. Le soir, un faux positif plus gênant : un compte rendu de fin de session qui *citait* les commandes de la journée dans un bloc de texte a déclenché le hook, parce qu'il lisait la commande entière, texte cité compris. Depuis, le script ignore le corps de ces blocs (les heredocs), et le cas a rejoint le jeu de tests.

**Les limites, écrites plutôt que cachées.** Il laisse passer un `npm install` local à un projet (par choix : les dépendances d'un site). Une commande citée dans un message de commit peut encore le déclencher : on accepte la fenêtre. Et il ne vaut que sur ce poste : un contrôle d'équipe se commite dans le dépôt (`settings.json`), pas dans un réglage personnel.

Ce que ça illustre pour votre charte : une règle avec qui (l'assistant), contrôle (le hook) et preuve (le script versionné et son jeu de tests), un faux positif corrigé, et des limites nommées.
