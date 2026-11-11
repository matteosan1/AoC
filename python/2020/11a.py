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

diff = range(-1, 2)
tot = -1
#for counts in range(6):
while countOccupied(seats) != tot:
    tot = countOccupied(seats)
    new_seats = []
    for y in range(ymax):
        #print ("iter y", y)
        temp = []
        #print ("nl")
        for x in range(xmax):
            #print ("iter x", x)
            occupied = 0
            if seats[y][x] == ".":
                temp.append(".")
                continue
            for dx in diff:
                if x+dx == xmax or x+dx < 0:
                    continue
                for dy in diff:
                    if dx == dy == 0:
                        continue    
                    if y+dy == ymax or y+dy < 0:
                        continue
                    try:
                        #print (y+dy, x+dx, seats[y+dy][x+dx])
                        if seats[y+dy][x+dx] == '#':
                            occupied += 1
                    except:
                        continue
            #print (occupied)
            if occupied >= 4 and seats[y][x] == "#":
                temp.append("L")
            elif occupied == 0 and seats[y][x] == "L":
                temp.append("#")
            else:
                temp.append(seats[y][x])
        #if counts == 1:
        #    print (temp)
            #import sys
            #sys.exit()
        new_seats.append(temp)
    showSeats(xmax, ymax, new_seats)
    seats = list(new_seats)
    #showSeats(xmax, ymax, seats)
    print ()
print (tot)

    
