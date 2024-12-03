import time, numpy as np
from utils import readInput

def loadInput():
    lines = readInput("input_2.txt")
    reports = []
    for l in lines:
        reports.append(list(map(int, l.split())))
    return reports

def check_safe(r):
    if (np.all(r > 0) and np.max(r) <= 3) or (np.all(r < 0) and np.min(r)>=-3):
        return True
    
def part1(reports):
    n = 0
    for r in reports:
        if check_safe(np.diff(r)):
            n += 1
    print (f"🎄 Part 1: {n}")

def problem_dampener(r):
    for i in range(len(r)):
        r_damp = np.diff(np.delete(r, [i]))
        if check_safe(r_damp):
            return True
    return False

def part2(reports):
    n = 0
    for r in reports:
        if check_safe(np.diff(r)):
            n += 1
        else:
            if problem_dampener(r):
                n += 1
    print (f"🎄🎅 Part 2: {n}")

if __name__ == "__main__":
    title = "Day 2: Red-Nosed Reports"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub) #"⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
