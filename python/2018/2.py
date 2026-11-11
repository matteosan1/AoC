from utils import readLines

ids = readLines("ids.txt")

letters2 = []
letters3 = []
for id in ids:
    temp = list(id)
    in2 = False
    in3 = False
    for c in temp:
        count = temp.count(c)
        if count == 2 and not in2:
            in2 = True
            letters2.append(id)
        if count == 3 and not in3:
            in3 = True
            letters3.append(id)

print ("With 2: ", len(letters2))
print ("With 3: ", len(letters3))
print (len(letters2) * len(letters3))

ids = list(set(letters2 + letters3))
right_ids = []
for i1 in range(len(ids)-1):
    id1 = ids[i1]
    for i2 in range(i1, len(ids)):
        id2 = ids[i2]
        diff = 0
        for i in range(len(id1)):
            if id1[i] != id2[i]:
                diff = diff + 1

        if diff == 1:
            right_ids.append(id1)
            right_ids.append(id2)
            
print (right_ids[0])
print (right_ids[1])



