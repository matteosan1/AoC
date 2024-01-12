import time

from utils import readInput
from intcode import IntCode

def loadInput():
    return readInput("input_5.txt")
    
def part1(lines):
    prog = IntCode("TEST", lines[0], mode="manual")
    print ("Provide 1")
    prog.run()
    print (f"🎅 Part 1: IntCode")

def part2(lines):
    prog = IntCode("TEST", lines[0], mode="manual")
    print ("Provide 5")
    prog.run()
    print (f"🎅🎄 Part 2: IntCode")

if __name__ == "__main__":
    title = "Day 5: Sunny with a Chance of Asteroids"
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
