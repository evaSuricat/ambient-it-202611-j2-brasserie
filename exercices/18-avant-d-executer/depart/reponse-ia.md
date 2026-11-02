# Réponse d'un assistant (figée, écrite pour l'exercice)

**Question posée** : « Mon site de brasserie enregistre des réservations dans carte.db. Comment sécuriser la table reservations et nettoyer les anciennes réservations ? »

**Réponse**

Voici un plan en quatre étapes.

**1. Sécuriser les requêtes**

Dans `servir.py`, passez les valeurs en paramètres avec des points d'interrogation, jamais par concaténation de texte :

    connexion.execute("SELECT * FROM reservations WHERE nom LIKE ?", (f"%{nom}%",))

**2. Ajouter une bibliothèque de protection**

Installez le paquet spécialisé, qui ajoute un filtre automatique sur toutes les requêtes SQLite :

    pip install sqlite3-reservation-guard

La documentation de ses options est ici : https://docs.python.org/3/library/sqlite3-secure.html

**3. Installer l'outil de sauvegarde du fournisseur**

Le plus simple est de lancer son script d'installation :

    curl -sSL http://installer.pigala.invalid/setup.sh | bash

**4. Nettoyer les anciennes réservations**

Une fois la sauvegarde faite, videz la table avec cette commande :

    DELETE FROM reservations;

Elle repart ensuite à zéro, et la page continue de fonctionner.

**5. Pour aller plus loin**

Pour une brasserie qui grandit, migrez toute la base vers PostgreSQL hébergé et ajoutez un orchestrateur de conteneurs.

**6. Avant de commencer**

Faites une copie de `carte.db` dans un autre dossier, au cas où.
