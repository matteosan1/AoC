import time, re

from collections import deque

from utils import readInput

r = re.compile("[a-z]{1,4}")

def loadInput():
    lines = readInput("instructions7a.txt")
    return deque(lines)

def decrypt(m):
    m = m.split("->")
    matches = r.findall(m[0])
    m[-1] = m[-1].strip()

    for v in matches:
        m[0]= m[0].replace(v, "____['" + v + "']")
    cmd = m[-1] + "=" + m[0].replace("____", "vars")

    cmd = cmd.replace("RSHIFT", ">>")
    cmd = cmd.replace("LSHIFT", "<<")
    cmd = cmd.replace("NOT", "65535-")
    cmd = cmd.replace("AND", "&")
    cmd = cmd.replace("OR", "|")
    return cmd

def part1(instructions):
    vars = {}
    while len(instructions) != 0:
        m = instructions.popleft()
        if m.startswith("#"):
            continue
        cmd = decrypt(m)
        try:
            #print("executing:", cmd)
            c = cmd.split("=")
            vars[c[0]] = eval(c[1])
        except:
            instructions.append(m)
    print (f"🎄 Part 1: {vars["a"]}")
    return vars['a']

def reset(instructions, a):
    for i in range(len(instructions)):
        if instructions[i].endswith(" -> b"):
            instructions[i] = f"{a} -> b"

def part2(instructions):
    vars = {}
    while len(instructions) != 0:
        m = instructions.popleft()
        cmd = decrypt(m)
        try:
            #print("executing:", cmd)
            c = cmd.split("=")
            vars[c[0]] = eval(c[1])
        except:
            instructions.append(m)
    print (f"🎄🎅 Part 2: {vars["a"]}")

if __name__ == "__main__":
    title = "Day 7: Some Assembly Required"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    a = part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    inputs = loadInput()
    reset(inputs, a)

    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
