import time, re
from utils import readInput

colors = ["red", "green", "blue"]
r = {}
for c in colors:
    r[c] = re.compile(f"(\d+) {c}")

def loadInput():
    lines = readInput("input_2.txt")
    return lines

def part1(inputs):
    tot = 0

    game = {"red":12, "green":13, "blue":14}
    r_game = re.compile(r"Game\s(\d+):")

    for l in inputs:
        m = r_game.match(l)
        id = int(m.groups()[0])

        possible = True
        for c in colors:
            matches = list(map(int, r[c].findall(l)))
            if max(matches) > game[c]:
                possible = False
                break
        if possible:
            tot += id
    print (f"🎄 Part 1: {tot}")

def part2(inputs):
    r_game = re.compile(r"Game\s(\d+):")
    powers = []
    for l in inputs:
        m = r_game.match(l)
        id = int(m.groups()[0])
        cubes = 1
        for c in colors:
            cubes *= max(list(map(int, r[c].findall(l))))
        powers.append(cubes)
    print (f"🎄🎅 Part 2: {sum(powers)}")


if __name__ == "__main__":
    title = "Day 2: Cube Conundrum"
    #sub = "⛄"*(len(title)//2+2)
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub) #"⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print (f"Time: {time.time()-t0:.5f}")
    
    t0 = time.time()
    part2(inputs)
    print (f"Time: {time.time()-t0:.5f}")
