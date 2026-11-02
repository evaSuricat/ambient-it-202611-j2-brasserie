# Sources de l'exercice 24

| Fichier | Origine |
|---|---|
| `user-story.md` | Écrite pour la formation, fictive |
| `historique.csv` | 120 demandes de réservation inventées pour septembre et octobre 2026. **Les codes postaux 99001 à 99004 n'existent pas** : ils ne désignent aucune commune réelle et ne stigmatisent aucun territoire. Les absences sont fixées zone par zone et créneau par créneau pour que le calcul soit reproductible. Le taux d'absence plus élevé des zones 99003 et 99004 vient en partie de ce qu'elles réservent surtout des dîners tardifs (créneau où l'on s'absente le plus pour tout le monde) et en partie de la distance : le calcul permet de le voir |
| `calcul.py` | Écrit pour la formation, bibliothèque standard seulement |
| Décisions automatisées | [RGPD, article 22](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679), EUR-Lex, règlement 2016/679, lu le 02/11/2026. Paragraphe 1 : « droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire ». Paragraphe 2 : exceptions (contrat, droit de l'Union ou de l'État membre, consentement). L'exercice ne dit pas que l'article s'applique au Pigala |
| Biais des algorithmes | [Défenseur des droits avec la CNIL, Algorithmes : prévenir l'automatisation des discriminations](https://www.defenseurdesdroits.fr/fr/rapports/2020/05/algorithmes-prevenir-lautomatisation-des-discriminations) : rapport daté du 31/05/2020 sur la page (une autre source donne le 22/06/2020) |
| Injection par un champ libre | [OWASP Top 10 LLM 2025](https://genai.owasp.org/llm-top-10/), liste LLM01 à LLM10 ; le commentaire de la réservation numéro 15 (`ressources/reservations.csv`) en est l'exemple |
