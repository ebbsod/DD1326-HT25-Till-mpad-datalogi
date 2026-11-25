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


periodic_table = ("H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr"
                  "Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd)"
                  "In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf"
                  "Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm"
                  "Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv").split()


class Syntaxfel(Exception):
    pass

def readFormel(teckenkö):
    readMol(teckenkö)
    if teckenkö.peek() != ".": # Om första värdet ej börjar med "."
        raise Syntaxfel("Felaktig gruppstart vid radslutet")

def readGroup(teckenkö):
    if teckenkö.peek() == "(": # Om vi stöter på "("
        teckenkö.dequeue() # Tar bort "(" ur kön
        readMol(teckenkö) # Läs molekylen efter "("

        if teckenkö.peek() != ")": # När readMol kmr tillbaka hit så checkar den att ")" finns.
            raise Syntaxfel("Saknad högerparentes vid radslutet")

        teckenkö.dequeue() # Tar bort ")" ur kön om finnes när readMol kommit tillbaka hit.

        if teckenkö.peek().isdigit(): # Värdet efter ")" måste vara en siffra.
            readNum(teckenkö)
        else:
            raise Syntaxfel("Saknad siffra vid radslutet")
        return # Avsluta syntaxen.


    # Om gruppen ej börjar med parantes
    if teckenkö.peek() == "." or teckenkö.peek() == ")" or teckenkö.peek().isdigit(): # Om vår molekyl börjar med "." (dvs empty), ")" eller en siffra så kommer den gnälla
        raise Syntaxfel("Felaktig gruppstart vid radslutet")

    else: # Annars går
        readAtom(teckenkö)
        if teckenkö.peek().isdigit(): # Om nästa värde är ett nummer
            readNum(teckenkö)




def readMol(teckenkö): # detta kan man kalla för "loop" starten. Den kör tills teckenkö är slut eller slutparantes.
    readGroup(teckenkö)
    if teckenkö.peek() != "." and teckenkö.peek() != ")": # Om nästa värde är !"." eller ")" börja om att läsa molekylen.
        readMol(teckenkö)



def readAtom(teckenkö):

    Atom = readLETTER(teckenkö) # måste börja med stor bokstav, sparas i atom
    if teckenkö.peek().islower(): # Om liten bokstav nästa
        Atom += readletter(teckenkö) # lägg till i atom
    if Atom in periodic_table: # om atomen finns i periodiska systemet
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


def StoreMol(molekyl):
    teckenkö = LinkedQ()
    for tecken in molekyl:
        teckenkö.enqueue(tecken)
    teckenkö.enqueue(".")
    return teckenkö

def CheckSyntax(teckenkö):
    string = ""
    try:
        readFormel(teckenkö)
        return "Formeln är syntaktiskt korrekt"
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
        resultat = CheckSyntax(teckenkö)
        print(resultat)
        molekyl = input()

if __name__ == "__main__":
    main()





