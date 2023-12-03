FILE = "input.txt"


def is_valid(lines, i, start, j):
    for k in range(i - 1, i + 2):
        if k < 0 or k >= len(lines):
            continue
        for l in range(start - 1, j + 1):
            if l < 0 or l >= len(lines[k]):
                continue
            if not lines[k][l] == "" and not lines[k][l].isnumeric() and not lines[k][l] == ".":
                return True

    return False


with open(FILE, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    sum = 0
    i = 0
    j = 0
    start = 0
    n = ""
    for line in lines:
        if not n == "":
            if is_valid(lines, i, start, j):
                print("valid", i, j, n)
                sum += int(n)
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
                    if is_valid(lines, i, start, j):
                        print("valid", i, j, n)
                        sum += int(n)
                start = -1
                n = ""
            j += 1
        i += 1

print(sum)
