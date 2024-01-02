import time

from itertools import permutations

from utils import readInput
from intcode import IntCode
            
def loadInput():
    return readInput("input_9.txt")

def part1(lines):
    prog = IntCode(0, lines[0])
    prog.run()
    print (f"ðŸŽ„ Part 1: Intcode output")

def part2(lines):
    prog = IntCode(0, lines[0])
    prog.run()
    print (f"ðŸŽ„ðŸŽ… Part 2: Intcode output")

if __name__ == "__main__":
    title = "Day 9: Sensor Boost"
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
