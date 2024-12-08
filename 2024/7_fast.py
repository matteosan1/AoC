import time

from itertools import product
from math import log10
from utils import readInput

def loadInput():
    #lines = readInput("input_7_prova.txt")
    lines = readInput("input_7.txt")
    operations = []
    for l in lines:
        oper = [int(l.split(": ")[0]), list(map(int, l.split(": ")[1].split(" ")))]
        operations.append(oper)
    return operations

def check_div(o):
    res = [""]*(len(o[1])-1)
    for i in range(1, len(o[1])):
        if o[0]%o[1][i] != 0:
            res[i-1] = "+"
    return res

def part1(operations):
    valid = 0
    for o in operations:
        fixed = check_div(o)
        #print (o)
        #print (fixed)
        #print (len(fixed)-fixed.count("+"))
        sequences = product(["+", "*"], repeat=len(fixed)-fixed.count("+"))
        for s in sequences:
            #print ("seq ", s)
            result = o[1][0]
            mask = []
            i = 0
            for j in range(len(fixed)):
                if fixed[j] == "": 
                    mask.append(s[i])
                    i += 1
                else:
                    mask.append(fixed[j])
            #print (mask)
            for i in range(len(mask)):
                if mask[i] == "+":
                    result += o[1][i+1]
                else:
                    result *= o[1][i+1]
            if o[0] == result:
                valid += result
                break
    return valid

def part2(operations):
    valid = 0
    for o in operations:
        spaces = len(o[1])-1
        sequences = product(["+", "*", "||"], repeat=spaces)
        for s in sequences:
            result = o[1][0]
            for i in range(spaces):
                if s[i] == "+":
                    result += o[1][i+1]
                elif s[i] == "*":
                    result *= o[1][i+1]
                else:
                    ofm = int(log10(abs(o[1][i+1])))+1
                    result = result*10**ofm + o[1][i+1]
            if o[0] == result:
                valid += result
                break
    return valid

if __name__ == '__main__':
    title = "Day 7: Bridge Repair"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
