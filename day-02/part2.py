FILE = "input.txt"

sum = 0

with open(FILE, 'r') as file:
    lines = file.readlines()

    for line in lines:
        id = line.split(":")[0].strip().split()[1]
        line = line.split(":")[1].strip()
        draws = line.split(";")
        balls = {
            "red":0,
            "green": 0,
            "blue": 0,
        }
        for d in draws:
            d = d.strip().split(",")
            for game in d:
                game = game.split()
                key = game[1].strip()
                val = int(game[0].strip())
                if val > balls[key]:
                    balls[key] = val
        print(balls)
        power = balls["red"] * balls["green"] * balls["blue"]
        print("id: {}, power: {}".format(id, power))
        sum += power


print(sum)
