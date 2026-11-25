import unittest
from Labb9 import *

"""
Na
H2O
Si(C3(COOH)2)4(H2O)7
Na332
#
"""

class SyntaxTest(unittest.TestCase):

    def test_correct_syntax(self):
        """ Testar korrekt syntax """
        self.assertEqual(CheckSyntax(StoreMol("Na")), "Formeln är syntaktiskt korrekt")

    def test_correct_syntax2(self):
        """ Testar korrekt syntax """
        self.assertEqual(CheckSyntax(StoreMol("H2O")), "Formeln är syntaktiskt korrekt")

    def test_correct_syntax3(self):
        """ Testar korrekt syntax """
        self.assertEqual(CheckSyntax(StoreMol("Si(C3(COOH)2)4(H2O)7")), "Formeln är syntaktiskt korrekt")

    def test_incorrect_syntax1(self):
        self.assertEqual(CheckSyntax(StoreMol("C(Xx4)5")), "Okänd atom vid radslutet 4)5")

    def test_incorrect_syntax2(self):
        self.assertEqual(CheckSyntax(StoreMol("C(OH4)C")), "Saknad siffra vid radslutet C")

    def test_incorrect_syntax3(self):
        self.assertEqual(CheckSyntax(StoreMol("C(OH4C")), "Saknad högerparentes vid radslutet")

    def test_incorrect_syntax4(self):
        self.assertEqual(CheckSyntax(StoreMol("H2O)Fe")), "Felaktig gruppstart vid radslutet )Fe")

    def test_incorrect_syntax5(self):
        self.assertEqual(CheckSyntax(StoreMol("H0")), "För litet tal vid radslutet")

    def test_incorrect_syntax6(self):
        self.assertEqual(CheckSyntax(StoreMol("H1C")), "För litet tal vid radslutet C")

    def test_incorrect_syntax7(self):
        self.assertEqual(CheckSyntax(StoreMol("H02C")), "För litet tal vid radslutet 2C")

    def test_incorrect_syntax8(self):
        self.assertEqual(CheckSyntax(StoreMol("Nacl")), "Saknad stor bokstav vid radslutet cl")

    def test_incorrect_syntax9(self):
        self.assertEqual(CheckSyntax(StoreMol("a")), "Saknad stor bokstav vid radslutet a")

    def test_incorrect_syntax10(self):
        self.assertEqual(CheckSyntax(StoreMol("(Cl)2)3")), "Felaktig gruppstart vid radslutet )3")

    def test_incorrect_syntax11(self):
        self.assertEqual(CheckSyntax(StoreMol(")")), "Felaktig gruppstart vid radslutet )")

    def test_incorrect_syntax12(self):
        self.assertEqual(CheckSyntax(StoreMol("2")), "Felaktig gruppstart vid radslutet 2")


if __name__ == '__main__':
    unittest.main()