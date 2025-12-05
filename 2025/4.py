import time

from utils import readInput, ALL_DIRECTIONS

def loadInput(filename: str) -> dict[complex, int]:
    lines = readInput(filename)
    rolls: dict[complex, int] = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "@":
                rolls[complex(x, y)] = 1
    return rolls

def accessible_roll(roll: complex, rolls: dict[complex, int], threshold: int) -> bool:
    if sum([rolls.get(roll+dir, 0) for dir in ALL_DIRECTIONS.values()]) < threshold:
        return True
    return False

def part1(rolls: dict[complex, int]):
    accessibles = sum([accessible_roll(roll, rolls, 4) for roll in rolls.keys()])
    print (f"🎄 Part 1: {accessibles}", end='')

def part2(rolls: dict[complex, int]):
    removed = 0
    while True:
        to_remove = [roll for roll in rolls.keys() if accessible_roll(roll, rolls, 4)]
        if len(to_remove) == 0:
            break
        removed += len(to_remove)
        for r in to_remove:
            rolls.pop(r)
    print (f"🎄🎅 Part 2: {removed}", end='')

if __name__ == "__main__":
    title = "Day 4: Printing Department"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_4.txt")
    
    t0 = time.perf_counter()
    part1(inputs)
    print (" - {:.5f}".format(time.perf_counter()-t0))
    
    t0 = time.perf_counter()
    part2(inputs)
    print (" - {:.5f}".format(time.perf_counter()-t0))
