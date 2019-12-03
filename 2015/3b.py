with open("instructions3a.txt", "r") as f:
#with open("example3b.txt", "r") as f:
    lines = f.readlines()
    
presents = {(0,0): 2}
pos = [(0,0), (0,0)]
isSanta = 0
for l in lines:
    l = l.split("\n")[0]
    for c in l:
        if c == "^":
            pos[isSanta] = (pos[isSanta][0], pos[isSanta][1]+1)
        elif c == "v":
            pos[isSanta] = (pos[isSanta][0], pos[isSanta][1]-1)
        elif c == "<":
            pos[isSanta] = (pos[isSanta][0]-1, pos[isSanta][1])
        elif c == ">":
            pos[isSanta] = (pos[isSanta][0]+1, pos[isSanta][1])
        presents[pos[isSanta]] = presents.setdefault(pos[isSanta], 0) + 1
        isSanta = 1 - isSanta
        #print ("isSanta", isSanta, pos)
print (len(presents))
#print (presents)
