# Le Pigala : la page prend des réservations, on protège les données de ses clients

Formation « Développeurs : boostez vos performances grâce à l'IA » (Ambient IT, novembre 2026), journée 2.

Le fil rouge reprend celui du jour 1 : la brasserie-restaurant fictive de Montreuil. Sa page prend maintenant des réservations, donc elle enregistre des noms, des téléphones et des courriels. Toute la journée, on se demande ce qui sort du poste, ce qui reste chez les outils, et comment s'en protéger. Tout est fictif : aucune vraie personne, aucun vrai client, aucun vrai secret dans ce dépôt. Les données et leurs sources sont décrites dans `ressources/SOURCES-DONNEES.md`.

## Démarrer

Prérequis : les mêmes qu'au jour 1 (VS Code avec GitHub Copilot et Claude Code connectés, Git, Python 3.12, Google Chrome). **Docker et Ollama ne sont exigés de personne** : ils sont montrés par la formatrice.

Claude Code demande un abonnement payant. Sans abonnement, chaque exercice a un chemin avec GitHub Copilot Free, ou se suit sur l'écran partagé de la formatrice. Avec Copilot Free, GitHub choisit le modèle, la revue de code peut ne rien dire, la complétion (Tab) invente, et **« New Chat » repasse en mode Ask : remettez Agent à chaque fois**. Une comparaison entre deux outils dit toujours « outil et modèle ».

1. Créer un dossier `stagiaire_J2` (là où vous rangez vos dossiers de formation), l'ouvrir dans VS Code (Fichier, Ouvrir le dossier, puis « Yes, I trust the authors »), et y cloner ce dépôt depuis un terminal de VS Code, sans oublier le point final :

```
git clone <adresse à venir> .
```

2. Créer sa branche de travail, une par personne :

```
git switch -c prenom
```

3. Garder la racine de `stagiaire_J2` ouverte toute la journée : c'est là que les assistants lisent `AGENTS.md`. Chaque exercice a un `CONSIGNE.md` dans `exercices/NN-nom/`. Les commandes se lancent depuis la racine, sauf quand la consigne dit de faire `cd`.

Si `python` n'existe pas sur votre poste (Mac, certains Linux), tapez `python3` partout.

## Une seule page, d'exercice en exercice

**Tout le monde part de la page fournie** : personne n'a besoin de sa page du jour 1. L'exercice 15, premier de la journée, part de la page sans photos (celle avec « Photo de la façade, à venir »). L'exercice 17 fournit sa propre page, déjà dotée de ses photos. Ensuite, chaque `depart/` est la solution de l'exercice précédent quand l'exercice touche la page ou le serveur (17, 21, 23).

| Exercice | Point du programme | Durée |
|---|---|---|
| 15 L'agent fait le sale boulot | Atelier officiel : automatiser une tâche répétitive avec un agent. Premier de la journée, il vérifie aussi les postes | 20 min chronométrées |
| 17 Les réservations arrivent | Le fil rouge reprend : une page qui enregistre des données personnelles | 15 min |
| 18 Avant d'exécuter | Sécurité avant exécution du code, hallucinations. Tri à l'oral, sans outil | 10 min |
| 19 Ce que mes outils gardent de moi | Fuite de données, conservation | 15 min |
| 20 Trois fuites dans un Dockerfile | Publication d'images Docker et confidentialité | 10 min |
| 21 Sécuriser le workflow | Atelier officiel : requête SQL sensible, anonymisation, sous-agent de relecture | 40 min, et 10 min de marge |
| 22 À qui est ce code ? | Propriété du code, droits, licences, auditabilité. En slides et en discussion | 20 min |
| 23 La fiche et la purge | RGPD, traçabilité, conservation | 25 min |
| 24 Revue d'une user story | Atelier officiel : biais et risques d'une user story | 45 min |
| 25 Une charte qui se vérifie | Atelier officiel : charte d'usage de l'IA | 45 min |
| Bonus formulaire | Formulaire de réservation robuste | 20 à 30 min |
| Bonus sous-agent | Écrire son propre sous-agent dans `.claude/agents/` | 20 à 30 min |

## Le serveur local

Depuis le dossier `depart/` de l'exercice :

```
python servir.py
```

Puis http://127.0.0.1:8000/ dans Chrome. `Ctrl+C` arrête le serveur. Deux situations à ne pas confondre : « Ce site est inaccessible » veut dire que le serveur n'est pas lancé (rien n'écoute sur le port) ; un 404 ou un 500 dans la console du navigateur (F12) veut dire que le serveur tourne et que quelque chose est faux dans le code ou l'adresse.

## Ce que ce dépôt contient, et ce qu'il ne contient pas

- `carte.db` est versionnée dans les `depart/` : c'est voulu, la base fait partie de l'exercice. Elle ne contient que des données fictives. Dans un vrai projet, on ne versionne jamais une base de clients.
- Les solutions complètes vivent dans le dépôt de la formatrice. Chaque `depart/` qui prolonge un exercice précédent en contient la solution : celui d'E23 contient `servir.py`, `gerant.py` et `separer_base.py` corrigés, qui sont la solution d'E21, voulue ainsi.
- `.claude/agents/relecteur-code.md`, à la racine, est le sous-agent de relecture de l'exercice 21 : il est versionné exprès. Le dossier `.venv/` que l'exercice 15 crée à la racine est ignoré par git.
- Le `.gitignore` ne contient que le nécessaire (`.venv/` et les fichiers de l'éditeur). Il n'ignore pas `rapports/` : vos dossiers de comptes rendus se committent normalement.
