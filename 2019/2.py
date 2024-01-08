import time

from collections import deque

from utils import readInput
from intcode import IntCode

def init_code(line):
    return list(map(int, line.split(",")))

def loadInput():
    return readInput("input_2.txt")
    
def part1(code):
    prog = IntCode("computer", code, mode="manual")
    prog.code[2] = 2
    prog.code[1] = 12
    prog.run()
    
    print (f"🎅 Part 1: {prog.code[0]}")

def part2(code):
    for noun in range(0, 100):
        for verb in range(0, 100):
            prog = IntCode("computer", code, mode="manual")
            prog.code[1] = noun
            prog.code[2] = verb
            prog.run()
            if prog.code[0] == 19690720:
                print (f"🎅🎄 Part 2: {100*noun+verb}")
                return

if __name__ == "__main__":
    title = "Day 2: 1202 Program Alarm"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    part1(lines[0])
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(lines[0])
    print ("Time: {:.5f}".format(time.time()-t0))
