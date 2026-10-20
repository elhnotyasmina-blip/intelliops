import unittest
from src.extraction import masquer_secrets, normaliser, dedoublonner


class TestExtraction(unittest.TestCase):
    def test_masque_password(self):
        self.assertEqual(
            masquer_secrets("login ok password=abc123"),
            "login ok password=[SECRET]",
        )

    def test_masque_api_key(self):
        self.assertEqual(masquer_secrets("api_key: XYZ789"), "api_key: [SECRET]")

    def test_normaliser_masque_et_valeurs_par_defaut(self):
        e = normaliser({"message": "token=abc"})
        self.assertEqual(e.message, "token=[SECRET]")
        self.assertEqual(e.severite, "info")
        self.assertEqual(e.source, "inconnu")

    def test_dedoublonner(self):
        b = {"source": "s", "message": "m", "horodatage": "T1"}
        evts = [normaliser(b), normaliser(b), normaliser({**b, "horodatage": "T2"})]
        self.assertEqual(len(dedoublonner(evts)), 2)

    def test_bearer(self):
        self.assertEqual(
            masquer_secrets("Authorization: Bearer eyJ.abc-1"),
            "Authorization: Bearer [SECRET]",
        )


if __name__ == "__main__":
    unittest.main()

