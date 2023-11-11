scanners = {}
with open("input_13.txt") as f:
    for l in f:
        if l.startswith("###"):
            break
        l = l.split("\n")[0].split(":")
        scanners[int(l[0])] = int(l[1])-1

pos = {k:[0,1] for k in scanners.keys()}
curLay = 0
damage = 0
for i in range(max(scanners.keys())+1):
    curLay = i
    if i in scanners.keys() and pos[i][0] == 0:
        damage += i*(scanners[i]+1)
        #print ("caught ", i, pos[i][0])
    for k, v in pos.items():
        if pos[k][0] == scanners[k]:
            pos[k] = [scanners[k], -1]
        elif pos[k][0] == 0:
            pos[k] = [0,1]
        pos[k][0] += pos[k][1]
        
    #print (curLay)
    #print (pos)

print ("🎄Part 1: {}".format(damage))
