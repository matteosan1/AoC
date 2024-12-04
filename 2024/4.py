import time, numpy as np
from utils import readInput

def loadInput():
    lines = readInput("input_4.txt")
    crosswords = []
    for y in range(len(lines)):
        crosswords.append([ x for x in lines[y]])

    for _ in range(3):
        crosswords.insert(0, ["." for _ in range(len(crosswords[0]))])
    for _ in range(3):
        crosswords.append(["." for _ in range(len(crosswords[0]))])
    for i in range(len(crosswords)):
        crosswords[i] = ['.', '.', '.'] + crosswords[i] + ['.', '.', '.']
    return  np.array(crosswords)
    
def find_word(square):
    keyword = "XMAS"
    occ = 0

    if "".join(square[3, 3:]) == keyword:
        occ += 1

    if "".join(square[3, 3::-1]) == keyword:
        occ += 1

    if "".join(square[3::-1, 3]) == keyword:
        occ += 1

    if "".join(square[3:, 3]) == keyword:
        occ += 1

    diag = "".join(np.diagonal(square))
    antidiag = "".join(np.flipud(square).diagonal())

    if diag[3:] == keyword:
        occ += 1
    if diag[3::-1] == keyword:
        occ += 1
    if antidiag[3:] == keyword:
        occ += 1
    if antidiag[3::-1] == keyword:
        occ += 1
    return occ

def part1(xwords):
    occurrencies = 0
    xmax, ymax = xwords.shape
    for y in range(3, ymax-3):
        for x in range(3, xmax-3):
            if (xwords[y][x] == "X"):
                square = xwords[y-3:y+4, x-3:x+4]
                occ = find_word(square)
                if occ > 0:
                   occurrencies += occ
    print (f"🎄 Part 1: {occurrencies}")

def find_word2(square):
    keyword = "MAS"
    x_dd = 0
    diag = "".join(np.diagonal(square))
    antidiag = "".join(np.flipud(square).diagonal())

    if diag == keyword or diag[::-1] == keyword:
        x_dd += 1
    if antidiag == keyword or antidiag[::-1] == keyword:
        x_dd += 1

    return x_dd >= 2

def part2(xwords):
    occurrencies = 0
    xmax, ymax = xwords.shape
    for y in range(3, ymax-3):
        for x in range(3, xmax-3):
            if (xwords[y][x] == "A"):
                square = xwords[y-1:y+2, x-1:x+2]
                if find_word2(square):
                   occurrencies += 1

    print (f"🎄🎅 Part 2: {occurrencies}")

if __name__ == "__main__":
    title = "Day 4: Ceres Search"
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
