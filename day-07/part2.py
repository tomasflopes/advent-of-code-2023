from functools import cmp_to_key

FILE = "input.txt"


def cmp_card(c1, c2):
    order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    order.index(c1)
    order.index(c2)

    if order.index(c1) - order.index(c2) > 0:
        return 1
    elif order.index(c1) - order.index(c2) < 0:
        return -1
    return 0


def get_occurences(hand):
    return {c: hand.count(c) for c in hand}


def get_j_occurences(hand):
    return hand.count("J")


def sort_hands(c1, c2):
    c1_occ = get_occurences(c1)
    c2_occ = get_occurences(c2)
    j1 = 1 if "J" in c1_occ else 0
    j2 = 1 if "J" in c2_occ else 0

    print("j1: " + str(j1))
    print("j2: " + str(j2))

    j1_len = len(c1_occ) - j1
    j2_len = len(c2_occ) - j2

    if j1_len > j2_len:
        return -1
    if j1_len < j2_len:
        return 1

    c1_j_occ = get_j_occurences(c1)
    c2_j_occ = get_j_occurences(c2)

    greatest_c1 = max(c1_occ.values()) + c1_j_occ
    greatest_c2 = max(c2_occ.values()) + c2_j_occ

    if j1_len == 2 or j1_len == 3:
        if greatest_c1 > greatest_c2:
            return 1
        if greatest_c1 < greatest_c2:
            return -1

    # for now on we can assume that both hands are 'tied'
    for i in range(len(c1)):
        if cmp_card(c1[i], c2[i]) > 0:
            return -1
        elif cmp_card(c1[i], c2[i]) < 0:
            return 1

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

    print("Before " + str(hands))
    hands.sort(key=cmp_to_key(sort_hands))
    print("After " + str(hands))

    sum = 0
    for i in range(len(hands)):
        sum += int(dict[hands[i]]) * (i + 1)
    print(sum)
