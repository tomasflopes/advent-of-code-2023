import math
import threading 
import concurrent.futures

FILE = "input.txt"

lowest = math.inf

def work(start,end,lines):
    global lowest

    print("Start ", threading.current_thread().name)

    for seed in range(start, end,5):
        mapped = False

        mapped_val = int(seed)
        for line in lines[2:]:
            line = line.strip()
            if line.endswith(':') or line == '':
                mapped = False
                continue
            if mapped:
                continue

            [source, destination, r] = line.split()
            source = int(source)
            destination = int(destination)
            r = int(r)

            if mapped_val < destination + r and mapped_val >= destination:
                mapped_val = (source - destination) + mapped_val
                mapped = True

        if mapped_val < lowest:
            lowest = mapped_val
            print(lowest)

    print("Done ", threading.current_thread().name)


with open(FILE, 'r') as file:
    lines = file.readlines()
    seeds = lines[0].split(':')[1].strip().split()
    
    threads = []
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    N_THREADS = 10

    for i in range(0, len(seeds), 2):
        start = int(seeds[i])
        end = start + int(seeds[i+1]) + 1
        for i in range(N_THREADS):
            r = end - start
            print("start ", start + i * (r // N_THREADS), "end ", start + (i + 1) * (r // N_THREADS))
            pool.submit(work, start + i * (r // N_THREADS), start + (i + 1) * (r // N_THREADS), lines)

     
    pool.shutdown(wait=True)


    
    print(lowest)

