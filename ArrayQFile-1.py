from array import array

class ArrayQ:
    def __init__(self):
        self.__items = array('i', [])

    def __str__(self):
        return str(list(self.__items))

    # Lägger till data i vår array sist i ledet
    def enqueue(self, item):
        self.__items.append(item)

    # Tar bort det första datan i vår array
    def dequeue(self):
        return self.__items.pop(0)

    # Längden på kön
    def size(self):
        return len(self.__items)

    # Om det är 0 data i kön så ska programmet returnera True
    def isEmpty(self):
        return self.size() == 0


q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
x = q.dequeue()
y = q.dequeue()

if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")