import time
from utils import readInput

def loadInput():
    lines = readInput("input_1.txt")
    return lines

def look_for_digits(l):
    i = 0
    digits = []
    while i < len(l):
        if '0' <= l[i] <= '9':
            digits.append(l[i])
            break
        i += 1
            
    i = len(l)-1
    while i > 0:
        if '0' <= l[i] <= '9':
            digits.append(l[i])
            break
        i -= 1
    return digits
    
def part1(lines):
    codes = []
    for l in lines:
        digits = look_for_digits(l)
        if len(digits) == 0:
            continue
        else:
            codes.append(int(digits[0]+digits[-1]))

    print (f"🎄 Part 1: {sum(codes)}")

def part2(lines):
    codes = []
    repl = {'one':"o1e", 'two':"t2o", 'three':"t3e", 'four':"f4r",
            'five':"f5e", 'six':"s6x", 'seven':"s7n",
            'eight':"e8t", 'nine':"n9e"}
    for l in lines:
        for k, v in repl.items():
            l = l.replace(k, v)
        digits = look_for_digits(l)
        if len(digits) == 0:
            continue
        else:
            codes.append(int(digits[0]+digits[-1]))
        
    print (f"🎄🎅 Part 2: {sum(codes)}")

if __name__ == "__main__":
    title = "Day 1: Trebuchet?!"
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
