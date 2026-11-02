# Règles du projet Le Pigala

Page web d'une brasserie-restaurant fictive de Montreuil, qui prend maintenant des réservations. Le brief est dans `brief.md`, la carte dans `carte.md` : ce sont les seules sources de texte. Lis-les avant toute modification.

## Langue et ton

- Tout est en français, avec les accents, y compris les commentaires du code.
- Vouvoiement, ton direct et chaleureux. Pas de superlatif, pas de tiret long.

## HTML

- HTML sémantique : `header`, `nav`, `main`, `section`, `footer`, `address`. Un seul `h1`. Les titres se suivent sans saut de niveau.
- Chaque `section` a un titre `h2` et un attribut `aria-labelledby` qui pointe dessus.
- Toute image a un attribut `alt` qui décrit ce qu'elle montre, ou `alt=""` si elle est décorative.
- Les numéros de téléphone sont des liens `tel:`.
- Tout champ de formulaire a un `label` relié par `for` et `id`, et un `autocomplete` adapté.

## CSS

- Les couleurs de l'enseigne sont des variables dans `:root` : orange `#F26B1D`, bleu nuit `#1D2A44`, crème `#FFF6E9`, vert houblon `#5C8A3A`. Réutilise les variables déjà déclarées dans la feuille principale, n'en invente pas.
- Contraste texte sur fond d'au moins 4,5 pour 1. L'orange `#F26B1D` ne sert ni de texte sur crème, ni de fond sous un texte blanc. Pour un bouton : orange foncé `#B84A0C`, texte blanc.
- La page se lit sur un téléphone sans défilement horizontal.

## Conventions de l'équipe

- Tout plan d'accès est accompagné d'un lien « Ouvrir le plan dans OpenStreetMap » vers openstreetmap.org, ouvert dans un nouvel onglet.
- Chaque nouveau composant a sa propre feuille de style dans le dossier `css/`, reliée par une balise `link` dans `index.html`.
- Chaque section ajoutée est encadrée par les commentaires `<!-- DÉBUT nom -->` et `<!-- FIN nom -->`.

## JavaScript

- Aucun framework, aucune bibliothèque, aucune ressource chargée depuis un autre domaine : la page s'ouvre sans Internet.
- `script.js` lit `/api/carte`. `reservations.js` envoie le formulaire de réservation à `/api/reservations`. Il n'y a pas d'autre script.

## Contenu et données

- Tout texte de contenu vient de `brief.md` ou de `carte.md`. Si une information manque, dis-le plutôt que de l'inventer.
- Les libellés de champs et les messages d'erreur d'un formulaire sont de l'interface : permis, sans promesse inventée (pas de délai de rappel, pas de confirmation garantie).
- Les données de ce projet sont fictives. Ne mets jamais une vraie personne, un vrai client ou un vrai secret dans un fichier, dans un prompt ou dans un commit.
- N'affiche jamais la valeur d'un secret ou d'un jeton dans une réponse : teste sa présence, pas son contenu.

## Façon de travailler

- Annonce en une ligne ce qui va être modifié avant de modifier.
- Après une modification de `index.html`, vérifie que la page reste valide (balises fermées, un seul `h1`).
- Ne lance pas le serveur toi-même : il ne rend jamais la main, la personne le lance dans son terminal.
