lines = []
with open("input_9a.txt") as f:
    for l in f:
        lines.append(int(l.split("\n")[0]))

target = 10884537
start = 0
end = 1
sums = sum(lines[start:end])
while sums != target:
    if sums < target:
        end += 1
    elif sums > target:
        start += 1
    sums = sum(lines[start:end])
#print (sums, start, end)
print (min(lines[start:end]), max(lines[start:end]),
       min(lines[start:end]) + max(lines[start:end]))
