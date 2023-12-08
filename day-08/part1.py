FILE = "input.txt"

with open(FILE, "r") as file:
    lines = file.readlines()

    instructions = lines[0].strip()

    lines = lines[2:]
    dict = {}

    for line in lines:
        line = line.strip()
        if line == '':
            continue
        source = line.split()[0].strip()
        left = line.split()[2].split('(')[1].split(',')[0].strip()
        right = line.split()[3].split(')')[0].strip()
        dict.update({ source: {"L": left, "R": right} })

    current = dict.get('AAA')
    steps = 0
    while True:
        c = instructions[steps % len(instructions)]
        steps += 1

        if current.get(c) == 'ZZZ':
            print(steps)
            break
        current = dict.get(current.get(c))



