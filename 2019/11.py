import time

from utils import readInput
from intcode import IntCode
            
def loadInput():
    return readInput("input_11.txt")

def painting(prog, hull, channel):
    dir = 0
    pos = complex(0, 0)
    while True:
        prog.run()
        if len(channel['me']) == 0:
            break
        for i in range(2):
            val = channel["me"].pop()
            if i == 0:
                hull[pos] = val
            else:
                if val == 0:
                    dir -= 1
                else:
                    dir += 1
                dir = dir % 4
        if dir == 0:
            pos += complex(0,-1)
        elif dir == 1:
            pos += complex(1,0)
        elif dir == 2:
            pos += complex(0,1)
        elif dir == 3:
            pos += complex(-1,0)
        channel["Robot"].insert(0, hull.get(pos, 0))         
    
def part1(lines):
    channel = {"Robot":[0], "me":[]}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    hull = {}
    painting(prog, hull, channel)
    print (f"🎅 Part 1: {len(hull)}")

def show_hull(hull):
    xs = [h.real for h in hull]
    ys = [h.imag for h in hull]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    for y in range(int(ymin), int(ymax+1)):
        for x in range(int(xmin), int(xmax+1)):
            val = hull.get(complex(x, y), 0)
            if val == 1:
                print("▮", end='')
            else:
                print(" ", end='')
        print()
    
def part2(lines):
    channel = {"Robot":[1], "me":[]}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    hull = {}
    painting(prog, hull, channel)
    print (f"🎅🎄 Part 2:")
    show_hull(hull)

if __name__ == "__main__":
    title = "Day 11: Space Police"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
