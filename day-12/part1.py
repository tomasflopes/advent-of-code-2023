FILE = "input.txt"

def count(arrangement, nums):
    if arrangement == "":
        return 1 if len(nums) == 0 else 0

    if len(nums) == 0:
        return 0 if "#" in arrangement else 1

    sum = 0

    if arrangement[0] in ".?":
        sum += count(arrangement[1:], nums)

    n = nums[0]

    if arrangement[0] in "#?":
        if n <= len(arrangement) and "." not in arrangement[:n] and (n == len(arrangement) or arrangement[n] != "#"):
            sum += count(arrangement[n+1:], nums[1:])

    return sum

with open(FILE, "r") as file:
    lines = file.readlines()
    
    sum = 0
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        arrangement = line.split()[0] 
        numbers = line.split()[1].strip().split(",")
        numbers = [int(n) for n in numbers]

        res = count(arrangement, numbers)
        sum += res
    print(sum)
        
