FILE = "input.txt"

def print_matrix(matrix):
    for row in matrix:
        print("".join(row))

    print()

def transpose_matrix(matrix):
    m = []

    for i in range(len(matrix[0])):
        m.append([])
        for j in range(len(matrix)):
            m[i].append(matrix[j][i])

    return m

def insert_dup_lines(matrix):
    m = []
    for i in range(len(matrix)):
        line = matrix[i]
        if set(line) == set(["."]):
            m.append(line)
        m.append(line)
    return m

def get_galaxies(matrix):
    d = {}
    n = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "#":
                d[(i,j)] = n
                n+=1

    return d


with open(FILE, "r") as file:
    lines = file.readlines()
    map = []

    for line in lines:
        ll = []
        if line.strip() == "":
            continue
        for c in line.strip():
            ll.append(c)
        map.append(ll)

    map = insert_dup_lines(map)
    map = transpose_matrix(map)
    map = insert_dup_lines(map)
    map = transpose_matrix(map)


    gal = get_galaxies(map)

    sum = 0
    keys = list(gal.keys())
    i = 1
    for k in gal.keys():
        for ki in keys[i:]:
            distance = abs(k[0] - ki[0]) + abs(k[1] - ki[1])
#            print("Distance between {} {} and {} {} is {}".format(gal[k], k, gal[ki], ki, distance))
            sum += distance
        i+=1

    print(sum)

