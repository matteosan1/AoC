scanners = {}
with open("input_13.txt") as f:
    for l in f:
        if l.startswith("###"):
            break
        l = l.split("\n")[0].split(":")
        scanners[int(l[0])] = int(l[1])

def scannerPos(picos, r, delay):
    return (picos+delay+1)%((r-1)*2)
    
delay = 0
while True:
    #print (delay)
    for i in sorted(scanners.keys()):
        if scannerPos(i, scanners[i], delay-1) == 0:
            break
    else:
        break    
    delay += 1

print ("🎁🎄Part 2: {}".format(delay))

