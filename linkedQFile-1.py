class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def isEmpty(self):
        return self.__first is None

    def enqueue(self, data):
        node = Node(data)
        # Om det ej finns någon data i kön:
        if self.__last is None:
            self.__first = node #första platsen går till denna
            self.__last = node # sista platsen är också detta värde

        # Om det finns grejer i kön
        else:
            self.__last.next = node # Sista noden pekar mot nästa objekt
            self.__last = node # Sista noden blir den nya noden

    def dequeue(self):
        # Finns inget i kön att tömma:
        if self.isEmpty():
            return None

        # Skapar en variabel som ska spara datan:
        removed = self.__first.data

        # Flyttar första värdet till nästa i kön
        self.__first = self.__first.next

        # Om kön då töms när detta händer:
        if self.__first is None:
            self.__last = None # Sista objektet sätts också som tom då.
        return removed



