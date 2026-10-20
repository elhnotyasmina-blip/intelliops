import unittest
from src.contrat import Evenement


class TestContrat(unittest.TestCase):
    def test_creation_valide(self):
        e = Evenement("jenkins", "build", "echec du build", "erreur")
        self.assertEqual(e.source, "jenkins")
        self.assertEqual(e.severite, "erreur")

    def test_severite_invalide(self):
        with self.assertRaises(ValueError):
            Evenement("x", "y", "msg", "tres-grave")

    def test_aller_retour_dict(self):
        e = Evenement("k8s", "pod", "CrashLoopBackOff", "erreur", "2026-01-01T10:00:00")
        self.assertEqual(Evenement.from_dict(e.to_dict()), e)


if __name__ == "__main__":
    unittest.main()