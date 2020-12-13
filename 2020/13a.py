lines = []
with open("input_13a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

offset = int(lines[0])
items = lines[1].split(",")
lines = []
for l in items:
    if l == "x":
        continue
    else:
        lines.append(int(l))
print (offset)
print (lines)

times = {}
for l in lines:
    times[l] = l - (offset%l)

keys = list(times.keys())
print (times)

line = keys[list(times.values()).index(min(times.values()))]
print (min(times.values())*line)
