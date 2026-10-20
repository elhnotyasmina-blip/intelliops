"""Agent 3 : Notification (diffusion, validation humaine, trace des decisions)."""
from src.contrat import maintenant


def formater_message(evenement):
    return (f"[{evenement.severite.upper()}] "
            f"{evenement.source}/{evenement.type} : {evenement.message}")


def notifier(message, sortie=print):
    """Notification Teams simulee."""
    sortie(f"[Teams simule] {message}")
    return message


def demander_validation(action, input_fn=input):
    """Validation humaine : seule la reponse 'o' approuve."""
    reponse = input_fn(f"Valider l'action '{action}' ? (o/n) ")
    return reponse.strip().lower() == "o"


def tracer_decision(journal, action, approuvee):
    entree = {
        "horodatage": maintenant(),
        "action": action,
        "decision": "approuvee" if approuvee else "refusee",
    }
    journal.append(entree)
    return entree