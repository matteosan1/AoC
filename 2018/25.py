from utils import readLines, manahattanDistance4d

def checkConstellation(s, cs):
    for c in cs:
        if s in c:
            return True
    return False

lines = readLines("constellation.txt")

stars = []
for l in lines:
    items = list(map(int, l.split(",")))
    stars.append(items)

constellations = []

while len(stars) > 0:
    #if checkConstellation(s1, constellations):
    #    continue
    s1 = stars[0]
    temp = [s1]
    stars.remove(s1)
    i = 0
    while len(stars) > 0:
        s2 = stars[i]
        for t in temp:
            if manahattanDistance4d(t, s2) <= 3:
                temp.append(s2)
                stars.remove(s2)
                i = 0
                break
        else:
            i = i + 1
        if i == len(stars):
            break
    constellations.append(temp)

print (constellations)
print (len(constellations))