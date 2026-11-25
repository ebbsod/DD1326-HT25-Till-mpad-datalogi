import unittest
from Labb8 import *


class SyntaxTest(unittest.TestCase):

    def test_correct_syntax(self):
        """ Testar korrekt syntax """
        self.assertEqual(kollaGrammatiken(lagraMolekyl("H2O")), "Formeln är syntaktiskt korrekt")

    def test_smallNo(self):
        """ Testar inkorrekt syntax: felaktigt nr """
        self.assertEqual(kollaGrammatiken(lagraMolekyl("H02")),"För litet tal vid radslutet 2" )

    def test_lowercaseFirst(self):
        """ Testar korrekt syntax: liten bokstav före stor """
        self.assertEqual(kollaGrammatiken(lagraMolekyl("hH2")), "Saknad stor bokstav vid radslutet hH2")


if __name__ == '__main__':
    unittest.main()