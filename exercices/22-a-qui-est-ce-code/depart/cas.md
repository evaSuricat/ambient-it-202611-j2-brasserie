# Trois cas du Pigala

Les trois cas sont inventés pour la formation. Ils posent des questions de droits, de licences et d'auditabilité. Aucun ne demande un avis juridique : vous documentez la **décision de l'équipe** et sa trace.

## Cas A : l'extrait de code qui arrive avec une licence

En écrivant la validation du courriel du formulaire, l'assistant propose une fonction de dix lignes de code, précédée d'un en-tête de six lignes (seize lignes en tout). Le fichier `exercices/22-a-qui-est-ce-code/depart/extrait-licence.js` la reproduit : ouvrez-le. L'en-tête annonce un auteur, une année et une licence, c'est-à-dire les conditions auxquelles cet auteur autorise la réutilisation de son code. Personne dans l'équipe n'a écrit ce code ni ne connaît cet auteur.

Questions : que faites-vous de ces dix lignes de code ? Qu'est-ce que vous ne savez pas ? Que vérifiez-vous, et où ?

## Cas B : la question du client

Le gérant du Pigala demande : « Le code que vous me livrez a été en partie écrit par une IA. Est-ce que j'en suis propriétaire ? Est-ce que je peux le revendre ou le modifier librement ? »

Ce que disent les textes lus pour cet exercice (détail et liens dans `exercices/22-a-qui-est-ce-code/depart/SOURCES.md`) :

- **Le contrat, comme avant.** Pour tout logiciel, les droits du client viennent du contrat qui le lie à son prestataire : une cession des droits, écrite et détaillée droit par droit, ou une licence d'utilisation. L'usage d'une IA ne change pas cela.
- **Le fournisseur de l'outil.** Anthropic, qui édite Claude, écrit dans ses conditions pour les particuliers : « we assign to you all our right, title, and interest (if any) in Outputs », mot à mot « nous vous cédons tous nos droits sur les sorties, s'il y en a ». Pour ses offres d'entreprise : « Customer […] owns its Outputs », le client possède ses sorties.
- **Le droit français.** Le code de la propriété intellectuelle ne contient aucun article sur l'IA. Un logiciel est protégé s'il est original, c'est-à-dire s'il porte l'apport personnel de son auteur, une personne physique.
- **GitHub.** Une suggestion qui correspond à du code public peut être bloquée, ou montrée avec des informations sur la correspondance, y compris la licence quand elle est trouvée.

Questions : pour le gérant, qu'est-ce que l'usage d'une IA ne change pas ? Qu'est-ce qu'il change ? Que pouvez-vous lui affirmer à partir de ces textes ? Que ne pouvez-vous pas affirmer ? Que lui répondez-vous, par écrit, sans conclure un point de droit que ces textes ne tranchent pas ?

## Cas C : qui a écrit ce commit ?

Un audit demande, trois mois plus tard : « Quelles parties du code de la page de réservation ont été produites avec une IA, par quel outil, et qui les a relues ? »

Ouvrez `exercices/22-a-qui-est-ce-code/depart/journal-exemple.txt` : c'est un historique Git fictif, la liste des enregistrements d'un dépôt (les commits) avec, pour chacun, qui l'a fait, quand, et son message. La formatrice peut aussi montrer l'historique de son propre dépôt.

Questions : que permet de répondre l'historique tel quel ? Qu'est-ce qui manque ? Quelle pratique d'équipe (message de commit, étiquette, relecture notée) rendrait la réponse possible ?
