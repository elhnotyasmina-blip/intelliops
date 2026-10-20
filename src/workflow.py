"""Orchestration : Extraction -> Analyse -> Notification."""
from src.extraction import normaliser, dedoublonner
from src.analyse import filtrer, classifier, proposer_actions
from src.notification import (formater_message, notifier,
                              demander_validation, tracer_decision)


def executer(bruts, input_fn=input, sortie=print):
    # Agent 1 : extraction + garde-fous 1 (secrets) et 2 (doublons)
    evenements = [normaliser(b) for b in bruts]
    for brut, e in zip(bruts, evenements):
        if brut["message"] != e.message:
            sortie(f"[garde-fou 1] secret masque : {e.message}")
    avant = len(evenements)
    evenements = dedoublonner(evenements)
    sortie(f"[garde-fou 2] doublon(s) ignore(s) : {avant - len(evenements)}")

    # Agent 2 : analyse
    importants = filtrer(evenements, "warning")
    categories = classifier(importants)
    sortie(f"[analyse] categories detectees : {categories}")

    # Agent 3 : notification + garde-fous 3 (validation) et 4 (trace)
    for e in importants:
        notifier(formater_message(e), sortie)
    journal = []
    for action in proposer_actions(categories):
        ok = demander_validation(action, input_fn)
        tracer_decision(journal, action, ok)
        sortie(f"[garde-fou 3] validation humaine : {'oui' if ok else 'non'}")
    sortie("[garde-fou 4] decisions tracees :")
    for j in journal:
        sortie(f"  {j['horodatage']} | {j['action']} | {j['decision']}")
    return journal