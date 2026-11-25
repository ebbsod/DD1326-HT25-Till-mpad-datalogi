import timeit

def binary_search(the_list, key):
  left = 0
  right = len(the_list) - 1

  while left <= right:
    mid = (left + right) // 2 # mitten av listan

    if the_list[mid] == key: # returnerar det man söker om det finns i mitten
      return key

    if the_list[mid] < key: # halverar listan och kollar bara högra halvan om det man söker är större än mitten
      left = mid + 1
    else:
      right = mid - 1 # behåller annars vänstra delen

def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal: # jämför med det sökta värdet
      return arr[i] # returnerar om det är samma

def build_hash_table(items):
  table = {} # skapar en tom dictionary
  for item in items:
    table[item] = True  # värdet kan vara vad som helst, t.ex. True
  return table

def search_hash_table(table, query):
  return query in table # tar fram nyckeln i en dictionary

def bubbelsortera(data):
  n = len(data)
  bytt = True
  while bytt:
    bytt = False
    for i in range(n - 1):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        bytt = True

def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)


def qsort(data, low, high):
  pivotindex = (low + high) // 2
  # flytta pivot till kanten
  data[pivotindex], data[high] = data[high], data[pivotindex]

  # damerna först med avseende på pivotdata
  pivotmid = partitionera(data, low - 1, high, data[high])

  # flytta tillbaka pivot
  data[pivotmid], data[high] = data[high], data[pivotmid]

  if pivotmid - low > 1:
    qsort(data, low, pivotmid - 1)
  if high - pivotmid > 1:
    qsort(data, pivotmid + 1, high)


def partitionera(data, v, h, pivot):
  while True:
    v = v + 1
    while data[v] < pivot:
      v = v + 1
    h = h - 1
    while h != 0 and data[h] > pivot:
      h = h - 1
    data[v], data[h] = data[h], data[v]
    if v >= h:
      break
  data[v], data[h] = data[h], data[v]
  return v

class Song:
  def __init__(self,trackid,låtid,artistnamn,låttitel):
    self.trackid = trackid
    self.låtid = låtid
    self.artistnamn = artistnamn
    self.låttitel = låttitel

  def __lt__(self, other):
    return self.artistnamn < other.artistnamn # jämförelse sker efter artistnamn

  def __str__(self):
    return self.trackid + " " + self.låtid + self.artistnamn + self.låttitel # för att enkelt kunna testa att inläsning funkar

def readfile(filename):
  object_list = [] # tom lista till objekten
  with open(filename,mode="r",encoding="utf-8") as text_file:
    for line in text_file: # läser in rad för rad
      song_list = line.strip().split("<SEP>") # tar bort tomma rader och gör till en lista
      object_list.append(Song(song_list[0],song_list[1],song_list[2],song_list[3])) # skapar objektet och lägger in i listan
    return object_list



"""def main():
  filename = "unique_tracks.txt"

  lista = readfile(filename)
  #lista.sort() # används för binärsökning

  n = len(lista)
  print("Antal element =", n)

  objekt = lista[5000] # det sökta objektet
  testartist = objekt.artistnamn

  kort_lista = lista[0:500000] # när bara delar av listan ska användas
  table = build_hash_table(kort_lista) # används för sökning i hashtabbel

  linjtid = timeit.timeit(stmt=lambda: search_hash_table(table,objekt), number=10000)
  print("Linjärsökningen tog", round(linjtid, 4), "sekunder")"""



list = readfile("unique_tracks.txt")
short_list = list[0:1000000]
linjtid = timeit.timeit(stmt=lambda:quicksort(short_list), number=1)
print("Sorteringen tog", round(linjtid, 4), "sekunder")



