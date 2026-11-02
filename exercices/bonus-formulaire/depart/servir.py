"""Sert la page du Pigala en local, sans cache. Répond sur /api/carte (la carte en JSON)
et reçoit les réservations en POST sur /api/reservations.

    python servir.py          # http://127.0.0.1:8000/
    python servir.py 8001     # autre port

Ce qui est servi : une liste blanche de fichiers (page, feuilles de style, scripts, photos).
Le reste, base de données et code compris, répond 404. Les réservations vivent dans
donnees/reservations.db : le serveur ne sait que les ajouter. Pour les consulter, le
gérant lance gerant.py sur le poste, sans passer par le réseau.

Ctrl+C pour arrêter.
"""
import http.server
import json
import os
import posixpath
import re
import sqlite3
import sys
from datetime import date as jour
from urllib.parse import unquote, urlparse

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DOSSIER = os.path.dirname(os.path.abspath(__file__))
CARTE = os.path.join(DOSSIER, "carte.db")
RESERVATIONS = os.path.join(DOSSIER, "donnees", "reservations.db")
os.chdir(DOSSIER)

# Liste blanche : ces fichiers à la racine, plus les feuilles de css/ et les images de photos/.
FICHIERS_RACINE = {"index.html", "style.css", "script.js", "reservations.js"}
EXTENSIONS_IMAGES = {".jpg", ".jpeg", ".png", ".webp", ".svg"}
TAILLE_MAX_CORPS = 10_000


def est_public(chemin):
    """Vrai si ce chemin d'URL fait partie de la liste blanche."""
    propre = posixpath.normpath(unquote(chemin)).lstrip("/")
    if propre in ("", "."):
        return True
    if propre.startswith("..") or "\\" in propre:
        return False
    if propre in FICHIERS_RACINE:
        return True
    dossier, _, reste = propre.partition("/")
    extension = posixpath.splitext(reste)[1].lower()
    if dossier == "css":
        return extension == ".css" and "/" not in reste
    if dossier == "photos":
        return extension in EXTENSIONS_IMAGES
    return False


def lire_carte():
    # Lecture seule : cette connexion ne peut rien modifier.
    with sqlite3.connect(f"file:{CARTE}?mode=ro", uri=True) as connexion:
        connexion.row_factory = sqlite3.Row
        lignes = connexion.execute(
            "SELECT categorie, nom, description, prix FROM carte ORDER BY categorie, nom"
        ).fetchall()
    return [dict(l) for l in lignes]


def valider(donnees):
    """Renvoie les champs nettoyés, ou lève ValueError (message sans détail technique)."""
    if not isinstance(donnees, dict):
        raise ValueError("Requête invalide.")
    nom = str(donnees.get("nom", "")).strip()
    telephone = str(donnees.get("telephone", "")).strip()
    email = str(donnees.get("email", "")).strip()
    commentaire = str(donnees.get("commentaire", "")).strip()
    if not 1 <= len(nom) <= 100:
        raise ValueError("Nom invalide.")
    if telephone and not re.fullmatch(r"[0-9 +().-]{6,25}", telephone):
        raise ValueError("Téléphone invalide.")
    if email and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise ValueError("Courriel invalide.")
    if len(email) > 200 or len(commentaire) > 500:
        raise ValueError("Texte trop long.")
    try:
        jour.fromisoformat(str(donnees.get("date")))
        couverts = int(donnees.get("couverts"))
    except (TypeError, ValueError):
        raise ValueError("Date ou nombre de personnes invalide.")
    if not 1 <= couverts <= 12:
        raise ValueError("Nombre de personnes invalide.")
    return nom, telephone, email, str(donnees["date"]), couverts, commentaire


def enregistrer_reservation(champs):
    with sqlite3.connect(RESERVATIONS) as connexion:
        curseur = connexion.execute(
            "INSERT INTO reservations (nom, telephone, email, date, couverts, commentaire, cree_le) "
            "VALUES (?, ?, ?, ?, ?, ?, datetime('now'))",
            champs,
        )
        return curseur.lastrowid


class Serveur(http.server.SimpleHTTPRequestHandler):
    def repondre_json(self, statut, contenu):
        corps = json.dumps(contenu, ensure_ascii=False).encode("utf-8")
        self.send_response(statut)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def do_GET(self):
        chemin = urlparse(self.path).path
        if chemin == "/api/carte":
            self.repondre_json(200, lire_carte())
        elif chemin.startswith("/api/") or not est_public(chemin):
            self.send_error(404)
        else:
            super().do_GET()

    def do_HEAD(self):
        if not est_public(urlparse(self.path).path):
            self.send_error(404)
        else:
            super().do_HEAD()

    def do_POST(self):
        if urlparse(self.path).path != "/api/reservations":
            self.send_error(404)
            return
        try:
            longueur = int(self.headers.get("Content-Length", 0))
            if not 0 < longueur <= TAILLE_MAX_CORPS:
                raise ValueError("Requête invalide.")
            champs = valider(json.loads(self.rfile.read(longueur)))
            numero = enregistrer_reservation(champs)
        except (ValueError, sqlite3.Error) as erreur:
            # Le détail technique reste dans le terminal du serveur, jamais dans la réponse.
            print("Réservation refusée :", type(erreur).__name__, file=sys.stderr)
            self.repondre_json(400, {"erreur": "Requête invalide."})
            return
        self.repondre_json(201, {"id": numero})

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()


if __name__ == "__main__":
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Serveur) as serveur:
        print(f"Le Pigala sur http://127.0.0.1:{PORT}/  (Ctrl+C pour arrêter)")
        try:
            serveur.serve_forever()
        except KeyboardInterrupt:
            print("\nServeur arrêté.")
