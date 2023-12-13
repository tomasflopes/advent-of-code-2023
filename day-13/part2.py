FILE = "input.txt"

def reflection_column(pattern):
    for j in range(len(pattern[0])):
        c = 0
        for k in range(min(j+1, len(pattern[0])-j-1)):
            for i in range(len(pattern)):
                if pattern[i][j-k] != pattern[i][j+k+1]:
                    c+=1

        if c == 1:
            if j == len(pattern[0]) - 1:
                return -1
            return j +1

    
    return -1

def reflection_row(pattern):
    for i in range(len(pattern)):
        c = 0
        for k in range(min(i+1, len(pattern)-i-1)):
            for j in range(len(pattern[0])):
                if pattern[i-k][j] != pattern[i+k+1][j]:
                    c+=1

        if c == 1:
            if i == len(pattern) - 1:
                return -1
            return i + 1

    return -1

with open(FILE, "r") as file:
    lines = file.readlines()
    patterns = []

    p = []
    for line in lines:
        if line == "\n":
            patterns.append(p)
            p = []
        else:
            p.append(line.strip())

    patterns.append(p)


    sum = 0
    for (i,pattern) in enumerate(patterns):
        row = reflection_row(pattern)
        col = reflection_column(pattern)

        if col == -1:
            col = 0
        if row == -1:
            row = 0
        else:
            row*=100

        print("Row: {}, Col: {}".format(row,col))

        sum+= col+row


    print("Sum:",sum)

