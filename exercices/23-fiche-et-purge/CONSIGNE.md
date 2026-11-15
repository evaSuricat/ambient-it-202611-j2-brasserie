# E23 · La fiche et la purge

**Point du programme** : RGPD, traçabilité, données, conservation, appliqués au Pigala.

**Durée** : 10 minutes. **C'est une démonstration de la formatrice** : vous regardez et vous discutez. Vous n'écrivez rien, vous ne committez rien.

## Pourquoi cette démonstration

Le site du Pigala garde les noms, les téléphones et les courriels de ses clients. Deux questions se posent : qu'est-ce qu'on en fait exactement, et combien de temps on le garde ? Le RGPD (la loi européenne sur les données personnelles) demande de pouvoir répondre aux deux. Une durée de conservation écrite dans un document ne supprime rien : il faut aussi un programme qui supprime vraiment.

## Ce que la formatrice montre

1. **La fiche de traitement** : une page qui dit ce que le projet fait des données des clients. Pourquoi on les demande, lesquelles, qui y accède, combien de temps on les garde. Elle est remplie à partir du code, pas de mémoire, et projetée.
2. **La page de la CNIL sur les durées de conservation** (la CNIL est l'autorité française qui surveille les données personnelles) : https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees (page du 02/04/2026). Elle ne donne pas un chiffre unique pour tous les cas : la durée se fixe et se justifie selon l'usage des données.
3. **La purge**, c'est-à-dire la suppression des réservations dont la date est passée. Le script `purger.py` est lancé sur **une copie** de la base, jamais sur la vraie. D'abord en **simulation** : il annonce combien de réservations il supprimerait, sans rien supprimer. Puis **pour de vrai**, sur la copie : il supprime et note l'opération dans un journal.

## Trois questions à vous poser en regardant

- Combien de temps garderiez-vous une réservation une fois la date passée, et pourquoi ?
- Pourquoi essaie-t-on d'abord sur une copie, et d'abord en simulation ?
- Que doit contenir le journal de la purge ? Et que ne doit-il surtout pas contenir ?

## Le message à retenir

Une durée de conservation se décide et se justifie, puis elle se met en œuvre par un programme qu'on essaie à blanc, sur une copie. Un journal qui recopie des noms ou des téléphones recrée le problème qu'il devait régler.

Cette démonstration ne dit pas si Le Pigala doit tenir un registre officiel des traitements (l'article 30 du RGPD) : ce n'est pas un avis juridique.

## Pour la refaire chez vous

Tout est dans `exercices/23-fiche-et-purge/depart/` : `fiche-modele.md` à remplir, `test_purge.py` (quatre tests qui disent quand votre `purger.py` est juste) et la base fictive dans `donnees/`. Le script `purger.py` est à écrire avec votre outil.
