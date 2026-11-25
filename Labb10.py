"""
Syntaxregler:

 <formel>::= <mol> \n
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...

"""

# Syntaxkontroll

from linkedQFile import LinkedQ
from molgrafik import *


periodic_table = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81,
    "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180,
    "Na": 22.990, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974,
    "S": 32.06, "Cl": 35.45, "Ar": 39.948, "K": 39.098, "Ca": 40.078,
    "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938,
    "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.630, "As": 74.922, "Se": 78.971, "Br": 79.904,
    "Kr": 83.798, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224,
    "Nb": 92.906, "Mo": 95.95, "Tc": 98.0, "Ru": 101.07, "Rh": 102.91,
    "Pd": 106.42, "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71,
    "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29, "Cs": 132.91,
    "Ba": 137.33, "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24,
    "Pm": 145.0, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93,
    "Dy": 162.50, "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.04,
    "Lu": 174.97, "Hf": 178.49, "Ta": 180.95, "W": 183.84, "Re": 186.21,
    "Os": 190.23, "Ir": 192.22, "Pt": 195.08, "Au": 196.97, "Hg": 200.59,
    "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Po": 209.0, "At": 210.0,
    "Rn": 222.0, "Fr": 223.0, "Ra": 226.0, "Ac": 227.0, "Th": 232.04,
    "Pa": 231.04, "U": 238.03, "Np": 237.0, "Pu": 244.0, "Am": 243.0,
    "Cm": 247.0, "Bk": 247.0, "Cf": 251.0, "Es": 252.0, "Fm": 257.0,
    "Md": 258.0, "No": 259.0, "Lr": 262.0, "Rf": 267.0, "Db": 270.0,
    "Sg": 271.0, "Bh": 270.0, "Hs": 277.0, "Mt": 278.0, "Ds": 281.0,
    "Rg": 282.0, "Cn": 285.0, "Nh": 286.0, "Fl": 289.0, "Mc": 290.0,
    "Lv": 293.0, "Ts": 294.0, "Og": 294.0
}


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

class Syntaxfel(Exception):
    pass

def weight(mol):
    molekylvikt = 0

    if mol is None:
        return molekylvikt

    if mol.down is not None: # om det finns en parantes / undergrupp
        atomvikt = weight(mol.down) # räkna molekylvikten för denna grupp
        molekylvikt += atomvikt * mol.num # lägg till detta

    elif mol.atom in periodic_table: # Om det inte är "()" dvs finns i periodiska systemet
        atomvikt = periodic_table[mol.atom] # plockar ut atomvikt
        molekylvikt += atomvikt * mol.num # Lägger till totala atomvikten till molekylvikten

    # När programmet kollat färdigt down grenen och atomgruppen så ska den gå vidare till höger.
    molekylvikt += weight(mol.next)

    return molekylvikt


def readFormel(teckenkö):
    mol = readMol(teckenkö)
    if teckenkö.peek() != ".": # Om första värdet ej börjar med "."
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    return mol

def readGroup(teckenkö):
    rutan = Ruta()
    if teckenkö.peek() == "(": # Om vi stöter på "("
        teckenkö.dequeue() # Tar bort "(" ur kön
        #readMol(teckenkö) # Läs molekylen efter "("
        rutan.down = readMol(teckenkö)

        if teckenkö.peek() != ")": # När readMol kmr tillbaka hit så checkar den att ")" finns.
            raise Syntaxfel("Saknad högerparentes vid radslutet")

        teckenkö.dequeue() # Tar bort ")" ur kön om finnes när readMol kommit tillbaka hit.

        if teckenkö.peek().isdigit(): # Värdet efter ")" måste vara en siffra.
            rutan.num = readNum(teckenkö)
        else:
            raise Syntaxfel("Saknad siffra vid radslutet")
        return rutan # Avsluta syntaxen.

    # Om gruppen ej börjar med parantes
    if teckenkö.peek() == "." or teckenkö.peek() == ")" or teckenkö.peek().isdigit(): # Om vår molekyl börjar med "." (dvs empty), ")" eller en siffra så kommer den gnälla
        raise Syntaxfel("Felaktig gruppstart vid radslutet")

    else: # Annars går
        rutan.atom = readAtom(teckenkö)
        if teckenkö.peek().isdigit(): # Om nästa värde är ett nummer
            rutan.num = readNum(teckenkö)
        return rutan



def readMol(teckenkö): # detta kan man kalla för "loop" starten. Den kör tills teckenkö är slut eller slutparantes.
    mol = readGroup(teckenkö)
    if teckenkö.peek() != "." and teckenkö.peek() != ")": # Om nästa värde är !"." eller ")" börja om att läsa molekylen.
        mol.next = readMol(teckenkö)
    return mol



def readAtom(teckenkö):

    Atom = readLETTER(teckenkö) # måste börja med stor bokstav, sparas i atom
    if teckenkö.peek().islower(): # Om liten bokstav nästa
        Atom += readletter(teckenkö) # lägg till i atom
    if Atom in periodic_table.keys(): # om atomen finns i periodiska systemet
        return Atom
    else: #Om ej i periodiska systemet:
        raise Syntaxfel("Okänd atom vid radslutet")


def readLETTER(teckenkö):
    if teckenkö.peek().isupper():
        return teckenkö.dequeue()
    raise Syntaxfel("Saknad stor bokstav vid radslutet")

def readletter(teckenkö):
    if teckenkö.peek().islower(): # kollar om tecknet är en liten bokstav
        return teckenkö.dequeue()
    raise Syntaxfel("Saknad stor bokstav vid radslutet")


def readNum(teckenkö):
    tecken = teckenkö.dequeue()
    if tecken == "0":
        raise Syntaxfel("För litet tal vid radslutet")

    while teckenkö.peek().isdigit() and teckenkö.peek() is not None:
        tecken += teckenkö.dequeue()

    if int(tecken) <= 1:
        raise Syntaxfel("För litet tal vid radslutet")

    return int(tecken)


def StoreMol(molekyl):
    teckenkö = LinkedQ()
    for tecken in molekyl:
        teckenkö.enqueue(tecken)
    teckenkö.enqueue(".")
    return teckenkö

def CheckSyntax(teckenkö):
    string = ""
    try:
        mol = readFormel(teckenkö)
        print("Formeln är syntastiskt korrekt")
        return mol
    except Syntaxfel as fel:
        while not teckenkö.isEmpty() and teckenkö.peek() != "." and teckenkö.peek() != "#":
            string += teckenkö.dequeue()
        if string == "": # om strängen e tom (vill ej ha mellanslag)
            return str(fel)
        else:
            return str(fel) + " " + string



def main():
    molekyl = input()
    while molekyl != "#":
        teckenkö = StoreMol(molekyl)
        mol = CheckSyntax(teckenkö)
        if isinstance(mol, Ruta):
            print("Molekylvikt: " + str(weight(mol)))
            mg = Molgrafik()
            mg.show(mol)
            molekyl = input()
        else:
            print(mol)
            molekyl = input()



if __name__ == "__main__":
    main()





