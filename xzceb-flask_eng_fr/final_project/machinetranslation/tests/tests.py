import unittest
from translator import frenchToEnglish, englishToFrench

class Test_frenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('0'),('0'))
        self.assertEqual(frenchToEnglish('Hello'),('Bonjour'))
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('0'),('0'))
        self.assertEqual(englishToFrench('Bonjour'),('Hello'))
        