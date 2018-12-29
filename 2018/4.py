import datetime
from itertools import groupby

with open("shifts.txt", "r") as f:
    lines = f.readlines()

shifts = {}
for l in lines:
    items = l.split("\n")[0].split(" ")
    date = datetime.datetime.strptime(items[0]+" "+items[1], "[%Y-%m-%d %H:%M]")
    if items[2] == "Guard":
        shifts.setdefault(items[3], [])
        last_key = items[3]
    elif items[2] == "falls":
        shifts[last_key].append([date, date.minute, 0])
    elif items[2] == "wakes":
        shifts[last_key][-1][2] = date.minute

result = {}
max_asleep = ["", 0]
max_asleep_min = ["", (0,0)]
for g in shifts.keys():
    temp_shifts = []
    asleep = 0
    for s in shifts[g]:
        temp_shifts = temp_shifts + [i for i in range(s[1], s[2])]
        asleep = asleep + s[2] - s[1]
    if max_asleep[1] < asleep:
        max_asleep = [g, asleep]
    groups = groupby(sorted(temp_shifts))
    temp = [(i,len(list(k))) for i,k in groups]
    result[g] = temp
    if len(result[g]) != 0:
        maximum_min, maximum_per_min = max(temp, key=lambda i: i[1])
        if max_asleep_min[1][1] < maximum_per_min:
            max_asleep_min = [g, (maximum_min, maximum_per_min)]

maximum = max(result[max_asleep[0]], key=lambda i: i[1])[0]
r = maximum * int(max_asleep[0][1:])
print max_asleep, r, maximum

r = max_asleep_min[1][0] * int(max_asleep_min[0][1:])
print max_asleep_min, r        
