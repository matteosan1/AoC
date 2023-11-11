with open("input_11.txt") as f:
    for l in f:
        if l.startswith("###"):
            break
        dirs = l.split("\n")[0].split(",")

move = {'s':(lambda a:(a[0],a[1]+1)),
        'n':(lambda a:(a[0],a[1]-1)),
        'se':(lambda a:(a[0]+1,a[1]) if a[0]%2==0 else (a[0]+1,a[1]+1)),
        'sw':(lambda a:(a[0]-1,a[1]) if a[0]%2==0 else (a[0]-1,a[1]+1)),
        'ne':(lambda a:(a[0]+1,a[1]-1) if a[0]%2==0 else (a[0]+1,a[1])),
        'nw':(lambda a:(a[0]-1,a[1]-1) if a[0]%2==0 else (a[0]-1,a[1]))}

max_dist = 0
pos = (0,0)
for d in dirs:
    pos = move[d](pos)
    dist = abs(pos[1]) + abs(pos[0])-abs(pos[0])//2
    if dist > max_dist:
        max_dist = dist

print ("🎄Part 1: {}".format(dist))
print ("🎁🎄Part 2: {}".format(max_dist))
