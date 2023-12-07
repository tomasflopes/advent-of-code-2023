from math import log10, ceil
from datetime import datetime


def apply_maps(maps, seed):
    pre_map = seed
    for m in maps:
        for ds, ss, rl in m:
            if ss <= pre_map < ss + rl:
                pre_map = ds + (pre_map - ss)
                break
    return pre_map


def parse(seed_ranges=False):
    seeds = [int(x) for x in dat[0].split(": ")[1].strip().split(" ")]

    if seed_ranges:
        seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

    maps = []
    curr_map = []
    for d in dat[3:]:
        if d == "":
            continue
        if ":" in d:
            maps += [curr_map]
            curr_map = []
        else:
            curr_map += [tuple(int(x) for x in d.split(" "))]

    maps += [curr_map]

    return seeds, maps


with open("input.txt") as f:
    dat = [x.strip("\n") for x in f.readlines()]

    seeds, maps = parse(seed_ranges=True)

    step = int(pow(10, ceil(log10(max(s[1] for s in seeds) / 100))))
    search_vals = {
        (ss, ss + sl, s): apply_maps(maps, s)
        for ss, sl in seeds
        for s in range(ss, ss + sl, step)
    }
    estimates = min(search_vals.items(), key=lambda x: x[1])

    start, end, best_est = estimates[0]
    now = datetime.now()

    print(f"Best estimate: {best_est} in seed range {start} to {end}")
    print(f"Step size: {step}, estimate: {best_est}")

    while step > 1:
        l = max(best_est - step, start)
        r = min(best_est + step, end)

        step = step // 10
        search_vals = {s: apply_maps(maps, s) for s in range(l, r, step)}
        best_est, best = min(search_vals.items(), key=lambda x: x[1])

        print(f"Step size: {step:<8d}, estimate: {best_est}")

    print(f"Time taken: {(datetime.now() - now).total_seconds():.4f}s")
    print("res=", best)
