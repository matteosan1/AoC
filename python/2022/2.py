import time
from utils import readInput

def loadInput():
    lines = readInput("input_2.txt")
    pwds = []
    for l in lines:
        pwds.append(l.split(":"))
    return pwds

def part1(pwds):
    good_pwd = 0
    for p in pwds:
        c, p = p
        r, w = c.split(" ")
        rm, rM = map(int, r.split("-"))
        c = p.count(w)
        if (rm <= c <= rM):
            good_pwd += 1
    print ("🎄 Part 1: {}".format(good_pwd))

def part2(pwds):
    good_pwd = 0
    for p in pwds:
        c, p = p
        r, w = c.split(" ")
        rm, rM = map(int, r.split("-"))
        if (p[rm] == w) ^ (p[rM] == w):
            good_pwd += 1
    print ("🎄🎅 Part 2: {}".format(good_pwd))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 2         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))
