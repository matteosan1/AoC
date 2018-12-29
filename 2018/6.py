with open("areas.txt", "r") as f:
    lines = f.readlines()

coord = []
xmin = 100000000
ymin = 100000000
xmax = 0
ymax = 0
for l in lines:
    x, y = map(int(l.split(",")))
    if x < xmin:
        xmin = x
    if y < ymin:
        ymin = y

    if x > xmax:
        xmax = x
    if y > ymax:
        ymax = y
    
    coord.append([x, y])




















    

