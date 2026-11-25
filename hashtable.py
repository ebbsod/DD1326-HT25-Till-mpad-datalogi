import csv

class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key = "", data = None):
        """key är nyckeln som anvands vid hashningen
        data är det objekt som ska hashas in"""
        self.key = key
        self.data = data

    #Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.total_collision = 0
        self.max_collision = 0

    def store(self,key,data):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = HashNode(key, data)

        else:
            if self.slots[hashvalue].key == key: # if key with same name already exists
                self.slots[hashvalue].data = data  # replace data
            else:
                attempt = 1
                nextslot = rehash(hashvalue, self.size,attempt)
                while attempt < self.size and self.slots[nextslot] != None and self.slots[nextslot].key != key:
                    attempt += 1
                    nextslot = rehash(nextslot, self.size, attempt)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = HashNode(key, data)
                else:
                    self.slots[nextslot].data = data # replace


            self.total_collision += attempt
            if attempt > self.max_collision:
                self.max_collision = attempt

    def search(self,key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        attempt = 1
        while attempt < self.size and self.slots[position] != None and not found and not stop:
            if self.slots[position].key == key:
                found = True
                data = self.slots[position].data
            else:
                attempt += 1
                position = rehash(position, self.size, attempt)
                if position == startslot:
                    stop = True
        if data != None:
            return data
        else:
            raise KeyError(key)

    def hashfunction(self, key):
        """key är nyckeln
           Beräknar hashfunktionen för key"""
        return hash2(key) % self.size




def hash2(key):             # Beräknar hashkoden för en sträng key enligt
    result = 0            # key[0]*32n-1 + key[1]*32n-2 + ... + key[n-1]
    for c in key:
        result = result*32 + ord(c)
    return result

def rehash(oldhash, size, attempt):
    return (oldhash + 1) % size

"""def rehash(oldhash,size,attempt):
    return (oldhash + attempt ** 2) % size"""


""" Test 1 - kdrama fil """

class Drama:
    def __init__(self, drama):
        self.name = drama[0]
        self.rating = float(drama[1])
        self.actors = drama[2]
        self.viewship_rate = float(drama[3])
        self.genre = drama[4]
        self.director = drama[5]
        self.writer = drama[6]
        self.year = int(drama[7])
        self.no_episodes = int(drama[8])
        self.network = drama[9]

    def __str__(self):
        return self.name + " (" + str(self.year) + ")"

    def __lt__(self,other):
        return self.rating < other.rating

    def high_rating(self):
        return self.rating > 7.5

    def genre_str(self):
        print("genre: " + self.genre)

def create_object_dict():
    object_dict = Hashtable(540)
    with open("kdrama.csv", mode="r") as dramafile:
        csv_file = csv.reader(dramafile, delimiter=',')
        next(csv_file)
        for row in csv_file:
            drama = Drama(row)
            object_dict.store(row[0], drama)
        return object_dict

drama = create_object_dict()
print(drama.search("The Heirs"))
print(f"{drama.max_collision} max collisions for input with most collisions")
print(f"{drama.total_collision} total collisions")