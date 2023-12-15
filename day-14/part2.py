FILE = "input.txt"

directions = [(0,1), (1,0), (0,-1), (-1,0)]

def print_matrix(matrix):
    for line in matrix:
        for char in line:
            print(char, end="")
        print()


def tilt(rocks,n):
    for k in range(n):
        x,y = directions[k%4]

        for j in range(len(rocks[0])):
            for i in range(len(rocks)):
                rocks[i] = rocks[i].replace("O.",".O")


def get_sum(rocks):
    sum = 0

    for i in range(len(rocks)):
        for j in range(len(rocks[0])):
            if rocks[i][j] == "O":
                sum += len(rocks)-i

    return sum


with open(FILE, "r") as file:
    lines = file.readlines()
    rocks = []
    n = 4
    for line in lines:
        if line == "\n":
            continue
        else:
            rocks.append(line.strip())

    tilt(rocks, n)
    sum = get_sum(rocks)
    print_matrix(rocks)
    print(sum)


