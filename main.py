from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet not in svenska:
            svenska.put(ordet)             # in i sökträdet


gamla = Bintree()

startord = input("startord:")
slutord = input("slutord:")

def makechildren(startord):
    alfabetet = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla.put(startord)

    for bokstav in alfabetet:
        första_ord = bokstav + startord[1:] # kollar på bokstaven och de två sista bokstäverna i startordet
        andra_ord = startord[0] + bokstav + startord[2] # kollar på första bokstaven av start ord, bokstaven i alfabetet samt den sista bokstaven i startordet
        tredje_ord = startord[0] + startord[1] + bokstav # kollar på första & andra bokstaven i startord tillsammans med bokstaven i alfabetet
        ordlista = [första_ord, andra_ord, tredje_ord] # lägger in kombinationen i en lista
        for ord in ordlista: # går igenom de tre kombinationerna
            if ord in svenska and ord not in gamla: # om ordet finns i vår svenska lista, men ej i gamla
                gamla.put(ord) # lägg till ordet till vår gamla träd
                print(ord)


q = LinkedQ()

def makechildren2(q, word, slutord):
    alfabetet = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla.put(word)
    for bokstav in alfabetet:
        ord1 = bokstav + word[1:]
        ord2 = word[0] + bokstav + word[2]
        ord3 = word[0] + word[1]  + bokstav
        ordlista = [ord1, ord2, ord3]
        for ord in ordlista:
            if ord in svenska and ord not in gamla:
                if ord == slutord:
                    print ("Det finns en väg till " + slutord)
                    return True
                q.enqueue(ord)
                gamla.put(ord)


q.enqueue(startord)

while not q.isEmpty():
    word = q.dequeue()
    slutord_finns = makechildren2(q, word, slutord)
    if slutord_finns:
        break
if not slutord_finns:
    print("Det finns ingen väg till slutordet.")