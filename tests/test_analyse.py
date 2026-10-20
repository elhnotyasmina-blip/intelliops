import unittest
from src.contrat import Evenement
from src.analyse import filtrer, classifier, proposer_actions


def evt(msg, sev, h="T"):
    return Evenement("src", "t", msg, sev, h)


class TestAnalyse(unittest.TestCase):
    def test_filtrer_par_severite(self):
        evts = [evt("a", "info"), evt("b", "erreur")]
        self.assertEqual([e.message for e in filtrer(evts, "warning")], ["b"])

    def test_classifier_boucle_erreurs(self):
        evts = [evt("crash", "erreur", f"T{i}") for i in range(3)]
        self.assertIn("boucle_erreurs", classifier(evts))

    def test_classifier_pas_de_boucle_sous_le_seuil(self):
        evts = [evt("crash", "erreur", f"T{i}") for i in range(2)]
        self.assertNotIn("boucle_erreurs", classifier(evts))

    def test_classifier_critique(self):
        self.assertIn("critique", classifier([evt("CVE", "critique")]))

    def test_classifier_normal(self):
        self.assertEqual(classifier([evt("ok", "info")]), ["normal"])

    def test_proposer_actions(self):
        self.assertEqual(len(proposer_actions(["boucle_erreurs", "critique"])), 2)
        self.assertEqual(proposer_actions(["normal"]), [])


if __name__ == "__main__":
    unittest.main()
