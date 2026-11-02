# Sources de l'exercice 20

| Fichier | Origine |
|---|---|
| `Dockerfile`, `app.py`, `secrets.env` | Écrits pour la formation. Le jeton de `secrets.env` et celui du `Dockerfile` sont de faux jetons visiblement faux (« jeton-factice-pigala-0000-NE-PAS-UTILISER »), qui ne donnent accès à rien |
| `reservations.csv` | Les 30 réservations fictives de l'exercice 17 |
| `historique-docker.txt` | Sortie réelle de `docker history --no-trunc --format "{{.CreatedBy}}" pigala-demo:fuite`, relevée le 02/11/2026 (Docker 25.0.3), image construite à partir de `ubuntu:24.04` avec ce `Dockerfile` |
| `preuve-couches.txt` | Relevé fait le 02/11/2026 en lisant les couches de la même image |
| Documentation | [Build secrets](https://docs.docker.com/build/building/secrets/), [Dockerfile](https://docs.docker.com/reference/dockerfile/), [image history](https://docs.docker.com/reference/cli/docker/image/history/) |
