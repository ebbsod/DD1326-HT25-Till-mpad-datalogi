import csv

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

def class_test():
    drama1 = Drama(["name1","7.4","actor1","2","genre1","director1","writer1","2001","23","network1"])
    drama2 = Drama(["name2","8","actor2","9.1","genre2","director2","writer2","2000","100","network2"])

    print(drama1)
    print(drama1<drama2)
    print(drama2.high_rating())
    drama1.genre_str()

def print_file():
    with open("kdrama.csv", mode="r") as dramafile:
        csv_file = csv.reader(dramafile, delimiter=",")
        #next(csv_file)
        for line in csv_file:
            for part in line:
                print(part, end=" ")
            print()

def create_object_list():
    object_list = []
    with open("kdrama.csv", mode="r") as dramafile:
        csv_file = csv.reader(dramafile, delimiter=",")
        next(csv_file)
        for line in csv_file:
            #if len(line) == 10:
                drama = Drama(line)
                object_list.append(drama)
        return object_list

def find_lowest_rating(object_list):
    min = 10
    for drama in object_list:
        if drama.rating < min:
            min = drama.rating
            min_drama = drama
    return min_drama

print(find_lowest_rating(create_object_list()))


