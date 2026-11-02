// Envoie le formulaire de réservation à /api/reservations.
// Contrat avec la page : un <form id="form-reservation"> dont les champs ont pour attribut name
// nom, telephone, email, date, couverts, commentaire, et un élément #reservation-message
// (role="status") qui reçoit le message pour le client.
(function () {
  "use strict";

  const formulaire = document.getElementById("form-reservation");
  const message = document.getElementById("reservation-message");
  if (!formulaire || !message) return;

  function afficher(texte, erreur) {
    message.textContent = texte;
    message.classList.toggle("reservation-erreur", Boolean(erreur));
  }

  formulaire.addEventListener("submit", async function (evenement) {
    evenement.preventDefault();
    const champs = new FormData(formulaire);
    const donnees = {
      nom: champs.get("nom"),
      telephone: champs.get("telephone"),
      email: champs.get("email"),
      date: champs.get("date"),
      couverts: Number(champs.get("couverts")),
      commentaire: champs.get("commentaire"),
    };
    afficher("Envoi en cours…", false);
    try {
      const reponse = await fetch("/api/reservations", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(donnees),
      });
      if (!reponse.ok) throw new Error("Réponse " + reponse.status);
      const resultat = await reponse.json();
      formulaire.reset();
      afficher("Votre demande est enregistrée (numéro " + resultat.id + ").", false);
    } catch (e) {
      console.error(e);
      afficher("Votre demande n'a pas pu être envoyée. Appelez le 01 23 45 67 89.", true);
    }
  });
})();
