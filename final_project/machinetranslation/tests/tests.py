import unittest
from ..translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test_etf_hello_notequal_emptystring(self):
        self.assertNotEqual(english_to_french("Hello"), "")

    def test_etf_hello_equal_bonjour(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_fte_bonjour_notequal_emptystring(self):
        self.assertNotEqual(french_to_english("Bonjour"), "")

    def test_fte_bonjour_equal_hello(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()
