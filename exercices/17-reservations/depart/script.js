// Remplit la carte depuis /api/carte. Sans serveur, le contenu du <noscript> reste la référence.
(async function () {
  const listes = {
    biere: document.querySelector('[data-categorie="biere"]'),
    plat: document.querySelector('[data-categorie="plat"]'),
  };
  if (!listes.biere || !listes.plat) return;

  try {
    const reponse = await fetch("/api/carte");
    if (!reponse.ok) throw new Error("Réponse " + reponse.status);
    const carte = await reponse.json();
    const euros = new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" });

    for (const ligne of carte) {
      const liste = listes[ligne.categorie];
      if (!liste) continue;
      const li = document.createElement("li");
      li.innerHTML =
        '<span class="nom"></span><span class="desc"></span><span class="prix"></span>';
      li.querySelector(".nom").textContent = ligne.nom;
      li.querySelector(".desc").textContent = ligne.description;
      li.querySelector(".prix").textContent = euros.format(ligne.prix);
      liste.appendChild(li);
    }
  } catch (erreur) {
    const message = document.createElement("p");
    message.className = "attente";
    message.textContent = "La carte n'a pas pu être chargée. Demandez-la au comptoir.";
    listes.biere.before(message);
  }
})();
