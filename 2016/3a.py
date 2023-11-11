
comb = [(0,1,2), (0,2,1), (1,2,0)]
triangles = []
with open("input_3.txt") as f:
    for l in f.readlines():
        t = [int(c) for c in l.split("\n")[0].split(" ") if c != ""]
        if len(t) != 0:
            for c in comb:
                if t[c[0]] + t[c[1]] <= t[c[2]]:
                    break
            else:
                triangles.append(t)

print ("🎄Part 1: {}".format(len(triangles)))
