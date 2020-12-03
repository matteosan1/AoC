lines = []
with open("input_3a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

#print (lines)
y = 0
x = 0
trees = 0
N = len(lines)
Nx = len(lines[0])
while True:
    y += 1
    if y >= N:
        break
    x += 3
    x = x % Nx
    print (N, Nx, y, x)
    if lines[y][x] == "#":
        trees += 1
print (trees)
