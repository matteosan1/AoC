import time

from itertools import permutations
from queue import Queue
from threading import Thread

from utils import readInput
from intcode import IntCode
            
def loadInput():
    return readInput("input_7.txt")
        
def part1(lines):
    max_val = 0
    phases = [0,1,2,3,4]
    qin = [Queue() for _ in range(len(phases))]
    for perm in permutations(phases, 5):
        threads = []
        progs = []
        for i in range(5):
            progs.append(IntCode(i, lines[0], qin=qin[i], mode="thread", qout=qin[(i+1)%5]))
            threads.append(Thread(target=progs[i].run))
            threads[i].start()
            qin[i].put(perm[i])
        qin[0].put(0)
        threads[-1].join()
        max_val = max(max_val, qin[0].get())
    print (f"🎅 Part 1: {max_val}")

def part2(lines):
    max_val = 0
    phases = [9,8,7,6,5]
    qin = [Queue() for _ in range(len(phases))]
    for perm in permutations(phases, 5):
        progs = []            
        threads = []
        for i in range(5):
            progs.append(IntCode(i, lines[0], qin=qin[i], mode="thread", qout=qin[(i+1)%5]))
            qin[i].put(perm[i])
            threads.append(Thread(target=progs[i].run))
            threads[i].start()
        qin[0].put(0)
        threads[-1].join()
        max_val = max(max_val, qin[0].get())
    print (f"🎅🎄 Part 2: {max_val}")

if __name__ == "__main__":
    title = "Day 7: Amplification Circuit"
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
