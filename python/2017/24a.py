import heapq

tiles = []
with open("input_24.txt") as f:
    for l in f:
        if l.startswith("********"):
            break
        tiles.append(tuple(map(int, l.split("\n")[0].split("/"))))

def findMatch(t, m):
    if m is None:
        m = 0
    return t[0] if t[1] == m else t[1]

def computeStrength(path, final):
    strength = sum([sum(t) for t in path])
    if final[1] < strength:
        return (path, strength)
    else:
        return final

bridge = ([], 0)
check = []
best_bridge = ([], 0)

heapq.heappush(check, bridge)
while len(check) != 0:
    bridge = heapq.heappop(check)
    ports = [t for t in tiles if bridge[1] in t and t not in bridge[0]]
    if len(ports) == 0:
        best_bridge = computeStrength(bridge[0], best_bridge)
    else:
        for p in ports:
            if p not in bridge[0]:
                match = p[0] if bridge[1] == p[1] else p[1]
                heapq.heappush(check, (bridge[0]+[p], match))

print ("🎄Part 1: {}".format(best_bridge))

