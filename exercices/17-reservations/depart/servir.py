"""Sert ce dossier en local, sans cache. Répond sur /api/carte (la carte en JSON)
et sur /api/reservations (enregistrer une réservation, chercher une réservation).

    python servir.py          # http://127.0.0.1:8000/
    python servir.py 8001     # autre port

Ctrl+C pour arrêter.
"""
import http.server
import json
import os
import sqlite3
import sys
from urllib.parse import parse_qs, urlparse

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DOSSIER = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(DOSSIER, "carte.db")
os.chdir(DOSSIER)


def lire_carte():
    with sqlite3.connect(DB) as connexion:
        connexion.row_factory = sqlite3.Row
        lignes = connexion.execute(
            "SELECT categorie, nom, description, prix FROM carte ORDER BY categorie, nom"
        ).fetchall()
    return [dict(l) for l in lignes]


def enregistrer_reservation(donnees):
    """Ajoute une réservation et renvoie son numéro."""
    with sqlite3.connect(DB) as connexion:
        curseur = connexion.execute(
            "INSERT INTO reservations (nom, telephone, email, date, couverts, commentaire, cree_le) "
            "VALUES (?, ?, ?, ?, ?, ?, datetime('now'))",
            (
                donnees.get("nom"),
                donnees.get("telephone", ""),
                donnees.get("email", ""),
                donnees.get("date"),
                int(donnees.get("couverts")),
                donnees.get("commentaire", ""),
            ),
        )
        return curseur.lastrowid


def chercher_reservations(nom):
    """Recherche pour le gérant : toutes les réservations dont le nom contient le texte donné."""
    requete = (
        "SELECT id, nom, telephone, email, date, couverts, commentaire "
        "FROM reservations WHERE nom LIKE '%" + nom + "%' ORDER BY date"
    )
    with sqlite3.connect(DB) as connexion:
        connexion.row_factory = sqlite3.Row
        return [dict(l) for l in connexion.execute(requete).fetchall()]


class Serveur(http.server.SimpleHTTPRequestHandler):
    def repondre_json(self, statut, contenu):
        corps = json.dumps(contenu, ensure_ascii=False).encode("utf-8")
        self.send_response(statut)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def do_GET(self):
        adresse = urlparse(self.path)
        if adresse.path == "/api/carte":
            self.repondre_json(200, lire_carte())
        elif adresse.path == "/api/reservations":
            nom = parse_qs(adresse.query).get("nom", [""])[0]
            try:
                self.repondre_json(200, chercher_reservations(nom))
            except sqlite3.Error as erreur:
                self.repondre_json(500, {"erreur": str(erreur)})
        else:
            super().do_GET()

    def do_POST(self):
        if urlparse(self.path).path != "/api/reservations":
            self.send_error(404)
            return
        try:
            longueur = int(self.headers.get("Content-Length", 0))
            donnees = json.loads(self.rfile.read(longueur))
            if not donnees.get("nom") or not donnees.get("date"):
                raise ValueError("nom et date obligatoires")
            numero = enregistrer_reservation(donnees)
        except (ValueError, TypeError, sqlite3.Error) as erreur:
            self.repondre_json(400, {"erreur": str(erreur)})
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
