
comb = [(0,1,2), (0,2,1), (1,2,0)]
triangles = [[], [], []]
with open("input_3.txt") as f:
    for l in f.readlines():
        t = [int(c) for c in l.split("\n")[0].split(" ") if c != ""]
        if len(t) != 0:              
            for i in range(3):
                triangles[i].append(t[i])
        
real_triangles = []
for i in range(3):
    for t in range(0, len(triangles[i]), 3):
        newt = [triangles[i][t],
                triangles[i][t+1],
                triangles[i][t+2]]

        for c in comb:
            if newt[c[0]] + newt[c[1]] <= newt[c[2]]:
                break
        else:
            real_triangles.append(newt)

print("🎁🎄Part 2: {}".format(len(real_triangles)))
