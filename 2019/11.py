import time

from queue import Queue
from threading import Thread

from utils import readInput
from intcode import IntCode
            
def loadInput():
    return readInput("input_11.txt")

def painting(prog, hull, channel):
    thread = Thread(target=prog.run, daemon=True)
    thread.start()
    dir = 0
    pos = (0, 0)
    while True:
        for i in range(2):
            val = channel["me"].get()
            if val == "BYE":
                return
            if i == 0:
                hull[pos] = val
            else:
                if val == 0:
                    dir -= 1
                else:
                    dir += 1
                dir = dir % 4
        if dir == 0:
            pos = (pos[0], pos[1]-1)
        elif dir == 1:
            pos = (pos[0]+1, pos[1])
        elif dir == 2:
            pos = (pos[0], pos[1]+1)
        elif dir == 3:
            pos = (pos[0]-1, pos[1])
        channel["Robot"].put(hull.get(pos, 0))
    
def part1(lines):
    channel = {"Robot":Queue(), "me":Queue()}
    prog = IntCode("Robot", lines[0], qin=channel['Robot'], qout=channel['me'], mode="channel")
    channel['Robot'].put(0)
    hull = {}
    painting(prog, hull, channel)
    print (f"🎅 Part 1: {len(hull)}")

def show_hull(hull):
    xs = [h[0] for h in hull]
    ys = [h[1] for h in hull]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    for y in range(int(ymin), int(ymax+1)):
        for x in range(int(xmin), int(xmax+1)):
            val = hull.get((x, y), 0)
            if val == 1:
                print("▮", end='')
            else:
                print(" ", end='')
        print()
    
def part2(lines):
    channel = {"Robot":Queue(), "me":Queue()}
    channel['Robot'].put(1)
    prog = IntCode("Robot", lines[0], qin=channel['Robot'], qout=channel['me'], mode="channel")
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
