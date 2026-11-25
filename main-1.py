from bintreeFile import Bintree
from linkedQFile import LinkedQ

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet not in svenska:
            svenska.put(ordet)             # in i sökträdet

gamla = Bintree()
q = LinkedQ()

startord = input("startord:")
slutord = input("slutord:")

def writechain(node):
    if node.parent != None:
        writechain(node.parent)
    print(node.word)


def makechildren(q, node):
    alfabetet = "abcdefghijklmnopqrstuvwxyzåäö"
    for bokstav in alfabetet:
        ord1 = bokstav + node.word[1:]
        ord2 = node.word[0] + bokstav + node.word[2]
        ord3 = node.word[0:2] + bokstav
        ordlista = [ord1, ord2, ord3]
        for ord in ordlista:
            if ord in svenska and ord not in gamla:
                ny_node = ParentNode(ord, node)
                q.enqueue(ny_node)
                gamla.put(ord)
                if ord == slutord:
                    writechain(ny_node)
                    print("det finns en väg till", ny_node.word)
                    return True
    return False

q.enqueue(ParentNode(startord, None))
gamla.put(startord)

slutord_finns = False

while not q.isEmpty() and slutord_finns is False:
    node = q.dequeue()
    slutord_finns = makechildren(q, node)
if slutord_finns is False:
    print("Det finns ingen väg till slutordet.")