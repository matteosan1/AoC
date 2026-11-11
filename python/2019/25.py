import time

from collections import deque
from itertools import combinations

from utils import readInput
from intcode import IntCode

def loadInput():
    return readInput("input_25.txt")

def toascii(txt):
    converted = []
    for c in txt:
        converted.append(ord(c))
    if converted[-1] != 10:
        converted.append(10)
    return converted

def output(msg):
    while len(msg):
        c = msg.popleft()
        if c <= 256:
            print (chr(c), end='')
        else:
            return c

def read_path():
    with open("path.txt", "r") as f:
        lines = f.readlines()
    print (lines)
    return [toascii(l) for l in lines]
        
def part1(lines):
    instructions = read_path()
    progs = []
    channel = {"droid":deque([]), "me":deque([])}
    prog = IntCode("droid", lines[0], channel=channel, mode="channel", output="me")

    for ins in instructions:
    #while True:
        prog.run()
        output(channel['me'])
        #a = input()
        #print (a)
        #channel['droid'].extend(toascii(a))
        channel['droid'].extend(ins)

    objs = ["fuel cell", "space heater", "hologram", "space law space brochure", "food ration", "tambourine", "spool of cat6", "festive hat"]
    current = set()
    tot = 0
    for i in range(1, 8):
        for c in combinations(range(8), i):
            to_remove = current - set(c)
            to_add = set(c) - current
            cmds = []
            for a in to_add:
                cmds.append(toascii(f"take {objs[a]}"))
            for r in to_remove:
                cmds.append(toascii(f"drop {objs[r]}"))
            cmds.append(toascii("south"))
            for cmd in cmds:
                channel['droid'].extend(cmd)
                prog.run()
                output(channel['me'])
            current = set(c)
    print (f"🎅 Part 1: {[objs[c] for c in current]}")

if __name__ == "__main__":
    title = "Day 25: Cryostasis"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
