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

counts = 0
for a in answers:
    temp = []
    for i in a:
        temp += list(i)
    counts += len(set(temp))
print (counts)

