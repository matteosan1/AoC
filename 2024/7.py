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

def replace_spaces(text, replacement_chars):
    index = 0
    output = ""
    for char in text:
        if char == " ":
            output += replacement_chars[index % len(replacement_chars)]
            index += 1
        else:
             output += char
    return output

def part1(operations):
    valid = 0
    for o in operations:
        spaces = len(o[1])-1
        sequences = product(["+", "*"], repeat=spaces)
        for s in sequences:
            result = o[1][0]
            for i in range(spaces):
                if s[i] == "+":
                    result += o[1][i+1]
                else:
                    result *= o[1][i+1]
                if result > o[0]:
                    break
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
                if result > o[0]:
                    break
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
