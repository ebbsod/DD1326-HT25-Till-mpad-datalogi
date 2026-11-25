"""
Syntaxregler:

   <molekyl> ::= <atom> | <atom><num>
      <atom>  ::= <LETTER> | <LETTER><letter>
      <LETTER>::= A | B | C | ... | Z
      <letter>::= a | b | c | ... | z
      <num>   ::= 2 | 3 | 4 | ...
"""

# Syntaxkontroll

from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass

def läsMolekyl(teckenkö):
    läsOrdning(teckenkö) # läser in
    if teckenkö.peek() == ".": # Om nästa värde är "."
        teckenkö.dequeue() # Tar bort tecken i vår linkedQ
    else:
        if teckenkö.peek().isdigit(): # Om nästa värde är ett nummer
            läsNum(teckenkö)
        läsMolekyl(teckenkö)

def läsOrdning(teckenkö):
    läsBOKSTAV(teckenkö) # måste börja med stor bokstav
    if teckenkö.peek().islower(): # Om liten bokstav nästa
        läsbokstav(teckenkö)
    if teckenkö.peek().isdigit(): # Om nr nästa
        läsNum(teckenkö)


def läsBOKSTAV(teckenkö):
    if teckenkö.peek().isupper():
        return teckenkö.dequeue()
    raise Syntaxfel("Saknad stor bokstav vid radslutet")

def läsbokstav(teckenkö):
    if teckenkö.peek().islower(): # kollar om tecknet är en liten bokstav
        return teckenkö.dequeue()
    raise Syntaxfel("Saknad stor bokstav vid radslutet")


def läsNum(teckenkö):
    tecken = teckenkö.dequeue()
    if tecken == "0":
        raise Syntaxfel("För litet tal vid radslutet")

    while teckenkö.peek().isdigit() and teckenkö.peek() is not None:
        tecken += teckenkö.dequeue()

    if int(tecken) <= 1:
        raise Syntaxfel("För litet tal vid radslutet")


def helmolekyl(teckenkö):
    while not teckenkö.isEmpty():
        tecken = teckenkö.dequeue()
        return tecken


def lagraMolekyl(molekyl):
    teckenkö = LinkedQ()
    for tecken in molekyl:
        teckenkö.enqueue(tecken)
    teckenkö.enqueue(".")
    return teckenkö

def kollaGrammatiken(teckenkö):
    string = ""
    try:
        läsMolekyl(teckenkö)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        while not teckenkö.isEmpty() and teckenkö.peek() != "." and teckenkö.peek() != "#":
            string += teckenkö.dequeue()
        return str(fel) + " " + str(string)

def main():
    molekyl = input()
    while molekyl != "#":
        teckenkö = lagraMolekyl(molekyl)
        resultat = kollaGrammatiken(teckenkö)
        print(resultat)
        molekyl = input()

if __name__ == "__main__":
    main()





