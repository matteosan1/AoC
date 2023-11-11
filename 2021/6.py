from utils import readInput

def sumDict(d1, d2):
    merge = {}
    merge.update(d1)
    for k2 in d2:
        if k2 in d1.keys():
            merge[k2] += d2[k2]
        else:
            merge[k2] = d2[k2]
    return merge

def breeding(offsets, days):
    children = {}
    for t in range(days+1):
        to_delete = []
        to_add = {}
        grown = {}
        for k, v in children.items():
            if k == (t-9):
                to_add[t] = to_add.setdefault(t, 0) + v
                idx = (t % 7) - 1
                grown[idx] = grown.setdefault(idx, 0) + v
                to_delete.append(k)
        for d in to_delete:
            del children[d]

        for i, o in offsets.items():
            if (i-t)%7 == 6:
                to_add[t] = to_add.setdefault(t, 0) + o

        children = sumDict(children, to_add)
        offsets = sumDict(offsets, grown)

    return sum(offsets.values()) + sum(children.values())

timers = readInput("input_6.txt")
offsets = {}
for i in list(map(int, timers[0].split(","))):
    offsets[i] = offsets.setdefault(i, 0) + 1
days = 80

fishes = breeding(offsets, days)
print ("🎄 Part 1 {:3} days: {}".format(days, fishes))

offsets = {}
for i in list(map(int, timers[0].split(","))):
    offsets[i] = offsets.setdefault(i, 0) + 1
days = 256
fishes = breeding(offsets, days)
print ("🎄🎅 Part 2 {:3} days: {}".format(days, fishes))
