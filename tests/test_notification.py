import unittest
from src.contrat import Evenement
from src.notification import (
    formater_message,
    notifier,
    demander_validation,
    tracer_decision,
)


class TestNotification(unittest.TestCase):
    def test_formater_message(self):
        e = Evenement("jenkins", "build", "echec", "erreur")
        self.assertEqual(formater_message(e), "[ERREUR] jenkins/build : echec")

    def test_validation_oui(self):
        self.assertTrue(demander_validation("x", input_fn=lambda _: " O "))

    def test_validation_non(self):
        self.assertFalse(demander_validation("x", input_fn=lambda _: "n"))
        self.assertFalse(demander_validation("x", input_fn=lambda _: ""))

    def test_tracer_decision(self):
        journal = []
        tracer_decision(journal, "redemarrer", True)
        tracer_decision(journal, "isoler", False)
        self.assertEqual([j["decision"] for j in journal], ["approuvee", "refusee"])

    def test_notifier(self):
        sorties = []
        notifier("hello", sortie=sorties.append)
        self.assertEqual(sorties, ["[Teams simule] hello"])


if __name__ == "__main__":
    unittest.main()
