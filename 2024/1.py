import time, numpy as np
from utils import readInput

def loadInput():
    lines = readInput("input_1.txt")
    id1 = []
    id2 = []
    for l in lines:
        id1.append(int(l.split()[0]))
        id2.append(int(l.split()[1]))
    return id1, id2

def part1(id1, id2):
    id1 = np.array(sorted(id1))
    id2 = np.array(sorted(id2))
    print (f"🎄 Part 1: {np.sum(np.abs(id1-id2))}")

def part2(id1, id2):
    tot = 0
    unique, counts = np.unique(id2, return_counts=True)
    id2 = dict(zip(unique, counts))
    for i in id1:
        tot += i*id2.get(i, 0)
    print (f"🎄🎅 Part 2: {tot}")

if __name__ == "__main__":
    title = "Day 1: Historian Hysteria"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub) #"⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs1, inputs2 = loadInput()
    
    t0 = time.time()
    part1(inputs1, inputs2)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs1, inputs2)
    print ("Time: {:.5f}".format(time.time()-t0))
