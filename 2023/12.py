import time
from functools import cache

from utils import readInput

def loadInput():
    lines = readInput("prova.txt")
    #lines = readInput("input_12.txt")
              
    inputs = []      
    for l in lines:
        parts = l.split(" ")
        inputs.append([parts[0], 
                      tuple(map(int, parts[1].split(",")))])
    return inputs
    
@cache
def numlegal(s, c):
    s = s.lstrip('.') # ignore leading dots

    # extreme cases
    # ['', ()] is legal
    if s == '':
        return int(c == ()) 

    # [s, ()] is legal so long as s has no '#' (we can convert '?' to '.')
    if c == ():
        return int(s.find('#') == -1) 

    # s starts with '#' so remove the first spring
    if s[0] == '#':
        if len(s) < c[0] or '.' in s[:c[0]]:
            return 0 # impossible - not enough space for the spring
        elif len(s) == c[0]:
            return int(len(c) == 1) #single spring, right size
        elif s[c[0]] == '#':
            return 0 # springs must be separated by '.' (or '?') 
        else:
            return numlegal(s[c[0]+1:],c[1:]) # one less spring

    # numlegal springs if we convert the first '?' to '#' + '.'
    return numlegal('#'+s[1:],c) + numlegal(s[1:],c)
    
def part1(inputs):
    res = [numlegal(s,c) for [s,c] in inputs]
    print (res)
    return sum(res)

def part2(inputs):
    ss2 = [[(s[0]+'?')*4 + s[0],s[1]*5] for s in inputs]
    res = [numlegal(s,c) for [s,c] in ss2]
    return sum(res)

if __name__ == '__main__':
    #print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    #print("⛄        Day 12         ⛄")
    #print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

    inputs = loadInput()
    
    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
