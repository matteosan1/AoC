dimensions = []

with open("instructions17a.txt", "r") as f:
    for cnt, l in enumerate(f):
        dimensions.append(int(l.split("\n")[0]))

dist = dict()
for mask in range(1, 1<<len(dimensions)):
    p = [d for i,d in enumerate(dimensions) if (mask & (1 << i)) > 0]
    if sum(p) == 150:
        dist[len(p)] = dist.setdefault(len(p), 0) + 1

print ("total:", sum(dist.values()))
print ("min:", dist[min(dist.keys())])
