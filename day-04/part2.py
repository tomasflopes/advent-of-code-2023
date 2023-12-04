FILE = "input.txt"

cards = []
winnings = []

with open(FILE, 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        cards.append(1)
    i = 0

    for line in lines:
        line = line.split(':')[1].strip()
        winning = line.split("|")[0].strip().split()
        numbers = line.split("|")[1].strip().split()
        w = 0

        for n in numbers:
            if n in winning:
                w+=1
        winnings.append(w)


        i += 1

    for i in range(len(lines)):
        for j in range(winnings[i]):
            cards[i+j+1] += cards[i]

print(cards)
print(sum(cards))
print(winnings)

