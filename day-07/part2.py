from functools import cmp_to_key

FILE = "input.txt"


def cmp_card(c1, c2):
    order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    return order.index(c1) - order.index(c2)


def get_occurences(hand):
    return {c: hand.count(c) for c in hand}


def get_j_occurences(hand):
    return hand.count("J")


def sort_hands(c1, c2):
    c1_occ = get_occurences(c1)
    c2_occ = get_occurences(c2)
    j1 = 1 if "J" in c1_occ else 0
    j2 = 1 if "J" in c2_occ else 0

    j1_len = max(1, len(c1_occ) - j1)
    j2_len = max(1, len(c2_occ) - j2)

    if not j1_len == j2_len:
        return j2_len - j1_len

    c1_j_occ = get_j_occurences(c1)
    c2_j_occ = get_j_occurences(c2)

    c1_without_j = {c: c1_occ[c] for c in c1_occ if not c == "J"}
    c2_without_j = {c: c2_occ[c] for c in c2_occ if not c == "J"}

    max_c1 = 1 if len(c1_without_j) == 0 else max(1, max(c1_without_j.values()))
    max_c2 = 1 if len(c2_without_j) == 0 else max(1, max(c2_without_j.values()))

    greatest_c1 = max_c1 + c1_j_occ
    greatest_c2 = max_c2 + c2_j_occ

    if j1_len == 2 or j1_len == 3:
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
