import csv

class DictHash(object):
    def __init__(self):
        self.hash = {}

    def store(self, nyckel, data):
        self.hash[nyckel] = data

    def search(self, nyckel):
        if nyckel in self.hash:
            return self.hash[nyckel]
        else:
            raise KeyError(nyckel)

    def __contains__(self, nyckel):
        return nyckel in self.hash


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
    object_dict = DictHash()
    with open("kdrama.csv", mode="r") as dramafile:
        csv_file = csv.reader(dramafile, delimiter=',')
        next(csv_file)
        for row in csv_file:
            drama = Drama(row)
            object_dict.store(row[0], drama)
        return object_dict

drama = create_object_dict()
print(drama.search("The Heirs"))
