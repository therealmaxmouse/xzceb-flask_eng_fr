import unittest

from translator import english_to_french, french_to_english

class TestEntoFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test translation
        self.assertIsNotNone(english_to_french('Hello'))

class TestFrtoEn(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test translation
        self.assertIsNotNone(french_to_english('Bonjour'))

unittest.main()