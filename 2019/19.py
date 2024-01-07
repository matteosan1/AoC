import time, copy

from collections import deque

from utils import readInput
from intcode import IntCode

def loadInput():
    return readInput("input_19.txt")

def scan(prog, x, y):
    prog.mem['Robot'].extend([x,y])
    prog.run()
    return prog.mem['me'].pop()

def part1(lines):
    channel = {"Robot":deque([]), "me":deque([])}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    prog.copy_code()
    tot = 0
    for x in range(0, 50):
        for y in range(0, 50):
            tot += scan(prog, x, y)
            prog.reset()

    print (f"🎅 Part 1: {tot}")

def get_ratios(prog):
    x = 0
    y = 10000
    while not scan(prog, x, y):
        x += 1
        prog.reset()
    x1 = x
    prog.reset()
    while scan(prog, x, y):
        x += 1
        prog.reset()
    x2 = x
    return y / x2, y / x1

def part2(lines):
    channel = {"Robot":deque([]), "me":deque([])}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    prog.copy_code()
    m1, m2 = get_ratios(prog)
    x2 = ((m1 * 99) + 99) / (m2 - m1)
    y1 = (m2 * x2) - 99
    print(x2, y1)
    print(round(x2)*10000 + round(y1))
    print (f"🎅🎄 Part 2: {0}")

if __name__ == "__main__":
    title = "Day 19: Tractor Beam"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    scaffold = part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    path = part2(lines)
    print ("Time: {:.5f}".format(time.time()-t0))

