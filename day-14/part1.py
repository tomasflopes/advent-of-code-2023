FILE = "input.txt"

def print_matrix(matrix):
    for line in matrix:
        for char in line:
            print(char, end="")
        print()


def tilt_north(rocks):
    for j in range(len(rocks[0])):
        for i in range(len(rocks)):
            if rocks[i][j] == "O":
                while i > 0 and rocks[i-1][j] == ".":
                    rocks[i][j] = "."
                    rocks[i-1][j] = "O"
                    i -= 1


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
    for line in lines:
        if line == "\n":
            continue
        else:
            rocks.append(list(line.strip()))

    tilt_north(rocks)
    print_matrix(rocks)
    sum = get_sum(rocks)
    print(sum)

