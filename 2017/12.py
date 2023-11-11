import heapq

connections = {}
with open("input_12.txt") as f:
    for l in f:
        if l.startswith("###"):
            break
        l = l.split("\n")[0].split("<->")
        connections[int(l[0])] = list(map(int, l[1].split(",")))

all_progs = sorted(connections.keys())
groups = []
while len(all_progs) != 0:
    progs = []
    heapq.heappush(progs, all_progs[0])
    group = set()
    while len(progs) != 0:
        p = heapq.heappop(progs)
        for candidate in connections[p]:
            if candidate not in group:
                heapq.heappush(progs, candidate)
        group.update([p])

    groups.append((group, len(group)))
    for g in group:
        all_progs.remove(g)
print ("🎄Part 1: {}".format(groups[0][1]))
print ("🎁🎄Part 2: {}".format(len(groups))) 
