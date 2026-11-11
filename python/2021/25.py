from utils import readInput
import numpy as np

def check(cm, typ):
    to_move = []
    for y in range(ymax):
        for x in range(xmax):
            if cm[x, y] == typ:
                if typ == 1:
                    if x == xmax - 1:
                        xnext = 0
                    else:
                        xnext = x+1
                    if cm[xnext, y] == 0:
                        to_move.append(((x, y), (xnext, y)))
                elif typ == 2:
                    if y == ymax - 1:
                        ynext = 0
                    else:
                        ynext = y+1
                    if cm[x, ynext] == 0:
                        to_move.append(((x, y), (x, ynext)))
    return to_move

def move(cm, to_move, typ):
    for m in to_move:
        cm[m[0]] = 0
        cm[m[1]] = typ
    return len(to_move)

def printMap(cm):
    for y in range(cm.shape[1]):
        for x in range(cm.shape[0]):
            if cm[x, y] == 0:
                print (".", end="")
            elif cm[x, y] == 1:
                print (">", end="")
            elif cm[x, y] == 2:
                print ("v", end="")
        print ("")
    print ("")

lines = readInput("input_25.txt")
xmax = len(lines[0])
ymax = len(lines)
cm = np.zeros(shape=(xmax, ymax))
for y in range(ymax):
    for x in range(xmax):
        if lines[y][x] == ">":
            cm[x, y] = 1
        elif lines[y][x] == "v":
            cm[x, y] = 2

steps = 0
printMap(cm)

while True:
    moves = 0
    for i in range(1, 3):
        moves += move(cm, check(cm, i), i)
    if moves == 0:
        break
    #printMap(cm)
    steps += 1
    
printMap(cm)
print ("🛷🦌🎅🎁🎄 Part 1: {}".format(steps+1))
