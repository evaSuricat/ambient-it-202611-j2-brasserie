# Sources des données de l'exercice 17

| Fichier | Contenu | Origine |
|---|---|---|
| `reservations.csv` | 30 réservations de novembre et décembre 2026 | Inventées pour la formation. Prénoms et noms composés au hasard, courriels en `@example.com` (domaine réservé aux exemples), téléphones dans les tranches que l'Arcep réserve à la fiction (01 99 00 et 06 39 98, voir `ressources/SOURCES-DONNEES.md`). Les commentaires de quelques lignes sont piégés exprès, pour l'exercice 21 |
| `carte.csv`, `carte.md`, `brief.md` | La carte et le brief du Pigala | Inventés pour la formation (jour 1) |
| `carte.db` | La carte (20 lignes) et les 30 réservations | Générée par `charger.py` puis `charger_reservations.py` à partir des deux fichiers ci-dessus. Versionnée exprès : elle ne contient que du fictif |
| `index.html`, `style.css`, `script.js`, `css/`, `photos/` | La page de départ | Solution de l'exercice 15, fournie à tout le monde. Photos réduites : trois largeurs (480, 960, 1600) de huit photos. Les images originales ne sont pas reprises |
| `servir.py`, `reservations.js` | Le serveur et le script du formulaire | Écrits pour le jour 2 à partir du `servir.py` de l'exercice 15 |
