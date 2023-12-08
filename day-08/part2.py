FILE = "input.txt"


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(numbers):
    for i in range(len(numbers) - 1):
        divisor = gcd(numbers[i], numbers[i + 1])
        numbers[i + 1] = (numbers[i] * numbers[i + 1]) // divisor

    return numbers[-1]


with open(FILE, "r") as file:
    lines = file.readlines()

    instructions = lines[0].strip()

    lines = lines[2:]
    dict = {}

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        source = line.split()[0].strip()
        left = line.split()[2].split("(")[1].split(",")[0].strip()
        right = line.split()[3].split(")")[0].strip()
        dict.update({source: {"L": left, "R": right}})

    current = []

    for k in dict.keys():
        if k.endswith("A"):
            current.append(dict.get(k))

    steps = 0
    found = [0] * len(current)
    while True:
        for i, cur in enumerate(current):
            if found[i] > 0:
                continue
            c = instructions[steps % len(instructions)]
            if cur.get(c).endswith("Z"):
                found[i] = steps + 1
                continue
            current[i] = dict.get(cur.get(c))

        steps += 1
        if all([f > 0 for f in found]):
            break

    # LCM just assumes that cycles are independent (for some reason in all inputs they are :) )
    print(found)
    print(lcm(found))
