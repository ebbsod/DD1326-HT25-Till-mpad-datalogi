import linkedQFile as lq

queue = lq.LinkedQ() # Skapar ny kö
#kort = input("Skriv in några kortvärden (med mellanslag mellan):").split()
kort = input().split() # Här kan man lägga in input från kattis

# Köar alla nummer som las in i kort
for num in kort:
    queue.enqueue(num)


# Skapar en tom kö som är "kortbordet"
table = lq.LinkedQ()

# Kör tills break
while True:
    while not queue.isEmpty():
        # Ta första kortet och lägg längst bak i kön
        queue.enqueue(queue.dequeue())

        # Ta nästa kort och lägg på bordet
        if not queue.isEmpty():
            card = queue.dequeue() # sparar kort samtidigt som en försvinner från kön
            table.enqueue(card) # lägger kortet på bordet

    # Om kön är tom så slutar loopen
    if queue.isEmpty():
        break

while not table.isEmpty(): # Printar vårt bord när kön inte är tom.
    print(table.dequeue(), end=' ')

#3 1 4 2 5



