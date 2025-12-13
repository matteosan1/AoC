import time, numpy as np

from utils import readInput, DIRECTIONS

def loadInput(filename: str) -> tuple[complex, list]:
    lines = readInput(filename)
    splitters = []
    start = complex(0, 0)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "S":
                start = complex(x, y)
            elif lines[y][x] == "^":
                splitters.append(complex(x, y))
    return start, splitters

def part1(start: complex, splitters: list) -> None:
    beams = [start]
    splits = 0
    for i in range(150):
        new_beams = []
        for beam in beams:
            beam += DIRECTIONS[2]
            if beam in splitters:
                splits += 1
                new_beams.append(beam+DIRECTIONS[1])
                new_beams.append(beam+DIRECTIONS[3])
            else:
                new_beams.append(beam)
        beams = list(set(new_beams))
    print (f"🎄 Part 1: {splits}")

def part2(start: complex, splitters: list) -> None:
    cols = int(max([s.real for s in splitters]) + 2)
    rows = int(max([s.imag for s in splitters]) + 1)
    path_counts = np.zeros(cols, dtype=int)
    path_counts[int(start.real)] = 1

    for i in range(rows - 1):
        next_path_counts = np.zeros(cols, dtype=int)
        for j in range(cols):
            if path_counts[j] == 0:
                continue
            if complex(j, i+1) not in splitters:
                next_path_counts[j] += path_counts[j]
            else:
                next_path_counts[j - 1] += path_counts[j]
                next_path_counts[j + 1] += path_counts[j]
        path_counts = next_path_counts
        #print (path_counts)
    print (f"🎄🎅 Part 2: {np.sum(path_counts)}")

def main():
    title = "Day 7: Laboratories"
    sub = "❄ "*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)

    t0 = time.perf_counter()
    inputs = loadInput("input_7.txt")
    print ("Loding Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part1(*inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part2(*inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    main()