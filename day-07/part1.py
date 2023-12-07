from functools import cmp_to_key

FILE = "input.txt"


def cmp_card(c1, c2):
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    return order.index(c1) - order.index(c2) 


def get_occurences(hand):
    return {c: hand.count(c) for c in hand}


def sort_hands(c1, c2):
    c1_occ = get_occurences(c1)
    c2_occ = get_occurences(c2)

    if not len(c1_occ) == len(c2_occ):
        return len(c2_occ) - len(c1_occ)

    greatest_c1 = max(c1_occ.values())
    greatest_c2 = max(c2_occ.values())

    if len(c1_occ) == 2 or len(c1_occ) == 3:
        if not greatest_c1 == greatest_c2:
            return greatest_c1 - greatest_c2

    # for now on we can assume that both hands are 'tied'
    for i in range(len(c1)):
        if not cmp_card(c1[i], c2[i]) == 0:
            return cmp_card(c2[i], c1[i])

    return 0


with open(FILE, "r") as file:
    lines = file.readlines()
    hands = []
    dict = {}
    for line in lines:
        hand = line.strip().split()[0].strip()
        hands.append(hand)
        rank = line.strip().split()[1].strip()
        dict.update({hand: rank})

    hands.sort(key=cmp_to_key(sort_hands))

    sum = 0
    for i in range(len(hands)):
        sum += int(dict[hands[i]]) * (i + 1)
    print(sum)
