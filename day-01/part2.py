FILE = "input.txt"

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open(FILE, 'r') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        n = ""
        i = 0
        for c in line:
            if c.isnumeric():
                n += c
            else:
                for k in numbers.keys():
                    if k == line[i:i+len(k)]:
                        n += str(numbers[k])
                        break
            i+=1


        sum += int(n[0]+n[-1])

    print(sum)


