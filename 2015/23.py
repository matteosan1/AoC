import time

from utils import readInput

def compiler(l, il, register):
    if l.startswith("hlf"):
        register[l[-1]] //= 2
        il += 1
    elif l.startswith("tpl"):
        register[l[-1]] *= 3
        il += 1
    elif l.startswith("inc"):
        register[l[-1]] += 1
        il += 1
    elif l.startswith("jmp"):
        l = l.split(" ")
        il += int(l[-1])
    elif l.startswith("jie"):
        l = l.split(" ")
        if register[l[1][-2]] %2 == 0:
            il += int(l[2])
        else:
            il += 1
    elif l.startswith("jio"):
        l = l.split(" ")
        if register[l[1][-2]] == 1:
            il += int(l[2])
        else:
            il += 1
    else:
        print ("Wrong command {}".format(l))
        import sys
        sys.exit()
    return il

def loadInput():
    lines = readInput("instructions23a.txt")
    return lines

def run(lines, register):    
    il = 0
    while il < len(lines):
        l = lines[il]
        il = compiler(l, il, register)

def part1(lines):
    register = {"a":0, "b":0}
    run(lines, register)
    print (f"🎄 Part 1: {register['b']}")

def part2(lines):
    register = {"a":1, "b":0}
    run(lines, register)
    print (f"🎄🎅 Part 2: {register['b']}")
    
if __name__ == "__main__":
    title = "Day 23: Opening the Turing Lock"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

