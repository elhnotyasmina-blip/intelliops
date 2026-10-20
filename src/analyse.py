"""Agent 2 : Analyse (filtrage, classification, propositions d'actions)."""
from collections import Counter
from src.contrat import SEVERITES

ACTIONS = {
    "boucle_erreurs": "Redemarrer le conteneur en boucle d'erreurs",
    "critique": "Isoler l'image signalee comme vulnerable",
}


def filtrer(evenements, severite_min="warning"):
    """Garde les evenements dont la severite est >= severite_min."""
    seuil = SEVERITES.index(severite_min)
    return [e for e in evenements if SEVERITES.index(e.severite) >= seuil]


def classifier(evenements):
    """Retourne la liste des categories detectees (ou ['normal'])."""
    categories = []
    erreurs = Counter(e.message for e in evenements if e.severite == "erreur")
    if any(n > 100 for n in erreurs.values()):
        categories.append("boucle_erreurs")
    if any(e.severite == "critique" for e in evenements):
        categories.append("critique")
    return categories or ["normal"]


def proposer_actions(categories):
    """Une action sensible a valider par categorie detectee."""
    return [ACTIONS[c] for c in categories if c in ACTIONS]