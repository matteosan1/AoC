import time
from utils import readInput

def loadInput():
    #lines = readInput("input_8_prova.txt")
    lines = readInput("input_8.txt")
    
    antennas = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != "." and lines[y][x] != "#":
                antennas.setdefault(lines[y][x], []).append((x, y))

    xmax = len(lines[0])
    ymax = len(lines)
    #print (antennas)
    return antennas, xmax, ymax

def draw_map(antennas, antinodes, xmax, ymax):
    antennas_drawing = {}
    for k, v in antennas.items():
        for item in v:
            antennas_drawing[item] = k

    for y in range(ymax):
        for x in range(xmax):
            if (x, y) in antennas_drawing:
                print (antennas_drawing[(x,y)], end="")
            elif (x, y) in antinodes:
                print ("#", end="")
            else:
                print (".", end="")
        print ()

def part1(antennas, xmax, ymax):
    antinodes = set([])
    for freq, poss in antennas.items():
        for i in range(len(poss)-1):
            for j in range(i+1, len(poss)):
                dx = poss[j][0] - poss[i][0]
                dy = poss[j][1] - poss[i][1]

                for c in [-1, 2]:
                    an = (poss[i][0]+c*dx, poss[i][1]+c*dy)
                    if an[0] >= 0 and an[0] < xmax and an[1] >= 0 and an[1] < ymax:
                        antinodes.add(an)
    return len(antinodes)

def part2(antennas, xmax, ymax):
    antinodes = set([])
    for freq, poss in antennas.items():
        for i in range(len(poss)-1):
            for j in range(i+1, len(poss)):
                antinodes.add(poss[i])
                antinodes.add(poss[j])
                dx = poss[j][0] - poss[i][0]
                dy = poss[j][1] - poss[i][1]

                an = poss[i]
                forward = backward = True
                c = 0
                while True:
                    an = (poss[i][0] + c*dx, poss[i][1] + c*dy)
                    if an[0] >= 0 and an[0] < xmax and an[1] >= 0 and an[1] < ymax:
                        antinodes.add(an)
                    else:
                        forward = False
                    
                    an = (poss[i][0] - c*dx, poss[i][1] - c*dy)
                    if an[0] >= 0 and an[0] < xmax and an[1] >= 0 and an[1] < ymax:
                        antinodes.add(an)
                    else:
                        backward = False

                    if not forward and not backward:
                        break
                    else:
                        c += 1
                        
    return len(antinodes)

if __name__ == '__main__':
    title = "Day 8: Resonant Collinearity"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(*inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(*inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
