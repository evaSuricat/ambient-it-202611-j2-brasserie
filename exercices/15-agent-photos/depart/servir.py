"""Sert ce dossier en local, sans cache, et répond sur /api/carte avec la carte en JSON.

    python servir.py          # http://127.0.0.1:8000/
    python servir.py 8001     # autre port

Sans cache : à chaque rechargement, Chrome relit le disque, on voit ses modifications
tout de suite. Ctrl+C pour arrêter.
"""
import http.server
import json
import os
import sqlite3
import sys

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


class Serveur(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] == "/api/carte":
            corps = json.dumps(lire_carte(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)
            return
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Serveur) as serveur:
        print(f"Le Pigala sur http://127.0.0.1:{PORT}/  (Ctrl+C pour arrêter)")
        serveur.serve_forever()
