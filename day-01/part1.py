FILE = "input.txt"

with open(FILE, 'r') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        n = ""
        for c in line:
            if c.isnumeric():
                n += c

        sum += int(n[0]+n[-1])

    print(sum)


