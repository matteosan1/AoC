import time

from math import dist, prod

from utils import readInput

def loadInput(filename: str) -> list:
    lines: list[str] = readInput(filename)
    jboxs = []
    for line in lines:
        jboxs.append(tuple(map(int, line.split(","))))
    return jboxs

def solver(jboxs: list, steps:int = 1000) -> int:
    conns = []
    for idx, box in enumerate(jboxs[:-1], 1):
        conns.extend((dist(box,item),{box,item}) for item in jboxs[idx:])
    conns = sorted(conns)[:steps]
    circuits = []
    for _, pair in conns:
        circ_ids = [idx for idx,circ in enumerate(circuits) if circ & pair]
        if circ_ids == 1:
            circuits[circ_ids[0]] |= pair
        elif circ_ids:
            circuits = [circ for idx,circ in enumerate(circuits) if idx not in circ_ids] + [pair.union(*[circuits[idx] for idx in circ_ids])]
        else:
            circuits.append(pair)
        if len(circuits) == 1 and len(circuits[0]) == len(jboxs):
            return prod(item[0] for item in pair)
    return prod(sorted(len(circ) for circ in circuits)[-3:])

def part1(jboxs: list) -> None:
    print (f"🎄 Part 1: {solver(jboxs)}", end='')

def part2(jboxs: list) -> None:
    print (f"🎄🎅 Part 2: {solver(jboxs, len(jboxs)*(len(jboxs)-1)//2)}", end='')

def main():
    title = "Day 8: Playground"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_8.txt")

    t0 = time.perf_counter()
    part1(inputs)
    print (f" - {time.perf_counter()-t0:.5f}")
    
    t0 = time.perf_counter()
    part2(inputs)
    print (f" - {time.perf_counter()-t0:.5f}")

if __name__ == "__main__":
    main()