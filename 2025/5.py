import time, bisect

from utils import readInput, merge_intervals

def loadInput(filename: str) -> tuple[list, list]:
    lines = readInput(filename)
    ranges = []
    IDs = []
    for line in lines:
        if line == "":
            continue

        if "-" in line:
            ranges.append(list(map(int, line.split("-"))))
        else:
            IDs.append(int(line))

    merged = merge_intervals(ranges)
    return merged, IDs

def part1(ranges: list, ids: list) -> None:
    start_points = [r[0] for r in ranges]
    fresh = 0
    for item in ids:
        i = bisect.bisect_right(start_points, item)
        if i > 0 and item <= ranges[i-1][1]:
            fresh +=1
    print (f"🎄 Part 1: {fresh}")

def part2(ranges: list) -> None:
    fresh_IDs = sum([(end - start + 1) for start, end in ranges])
    print (f"🎄🎅 Part 2: {fresh_IDs}")

if __name__ == "__main__":
    title = "Day 5: Cafeteria"
    sub = "❄ "*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)

    t0 = time.time()
    inputs = loadInput("input_5.txt")
    print ("Loding Time: {:.5f}".format(time.time()-t0))

    t0 = time.time()
    part1(*inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

    t0 = time.time()
    part2(inputs[0])
    print ("Time: {:.5f}".format(time.time()-t0))
