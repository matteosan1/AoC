from utils import readInput, printMap
import numpy as np

display = np.zeros(shape=(50, 6))
lines = readInput("input_8.txt")
for l in lines:
    if l.startswith("rect"):
        x, y = l.split(" ")[1].split("x")
        x = int(x)
        y = int(y)
        display[:x, :y] = 1
    elif l.startswith("rotate"):
        items = l.split(" ")
        if items[1] == "column":
            col = int(items[2][2:])
            amount = int(items[-1].strip())
            display[col, :] = np.roll(display[col, :], amount)
        elif items[1] == "row":
            row = int(items[2][2:])
            amount = int(items[-1].strip())
            display[:, row] = np.roll(display[:, row], amount)


print ("🎄Part 1: {}".format((display==1).sum()))
print("🎁🎄Part 2: ")
printMap(display)
