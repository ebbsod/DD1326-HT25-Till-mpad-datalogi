class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def search(p, data):
    while True:
        if p == None:
            return True
        if p.data == data:
            return True
        if p.data > data:
            p = p.left
        if data < p.data:
            p = p.right

def amount(p):
    if p == None:
        return 0
    else:
        return 1 + amount(p.left) + amount(p.right)

def exist(p, data):
    if p == None:
        return False
    if p.data == data:
        return True
    if p.data > data:
        return exist(p.left, data)
    if p.data < data:
        return exist(p.right, data)

def inorder(p):
    if p != None:
        inorder(p.left)
        print(p.data)
        inorder(p.right)

def preorder(p):
    if p != None:
        print(p.data)
        preorder(p.left)
        preorder(p.right)

def postorder(p):
    if p != None:
        postorder(p.left)
        postorder(p.right)
        print(p.data)


root = Node(50)
root.left = Node(80)
root.right = Node(25)
root.left.right = Node(35)

inorder(root)
postorder(root)
preorder(root)