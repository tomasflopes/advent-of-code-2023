FILE = "input.txt"

with open(FILE, "r") as file:
    line = file.readline()
    sum = 0
    for step in line.strip().split(","):
        res = 0
        for c in step:
            res += ord(c)
            res*=17
            res %= 256

        sum += res

    print(sum)


