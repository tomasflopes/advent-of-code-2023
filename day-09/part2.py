FILE = "input.txt"


def first_diff(numbers):
    if len(set(numbers)) == 1 and numbers[0] == 0:
        return 0

    diffs = []
    for i in range(len(numbers) - 1):
        diffs.append(numbers[i + 1] - numbers[i])

    return numbers[0] - first_diff(diffs)


with open(FILE, "r") as file:
    lines = file.readlines()

    sum = 0
    for line in lines:
        line = line.strip()
        numbers = line.split()
        numbers = [int(number) for number in numbers]
        difference = first_diff(numbers)
        sum += difference

    print(sum)
