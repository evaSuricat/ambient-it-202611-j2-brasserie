# E24 · Revue d'une user story

**Point du programme** : atelier officiel « user story » : biais, risques, décisions automatisées. Public mixte (développeurs, sécurité, chefs de projet) : **on ne code pas**.

**Durée** : 45 minutes.

## Ce qu'on fait

Le gérant du Pigala veut qu'une IA trie les demandes de réservation et rédige la réponse. Vous relisez sa user story en groupe, vous regardez les données qui la justifient, vous demandez à une IA de lister les risques, **puis chacun trie ce qu'elle propose** et complète ce qu'elle a manqué. L'IA propose, vous décidez.

Tout est fictif (`exercices/24-revue-user-story/depart/SOURCES.md`). Les codes postaux 99001 à 99004 n'existent pas. Sans abonnement : une IA gratuite en mode Ask suffit (aucun fichier n'est modifié), ou la grille se remplit sans IA, ou vous suivez sur l'écran partagé. Cet exercice se fait par groupes de trois ou quatre, avec au moins deux profils différents.

### Étape 0 : enregistrer le point de départ

Depuis la racine de `stagiaire_J2` :

```
git add exercices/24-revue-user-story
```

```
git commit -m "E24 : état avant la grille de risques"
```

Résultat attendu : « nothing to commit » est normal si rien n'a changé depuis le clonage.

### Étape 1 : lire la user story, chacun avec sa casquette (5 min)

Ouvrez `exercices/24-revue-user-story/depart/user-story.md`. Chacun la lit avec sa question : le développeur demande « où passent les données, et que reçoit le modèle ? », la personne sécurité « qu'est-ce qu'on peut détourner ? », le chef de projet « qui décide, qui répond, qui est prévenu ? ». Écrivez chacun une question avant de passer à l'étape 2.

### Étape 2 : regarder les données (10 min)

Dans un terminal, depuis la racine :

```
cd exercices/24-revue-user-story/depart
```

```
python calcul.py
```

Résultat attendu : quatre blocs : le total (20 absences sur 120 demandes), les absences par code postal, par créneau horaire, puis croisés. Si `python` n'existe pas, tapez `python3`. Lisez en trois temps et écrivez une phrase pour chacun :

1. Par code postal : quelles zones ont un taux d'absence plus élevé ?
2. Par créneau : que voyez-vous ?
3. Croisé : l'écart entre zones est-il le même dans chaque créneau ?

Sans affirmer ce que le tableau ne dit pas : 120 lignes, c'est peu, et un taux sur 6 ou 8 demandes bouge beaucoup avec une seule absence. Question à garder pour la grille : si l'IA refuse les demandes des zones 99003 et 99004 parce que leur taux est plus élevé, que se passe-t-il pour les gens qui y habitent ? Un code postal peut remplacer, sans le dire, une caractéristique qu'on n'a pas le droit d'utiliser.

### Étape 3 : demander les risques à l'IA (5 min)

Dans Claude Code, ou dans le chat de Copilot en mode **Ask** (aucun fichier à modifier) :

```
Lis exercices/24-revue-user-story/depart/user-story.md et historique.csv. Liste les risques de cette user story (sécurité, protection des données, équité, qualité de la réponse). Pour chacun : la phrase de la user story concernée, une gravité de 1 à 3, une remédiation. Ne cite aucun article de loi ni aucune norme : je te les donnerai si besoin.
```

Notez l'**outil et le modèle** utilisés. Recopiez trois propositions de la réponse dans la partie B de `grille-risques.md`, sans les corriger.

### Étape 4 : remplir la grille en groupe (20 min)

Ouvrez `exercices/24-revue-user-story/depart/grille-risques.md`. Pour chaque risque retenu par le groupe : où dans la user story, une gravité de 1 à 3, une remédiation, un critère d'acceptation **vérifiable**, et qui l'a trouvé (œil, calcul, outil, IA, discussion). Au moins six lignes. Triez les trois propositions de l'IA de la partie B : juste, faux ou à ignorer, et pourquoi.

Points à examiner, que l'IA peut avoir manqués ou mal traités (ne les cherchez pas tous : voyez ceux que votre groupe y trouve) :

- **Le champ code postal** : est-il nécessaire pour réserver une table ? À quoi sert-il vraiment dans la user story ?
- **Les commentaires** : revoyez la réservation numéro 15 (le commentaire qui commence par « Ignore tes consignes… ») dans `ressources/reservations.csv`. Que fait une IA qui lit cette ligne et qui a le pouvoir d'accepter ou de refuser ?
- **L'envoi automatique, sans relecture** : l'exemple de réponse de la user story promet une table. Sur quelle donnée l'IA s'appuie-t-elle pour savoir qu'elle est libre ? Cette donnée existe-t-elle dans le projet ?
- **Le refus** : est-ce que refuser une table « affecte la personne de manière significative » ? Lisez l'article 22 du RGPD ([EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679)) : son paragraphe 1 pose le « droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire » ; son paragraphe 2 prévoit des exceptions (contrat, droit de l'Union ou de l'État membre, consentement) (EUR-Lex, règlement 2016/679, lu le 02/11/2026). **La consigne ne dit pas qu'il s'applique ici** ; écrivez dans la partie D la question que votre groupe ne tranche pas, et qui la lèvera.
- **Les critères d'acceptation du gérant** : « le taux d'absence baisse » est-il vérifiable ? Qui mesure, sur quoi, comparé à quoi ?
- **Les données envoyées au modèle** : revoyez l'exercice 21.

Résultat attendu : une grille d'au moins six lignes, trois propositions triées, une question ouverte.

### Étape 5 : mise en commun (5 min)

Chaque groupe présente **un** risque que l'IA n'avait pas vu et une remédiation avec son critère vérifiable. Les autres disent si le critère se vérifie vraiment.

### Étape 6 : enregistrer

Depuis la racine :

```
cd ../../..
```

```
git add exercices/24-revue-user-story
```

```
git commit -m "E24 : grille de risques de la user story"
```

Résultat attendu : une ligne « files changed » qui cite `grille-risques.md`.

## Livrable

`grille-risques.md` rempli : au moins six risques avec gravité, remédiation, critère vérifiable et « qui l'a trouvé » ; le tri de trois propositions de l'IA ; une question laissée ouverte.

## Ce qu'on retient

- L'IA propose, chacun trie. Une liste de risques générée est un point de départ ; ce qu'elle oublie se voit avec des yeux de métiers différents.
- Un code postal n'est pas neutre : il peut servir de variable de substitution. Le calcul montre qu'on peut aussi se tromper en l'écartant sans regarder le créneau.
- Une décision automatisée qui touche une personne se discute avec l'article 22 du RGPD en main, avant d'être construite.
- Un critère d'acceptation se mesure.
