import pandas as pd
import numpy as np

def decrypt(m):
    m = m.split(" ")
    if len(m) == 5:
        s = m[2].split(",")
        e = m[4].split(",")
        if m[1] == "off":
            v = 0
        else:
            v = 1
    elif len(m) == 4:
        s = m[1].split(",")
        e = m[3].split(",")
        v = 2

    return [v] + list(map(int, s)) + list(map(int, e))


data = pd.read_csv("instructions6a.txt", header = None, delimiter=":")
#data = pd.read_csv("examples6a.txt", header = None, delimiter=":")
msgs = data[0]

grid = np.zeros(shape=(1000, 1000))
for m in msgs:
    i = decrypt(m)
    #print (i)
    if i[0] == 2:
        temp = np.where(grid[i[1]:i[3]+1, i[2]:i[4]+1] == 0, 1, 0)
        grid[i[1]:i[3]+1, i[2]:i[4]+1] = temp
    else:
        grid[i[1]:i[3]+1, i[2]:i[4]+1] = i[0]

print (grid)
print(np.count_nonzero(grid == 1))
