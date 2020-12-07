lines = []
with open ("input_6a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])
lines.append("")

answers = []
temp = []
for l in lines:
    if l == "":
        answers.append(temp)
        temp = []
    else:
        temp.append(l)

counts = [len(set.intersection(*list(map(set, a)))) for a in answers]
count = sum(counts)
print (count)

