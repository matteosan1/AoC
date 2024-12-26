import time

from utils import readInput

def loadInput(filename: str) -> tuple[dict[str, list[complex]], int, int]:
    lines: list[str] = readInput(filename)
    
    antennas: dict[str, list[complex]] = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != "." and lines[y][x] != "#":
                antennas.setdefault(lines[y][x], []).append(complex(x, y))

    xmax = len(lines[0])
    ymax = len(lines)
    return antennas, xmax, ymax

# def draw_map(antennas, antinodes, xmax, ymax):
#     antennas_drawing = {}
#     for k, v in antennas.items():
#         for item in v:
#             antennas_drawing[item] = k

#     for y in range(ymax):
#         for x in range(xmax):
#             if (x, y) in antennas_drawing:
#                 print (antennas_drawing[(x,y)], end="")
#             elif (x, y) in antinodes:
#                 print ("#", end="")
#             else:
#                 print (".", end="")
#         print ()

def part1(antennas: dict[str, list[complex]], xmax: int, ymax: int):
    antinodes: set[complex] = set([])
    for poss in antennas.values():
        for i in range(len(poss)-1):
            for j in range(i+1, len(poss)):
                dpos = poss[j] - poss[i]
                for c in [-1, 2]:
                    an = poss[i]+c*dpos
                    if an.real >= 0 and an.real < xmax and an.imag >= 0 and an.imag < ymax:
                        antinodes.add(an)
    print (f"🎄 Part 1: {len(antinodes)}", end='')

def part2(antennas: dict[str, list[complex]], xmax: int, ymax: int):
    antinodes: set[complex] = set([])
    for poss in antennas.values():
        for i in range(len(poss)-1):
            for j in range(i+1, len(poss)):
                antinodes.add(poss[i])
                antinodes.add(poss[j])
                dpos = poss[j] - poss[i]

                an = poss[i]
                forward = backward = True
                c = 0
                while True:
                    if forward:
                        an = poss[i] + c*dpos
                        if an.real >= 0 and an.real < xmax and an.imag >= 0 and an.imag < ymax:
                            antinodes.add(an)
                        else:
                            forward = False
                    
                    if backward:
                        an = poss[i] - c*dpos
                        if an.real >= 0 and an.real < xmax and an.imag >= 0 and an.imag < ymax:
                            antinodes.add(an)
                        else:
                            backward = False

                    if not forward and not backward:
                        break
                    else:
                        c += 1
    print (f"🎄🎅 Part 2: {len(antinodes)}", end='')

if __name__ == '__main__':
    title = "Day 8: Resonant Collinearity"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_8.txt")

    t0 = time.time()
    part1(*inputs)
    print (f" - {time.time()-t0:.5f}")
    
    t0 = time.time()
    part2(*inputs)
    print (f" - {time.time()-t0:.5f}")
