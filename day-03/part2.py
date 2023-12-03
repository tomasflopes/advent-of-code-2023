FILE = "input.txt"


def is_valid(lines, i, start, j):
    res = []
    for k in range(i - 1, i + 2):
        if k < 0 or k >= len(lines):
            continue
        for l in range(start - 1, j + 1):
            if l < 0 or l >= len(lines[k]):
                continue
            if lines[k][l] == "*":
                res.append((k, l))

    if res == []:
        return False
    return res


with open(FILE, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    sum = 0
    i = 0
    j = 0
    gears = {}
    start = 0
    n = ""
    for line in lines:
        n = ""
        j = 0
        start = -1
        for c in line:
            if c.isnumeric():
                if start == -1:
                    start = j
                n += c
            else:
                if not n == "":
                    res = is_valid(lines, i, start, j)
                    if res:
                        print("valid", i, j, n)

                        for r in res:
                            if gears.get(r) is None:
                                gears.update({r: []})
                            gears[r].append(n)

                start = -1
                n = ""
            j += 1
        if not n == "":
            res = is_valid(lines, i, start, j)
            if res:
                print("valid", i, j, n)

                for r in res:
                    if gears.get(r) is None:
                        gears.update({r: []})
                    gears[r].append(n)
        i += 1

    for gear in gears:
        print("gear", gear, gears[gear])
        if len(gears[gear]) == 2:
            sum += int(gears[gear][0]) * int(gears[gear][1])

print(sum)

