import time

from utils import readInput, DIRECTIONS

movements: dict[int, complex] = {i:d for i, d in enumerate(DIRECTIONS)}

def loadInput(filename: str) -> tuple[dict[complex, int], complex | None]:
    lines = readInput(filename)
    area: dict[complex, int] = {}
    start: complex | None = None
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == ".":
                area[complex(x, y)] = 0
            elif lines[y][x] == "^":
                area[complex(x, y)] = 0
                start = complex(x, y)
            elif lines[y][x] == "#":
                area[complex(x, y)] = 1
    return  area, start

def part1(area: dict[complex, int], start: complex|None) -> set[complex]:
    if start is None:
        raise ValueError("We need a start")
    face = 0
    pos: complex|None = start
    distincts = set([pos])
    try: 
        while True:
            new_pos: complex|None = pos + movements[face]
            if area[new_pos] == 1:
                face = (face+1)%4
            else:
                pos = new_pos
                distincts.add((pos))
    except:
        pass
    print (f"🎄 Part 1: {len(distincts)}")
    return distincts

def part2(area: dict[complex, int], start: complex|None, thepath: set[complex]) -> None:
    if start is None:
        raise ValueError("We need a start")

    blocks: list[complex] = []
    path = list(thepath)
    path.remove(start)
    for p in path:
        if p in blocks:
            continue
        area[p] = 1
        face = 0
        pos = start
        turns: set[tuple[complex, int]] = set([])
        isloop = False
        try:
            while True:
                new_pos = pos + movements[face]
                if area[new_pos] == 1:
                    face = (face+1)%4
                    if (pos, face) in turns:
                        isloop = True
                        break
                    turns.add((pos, face))
                else:
                    pos = new_pos
        except:
            pass
        if isloop:
            blocks.append(p)
        area[p] = 0

    print (f"🎄🎅 Part 2: {len(blocks)}")

if __name__ == "__main__":
    title = "Day 6: Guard Gallivant"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)

    inputs = loadInput("input_6.txt")
    
    t0 = time.time()
    path = part1(*inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    from utils import bcolors
    for y in range(130):
        for x in range(130):
            if complex(x, y) in path:
                print (bcolors.RED+"."+bcolors.ENDC, end="")
            elif inputs[0][complex(x, y)] == 0:
                print (".", end="")
            else:
                print (bcolors.BOLD+"#"+bcolors.ENDC, end="")
        print ("")
    print ("\n")

    t0 = time.time()
    part2(*inputs, path)
    print ("Time: {:.5f}".format(time.time()-t0))
