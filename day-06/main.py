FILE = "input.txt"

with open(FILE, "r") as file:
    lines = file.readlines()
    times = lines[0].split(":")[1].strip().split()
    distances = lines[1].split(":")[1].strip().split()

    i = 0
    res = 1
    for time in times:
        time = int(time)
        distance = int(distances[i])
        win = 0
        for j in range(time):
            if j * (time - j) > distance:
                win += 1
        res *= win
        i += 1

    print(res)
