class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None # Skapar en tom rot

    def put(self, newvalue):
        self.root = putta(self.root, newvalue) # lägger in värden i trädet

    def __contains__(self, value):
        return finns(self.root, value)

    def write(self):
        skriv(self.root)
        print("\n")

def putta(p, newdata):
    if p is None:
        return Node(newdata)
    elif newdata < p.data:
        p.left = putta(p.left, newdata)
    elif newdata > p.data:
        p.right = putta(p.right, newdata)
    return p

def finns(p, value):
    if p is None:
        return False
    if p.data == value:
        return True
    elif value < p.data:
        return finns(p.left, value)
    else:
        return finns(p.right, value)

def skriv(p):
    if p is not None:
        skriv(p.left)
        print(p.data, end=' ')  # print all nodes on one line
        skriv(p.right)
