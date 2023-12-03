FILE = "input.txt"

sum = 0

with open(FILE, 'r') as file:
    lines = file.readlines()

    for line in lines:
        id = line.split(":")[0].strip().split()[1]
        line = line.split(":")[1].strip()
        draws = line.split(";")
        valid = True
        for d in draws:
            balls = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            d = d.strip().split(",")
            for game in d:
                game = game.split()
                balls[game[1].strip()] += int(game[0].strip())

            if(balls["red"] >  12 or balls["green"] > 13 or balls["blue"] > 14):
                valid = False

        if(valid):
            sum += int(id)


print(sum)
