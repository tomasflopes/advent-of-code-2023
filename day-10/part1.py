FILE = "input.txt"

directions = {
    "D": {"J": "L", "|": "D", "L": "R"},
    "U": {"7": "L", "|": "U", "F": "R"},
    "R": {"J": "U", "-": "R", "7": "D"},
    "L": {"L": "U", "-": "L", "F": "D"},
}
increments = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

with open(FILE, "r") as file:
    lines = file.readlines()
    map = []
    start = (None, None)
    i = 0
    for line in lines:
        j = 0
        if line.strip() == "":
            continue
        ll = []
        for c in line.strip():
            ll.append(c)
            if c == "S":
                start = (i, j)
            j += 1
        i += 1
        map.append(ll)

    cur = start
    cur_direction = ""
    count = 1

    for dir in directions:
        y, x = cur
        dy, dx = increments[dir]
        if map[y + dy][x + dx] in directions[dir]:
            cur_direction = dir

    while cur != start or count == 1:
        y, x = cur
        dy, dx = increments[cur_direction]
        if map[y + dy][x + dx] == "S" and count > 1:
            break
        cur = (y + dy, x + dx)
        cur_direction = directions[cur_direction][map[y + dy][x + dx]]
        count += 1

    # the furthest point is half the perimeter
    print("Perimeter:", count)
    print("res=", count // 2)
