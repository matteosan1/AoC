import time, sys
from operator import itemgetter

from utils import readInput

def loadInput():
    lines = readInput("input_5.txt")
    data = {}
    label = None
    for l in lines:
        if l.startswith("seeds:"):
            data.update({"seed":list(map(int, l.split("seeds:")[1].split()))})
        else:
            if l.endswith("map:"):
                label = tuple(l[:-5].split("-")[::2])
            else:
                data.setdefault(label, []).append(list(map(int, l.split())))

    for k, v in data.items():
        if k == 'seed':
            continue
        data[k].sort(key=itemgetter(1))
    return data

def find_key(inputs, c):
    for k in inputs.keys():
        if c == k[0]:
            return k
    return None, None

def part1(inputs):
    chain = ['seed', 'soil', 'fertilizer', 'water',
             'light', 'temperature', 'humidity', 'location']
    res = inputs['seed']
    for c in chain:
        idx = find_key(inputs, c)
        if idx[1] is None:
            break

        new_res = []
        for r in res:
            intable = False
            for ran in inputs[idx]:
                if ran[1] <= r <= ran[1]+ran[2]:
                    new_r = (r - ran[1]) + ran[0]
                    new_res.append(new_r)
                    intable = True
                    break
            if not intable:
                new_res.append(r)
        res = new_res
    print (f"🎄 Part 1: {min(res)}")

def convert_into_range(lim, width):
    return (lim, lim+width-1)

def map_seed(s, m):
    destination_start, source_start, _ = m
    return destination_start + s - source_start

def map_seed_range(seed_range, map_ranges):
    seed_ranges = []
    seed_start, seed_end = seed_range[0], seed_range[1]

    for m in map_ranges:
        source_start, source_end = m[1], m[1]+m[2]-1
        overlap_start = max(seed_start, source_start)
        overlap_end = min(seed_end, source_end)

        if overlap_start <= overlap_end:
            if seed_start <= overlap_start - 1:
                seed_ranges.append((seed_start, overlap_start-1))

            seed_ranges.append((map_seed(overlap_start, m), map_seed(overlap_end, m)))
            if overlap_end+1 <= seed_end:
                seed_start = overlap_end + 1
            else:
                seed_start = sys.maxsize
                break
    if seed_start <= seed_end:
        seed_ranges.append((seed_start, seed_end))
    return seed_ranges

def part2(inputs):
    seed_ranges = []
    for x in range(0, len(inputs['seed']), 2):
        seed_ranges.append(convert_into_range(inputs['seed'][x], inputs['seed'][x+1]))

    for k, map_ranges in inputs.items():
        if k == 'seed':
            continue
        new_seed_ranges = []
        for seed_range in seed_ranges:
            new_seed_ranges += map_seed_range(seed_range, map_ranges)
        seed_ranges = new_seed_ranges

    lowest_location = min(seed_range[0] for seed_range in seed_ranges)
    print (f"🎄🎅 Part 2: {lowest_location}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 5         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(inputs)
print (f"Time: {time.time()-t0:.5f}")
