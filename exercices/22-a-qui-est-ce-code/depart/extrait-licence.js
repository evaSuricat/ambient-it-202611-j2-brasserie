/*
 * validerCourriel.js
 * Copyright (c) 2019 Atelier Houblonnière (auteur fictif)
 * Licence GPL-3.0-or-later (licence réelle, attribution fictive pour l'exercice).
 * Toute redistribution, modifiée ou non, doit rester sous la même licence.
 */
function validerCourriel(texte) {
  if (typeof texte !== "string") return false;
  const propre = texte.trim();
  if (propre.length < 6 || propre.length > 254) return false;
  const arobase = propre.indexOf("@");
  if (arobase < 1 || arobase !== propre.lastIndexOf("@")) return false;
  const domaine = propre.slice(arobase + 1);
  if (!domaine.includes(".") || domaine.startsWith(".") || domaine.endsWith(".")) return false;
  return !/\s/.test(propre);
}
