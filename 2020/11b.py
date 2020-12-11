import numpy as np

def countOccupied(s):
    c = 0
    for x in range(len(s[0])):
        for y in range(len(s)):
            if s[y][x] == "#":
                c += 1
    return c

def showSeats(xmax, ymax, s):
    for y in range(ymax):
        for x in range(xmax):
            print (s[y][x], end='')
        print ()
        
lines = []
with open("input_11a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

xmax = len(lines[0])
ymax = len(lines)

seats = []
for l in lines:
    seats.append(list(l))
showSeats(xmax, ymax, seats)

dirs = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
tot = -1

#for counts in range(3):
while countOccupied(seats) != tot:
    tot = countOccupied(seats)
    new_seats = []
    for y in range(ymax):
        temp = []
        for x in range(xmax):
            occupied = 0
            if seats[y][x] == ".":
                temp.append(".")
                continue
            for d in dirs:
                xp = x
                yp = y
                while True:
                    xp += d[1]
                    yp += d[0]
                    if xp == xmax or xp < 0:
                        break
                    if yp == ymax or yp < 0:
                        break
                    
                    if seats[yp][xp] == '#':
                        occupied += 1
                        break
                    elif seats[yp][xp] == 'L':
                        break
            if occupied >= 5 and seats[y][x] == "#":
                temp.append("L")
            elif occupied == 0 and seats[y][x] == "L":
                temp.append("#")
            else:
                temp.append(seats[y][x])
        #if counts == 2 and y == 0:
        #    print (temp)
        #    import sys
        #    sys.exit()
        new_seats.append(temp)
    showSeats(xmax, ymax, new_seats)
    seats = list(new_seats)
    print ()
print (tot)

    
