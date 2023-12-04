FILE = "input.txt"


with open(FILE, 'r') as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        line = line.split(':')[1].strip()
        winning = line.split("|")[0].strip().split()
        numbers = line.split("|")[1].strip().split()
        card_worth = 0.5
        for n in numbers:
            if n in winning:
                card_worth *= 2
        if card_worth == 0.5:
            card_worth = 0
        sum += card_worth

print(sum)
            
                
