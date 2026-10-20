"""Contrat d'echange commun aux trois agents."""
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

SEVERITES = ("info", "warning", "erreur", "critique")


def maintenant():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass(frozen=True)
class Evenement:
    source: str
    type: str
    message: str
    severite: str = "info"
    horodatage: str = field(default_factory=maintenant)

    def __post_init__(self):
        if self.severite not in SEVERITES:
            raise ValueError(f"severite invalide : {self.severite}")
        if not self.message:
            raise ValueError("message vide")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)