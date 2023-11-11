import time
from utils import readInput

def loadInput():
    lines = readInput("input_5.txt")

    return lines

def rule(code, up=128):
    diff = up // 2
    for c in code:
        if c == 'F' or c == 'L':
            up -= diff
        diff //= 2
    return up - 1

def part1(lines):
    #code = "BFFFBBFRRR" #: row 70, column 7, seat ID 567.
    #code = "FFFBBBFRRR" #: row 14, column 7, seat ID 119.
    #code = "BBFFBBFRLL" #:
    #code = "FBFBBFFRLR"

    maxID = 0
    for l in lines:
        row = rule(l[:7])
        col = rule(l[7:], 8)
        id  = row*8+col
        if id > maxID:
            maxID = id

    print ("🎄 Part 1: {}".format(maxID))

def part2(lines):
    ids = []
    seats  = []
    for l in lines:
        row = rule(l[:7])
        col = rule(l[7:], 8)
        ids.append(row*8+col)
        seats.append((col, row))

    ids = set(ids)
    all = set(range(59, 905))

    for y in range(128):
        print ("{:3} ".format(y), end='')
        for x in range(8):
            if (x, y) in seats:
                print ("X", end="")
            else:
                print (".", end="")
            if x == 3:
                print (" ", end="")
        print ()

    print ("🎄🎅 Part 2: {}".format(all-ids))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 5         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))
