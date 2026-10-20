"""Agent 1 : Extraction (collecte, normalisation, masquage, dedoublonnage)."""
import re
from src.contrat import Evenement

_MOTIF_BEARER = re.compile(r"(?i)(\bAuthorization\s*:\s*Bearer\s+)\S+")
_MOTIF_CLE = re.compile(
    r"(?i)\b(password|passwd|pwd|token|api[_-]?key|secret)\b(\s*[=:]\s*)\S+"
)


def masquer_secrets(texte):
    """Remplace les valeurs de secrets par [SECRET]."""
    texte = _MOTIF_CLE.sub(r"\1\2[SECRET]", texte)
    texte = _MOTIF_BEARER.sub(r"\1[SECRET]", texte)
    return texte


def normaliser(brut):
    """Transforme un dict brut en Evenement, secrets masques."""
    champs = {
        "source": brut.get("source", "inconnu"),
        "type": brut.get("type", "generique"),
        "message": masquer_secrets(brut["message"]),
        "severite": brut.get("severite", "info"),
    }
    if "horodatage" in brut:
        champs["horodatage"] = brut["horodatage"]
    return Evenement(**champs)


def dedoublonner(evenements):
    """Supprime les doublons exacts (meme source, type, message, horodatage)."""
    vus, resultat = set(), []
    for e in evenements:
        cle = (e.source, e.type, e.message, e.horodatage)
        if cle not in vus:
            vus.add(cle)
            resultat.append(e)
    return resultat