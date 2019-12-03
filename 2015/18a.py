import numpy, copy

size = 100
matrix = numpy.zeros(shape=(size+2, size+2))

def update(x, y):
    global temp, matrix
    xmin = x - 1
    xmax = x + 1
    ymin = y - 1
    ymax = y + 1
    on = numpy.sum(temp[ymin:ymax+1, xmin:xmax+1]) - temp[y, x]
    #if x == 6 and y==1:
    #    print (temp[ymin:ymax+1, xmin:xmax+1])
    #    print (x, y, on, xmin, ymin, xmax, ymax)
    if temp[y, x] == 1 and (on == 2 or on == 3):
        matrix[y, x] = 1
    elif temp[y, x] == 1 and not (on == 2 or on == 3):
        matrix[y, x] = 0
    elif temp[y, x] == 0 and on == 3:
        matrix[y, x] = 1
    elif temp[y, x] == 0 and on != 3:
        matrix[y, x] = 0

filename = "instructions18a.txt"
with open(filename, "r") as f:
    lines = f.readlines()

y = 1
for l in lines:
    x = 1
    l = l.split("\n")[0]
    for c in l:
        if c == "#":
            matrix[y, x] = 1
        x += 1
    y += 1

#print (matrix[1:-1, 1:-1])

step = 100
for _ in range(step):
    temp = copy.deepcopy(matrix)
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            update(x, y)
    #print (temp[1:-1, 1:-1])
print (matrix[1:-1, 1:-1])
print (numpy.sum(matrix))
