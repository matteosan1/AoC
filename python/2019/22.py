import time, numpy as np, copy

from numpy import array_equal

from utils import readInput

def loadInput():
    lines = readInput("prova.txt")
    return lines
        
def part1(lines):
    n = 10 #007
    c = 3 #2019

    def deal_new(c, n):    return (-c - 1) % n
    def deal_inc(c, n, i): return ( c * i) % n
    def cut(c, n, i):      return ( c - i) % n

    for l in lines:
        if l == 'deal into new stack\n':
            c = deal_new(c, n)
        elif l.startswith('deal with increment '):
            c = deal_inc(c, n, int(l[len('deal with increment '):]))
        elif l.startswith('cut '):
            c = cut(c, n, int(l[len('cut '):]))

    print (f"ðŸŽ… Part 1: {c}")
        
def part2(lines):
    levels = {0:bugs}
    for i in range(1, 200):
        levels.update({i:np.zeros_like(bugs)})
        levels.update({-i:np.zeros_like(bugs)})
    min_level, max_level = min(levels.keys()), max(levels.keys())
    for minutes in range(200):
        update = copy.deepcopy(levels)
        for k in levels:
            if k == max_level or k == min_level:
                continue
            neighbours(levels, update, k)
        levels = copy.deepcopy(update)

    tot = 0
    for k in levels:
        tot += levels[k].sum()
    print (f"ðŸŽ„ Part 2: {tot}")
    
if __name__ == "__main__":
    title = "Day 22: Slam Shuffle"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    part1(copy.deepcopy(inputs))
    print ("Time: {:.5f}".format(time.time()-t0))
    
    #t0 = time.time()
    #part2(inputs)
    #print ("Time: {:.5f}".format(time.time()-t0))
