
from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

english = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as englishfil:
    for rad in englishfil:
        rad = rad.strip()
        word = rad.split()
        for ord in word:
            if ord in english:
                pass
            else:
                if ord in svenska:
                    print(ord, end = " ")
                english.put(ord)






