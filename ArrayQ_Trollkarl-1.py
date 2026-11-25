import ArrayQFile as ArrayQ

queue = ArrayQ.ArrayQ() # Skapar kö
kort = input("Skriv in några nummer (med mellanslag mellan):").split() # kattis input

# Lägger alla kort från inputen i vår kö
for num in kort:
    queue.enqueue(int(num))


table = ArrayQ.ArrayQ() # Skapar bordet vi lägger ut korten på

# Kör loop tills break
while True:
    while not queue.isEmpty():
        # Ta första kortet och lägg längst bak i kön
        queue.enqueue(queue.dequeue())

        # Ta nästa kort och lägg på bordet
        if not queue.isEmpty():
            card = queue.dequeue() # Sparar datan som tas bort från kön
            table.enqueue(card) # Köar detta till bordet

    # Slutar programmet när kön är tom
    if queue.isEmpty():
        break

while not table.isEmpty(): # Printar vårt bord när kön inte är tom.
    print(table.dequeue(), end=' ')



