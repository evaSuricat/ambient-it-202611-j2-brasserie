# Trois cas du Pigala

Les trois cas sont inventés pour la formation. Ils posent des questions de droits, de licences et d'auditabilité. Aucun ne demande un avis juridique : vous documentez la **décision de l'équipe** et sa trace.

## Cas A : le snippet qui arrive avec une licence

En écrivant la validation du courriel du formulaire, l'assistant propose une fonction de douze lignes, qui commence par un en-tête. Le fichier `extrait-licence.js` la reproduit. L'en-tête annonce un auteur, une année et une licence. Personne dans l'équipe n'a écrit ce code ni ne connaît cet auteur.

Questions : que faites-vous de ces douze lignes ? Qu'est-ce que vous ne savez pas ? Que vérifiez-vous, et où ?

## Cas B : la question du client

Le gérant du Pigala demande : « Le code que vous me livrez a été en partie écrit par une IA. Est-ce que j'en suis propriétaire ? Est-ce que je peux le revendre ou le modifier librement ? »

Une phrase des conditions d'utilisation d'Anthropic (conditions pour les particuliers, entrées en vigueur le 8 octobre 2025, section 4) dit : « we assign to you all our right, title, and interest (if any) in Outputs ». Une page de la documentation GitHub sur les suggestions de code (lue le 02/11/2026) dit que les suggestions qui correspondent à du code public peuvent être bloquées ou montrées avec des informations sur la correspondance, y compris la licence quand elle est trouvée.

Questions : que pouvez-vous affirmer au gérant à partir de ces deux textes ? Que ne pouvez-vous pas affirmer ? Que lui répondez-vous, par écrit, sans conclure un point de droit que ces textes ne tranchent pas ?

## Cas C : qui a écrit ce commit ?

Un audit demande, trois mois plus tard : « Quelles parties du code de la page de réservation ont été produites avec une IA, par quel outil, et qui les a relues ? »

Regardez l'historique de **votre** dépôt `stagiaire_J2` (étape 3 de la consigne). S'il est trop court pour l'exercice, `journal-exemple.txt` en fournit un fictif.

Questions : que permet de répondre l'historique tel quel ? Qu'est-ce qui manque ? Quelle pratique d'équipe (message de commit, étiquette, relecture notée) rendrait la réponse possible ?
