FROM ubuntu:24.04
ARG JETON_DEPLOIEMENT=jeton-factice-pigala-0000-NE-PAS-UTILISER
ENV PIGALA_CLE=cle-factice-pigala-1111-NE-PAS-UTILISER
WORKDIR /app
COPY . .
RUN echo "Deploiement avec le jeton ${JETON_DEPLOIEMENT}" > /app/deploiement.log && rm secrets.env
CMD ["cat", "/app/app.py"]
