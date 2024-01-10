import time

from itertools import permutations
#from queue import Queue
from threading import Thread

from utils import readInput
from intcode import IntCode, BlockingQueue
            
def loadInput():
    return readInput("input_7.txt")
        
def part1(lines):
    max_val = 0
    phases = [0,1,2,3,4]
    progs = []
    threads = []
    queue = BlockingQueue()
    for perm in permutations(phases, 5):
        for i in range(5):
            progs.append(IntCode(i, lines[0], queue=queue, mode="thread", output=(i+1)%5))
            threads.append(Thread(target=progs[-1].run))
            threads[-1].start()
            queue.put((i, perm[i]))
            if i == 0:
                queue.put((0, 0))
        threads[-1].join()
        max_val = max(max_val, queue.get()[1])
        break
    print (f"ðŸŽ„ Part 1: {max_val}")

def part2(lines):
    return 0
    max_val = 0
    phases = [9,8,7,6,5]
    for perm in permutations(phases, 5):
        channels = {i:[p] for i, p in enumerate(perm)}
        channels[0].insert(0, 0)
        progs = [IntCode(i, lines[0], channels, mode="channel", output=(i+1)%5) for i in range(5)]
        nalive = sum([p.alive for p in progs])
        while nalive > 0:
            for i in range(5):
                if progs[i].alive:
                    progs[i].run()
            
            nalive = sum([p.alive for p in progs])            

        max_val = max(max_val, channels[0][0])
    print (f"ðŸŽ„ðŸŽ… Part 2: {max_val}")

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
