import time

from collections import deque

from utils import readInput
from intcode import IntCode

def loadInput():
    return readInput("input_21.txt")

def toascii(txt):
    converted = []
    for c in txt:
        converted.append(ord(c))
    return converted

def output(msg):
    while len(msg):
        c = msg.popleft()
        if c <= 256:
            print (chr(c), end='')
        else:
            return c

def part1(lines):
    channel = {"Springdroid":deque([]), "me":deque([])}
    prog = IntCode("Springdroid", lines[0], channel=channel, mode="channel", output="me")
    code = """NOT C J 
AND D J 
NOT A T 
OR T J
WALK
"""
    channel['Springdroid'].extend(toascii(code))
    prog.run()
    print (f"🎅 Part 1: Intcode")
    print (output(channel["me"]))

def part2(lines):
    channel = {"Springdroid":deque([]), "me":deque([])}
    prog = IntCode("Springdroid", lines[0], channel=channel, mode="channel", output="me")
    code = """NOT C J 
AND D J 
AND H J
NOT B T 
AND D T 
OR T J
NOT A T 
OR T J
RUN
"""
    channel['Springdroid'].extend(toascii(code))
    prog.run()
    print (f"🎅🎄 Part 2: Intcode")
    print (output(channel["me"]))
    
if __name__ == "__main__":
    title = "Day 21: Springdroid Adventure"
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

