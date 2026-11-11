import time

from collections import deque

from utils import readInput
from intcode import IntCode

def loadInput():
    return readInput("input_23.txt")

def init_computers(progs, channels):
    for i in range(50):
        channels.update({i:deque([])})
        channels[i].extend([i])
        prog = IntCode(i, lines[0], channel=channels, mode="channel", output="router")
        progs.append(prog)
        progs[-1].run()

def wake_up(channels, progs, nat=None):
    if nat is None or len(nat) == 0:
        for i in range(50):
            channels[i].append(-1)
            progs[i].run()
    else:
        channels['router'].extend([0, *nat])
        
def feed_nic(channels, progs, nat = None):
    while len(channels['router']) > 0:
        idx = channels['router'].popleft()
        x = channels['router'].popleft()
        y = channels['router'].popleft()
        if idx == 255:
            if nat is None:
                return y
            else:
                nat.clear()
                nat.extend([x, y])
        else:
            channels[idx].extend([x, y])
            progs[idx].run()
    return None
        
def part1(lines):
    progs = []
    channels = {"router":deque([])}
    init_computers(progs, channels)

    while True:
        if len(channels['router']) == 0:
            wake_up(channels, progs)
            res = None
        else:
            res = feed_nic(channels, progs)
        if res is not None:
            break
    print (f"🎅 Part 1: {res}")

def part2(lines):
    hist_nat = []
    nat = []
    progs = []
    channels = {"router":deque([])}
    init_computers(progs, channels)

    while True:
        if len(channels['router']) == 0:
            wake_up(channels, progs, nat)
            if len(nat) != 0:
                hist_nat.append(nat[1])
            if len(hist_nat) > 1 and nat[1] == hist_nat[-2]:
                break
        else:
            feed_nic(channels, progs, nat)            
    print (f"🎅🎄 Part 2: {nat[1]}")

    
if __name__ == "__main__":
    title = "Day 23: Category Six"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    path = part2(lines)
    print ("Time: {:.5f}".format(time.time()-t0))

