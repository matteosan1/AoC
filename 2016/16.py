part = 1
a = "11011110011011101"

if part == 1:
    size = 272
else:
    size = 35651584

def checksum(a):
    csum = ""
    for i in range(0, len(a), 2):
        if a[i] == a[i+1]:
            csum += "1"
        else:
            csum += "0"
    if len(csum) % 2 == 0:
        #print (csum)
        csum = checksum(csum)

    return csum

while len(a) < size:
    b = "".join(reversed(a)).replace("1", "2").replace("0", "1").replace("2", "0")
    a += "0"+b

#print (a)
if part == 1:
    print ("🎄Part 1: {}".format(checksum(a[:size])))
else:
    print ("🎁🎄Part 2: {}".format(checksum(a[:size])))
