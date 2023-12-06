import math

FILE = "input.txt"

with open(FILE, 'r') as file:
    lines = file.readlines()
    seeds = lines[0].split(':')[1].strip().split()

    mapped = False
    lowest = math.inf


    for seed in seeds:
        mapped_val = int(seed)
        for line in lines[2:]:
            line = line.strip()
            if line.endswith(':') or line == '':
                mapped = False
                continue
            if mapped:
                continue

            [source, destination, r] = line.split()
            source = int(source)
            destination = int(destination)
            r = int(r)
            seed = int(seed)

            if mapped_val < destination + r and mapped_val >= destination:
                mapped_val = (source - destination) + mapped_val
                mapped = True

        if mapped_val < lowest:
            lowest = mapped_val

print(lowest)
