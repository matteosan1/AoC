import time

t0 = time.time()
with open("instructions3a.txt", "r") as f:
#with open("example3a.txt", "r") as f:
    lines = f.readlines()
    
presents = {(0,0): 1}
pos = (0,0)
for l in lines:
    l = l.split("\n")[0]
    for c in l:
        if c == "^":
            pos = (pos[0], pos[1]+1)
        elif c == "v":
            pos = (pos[0], pos[1]-1)
        elif c == "<":
            pos = (pos[0]-1, pos[1])
        elif c == ">":
            pos = (pos[0]+1, pos[1])
        presents[pos] = presents.setdefault(pos, 0) + 1

print (len(presents))
print (time.time() - t0)
