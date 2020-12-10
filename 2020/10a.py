lines = []
with open("test_10a.txt") as f:
    for l in f:
        lines.append(int(l.split("\n")[0]))

jolts = []
s = [0] + sorted(lines) + [max(lines) + 3]
print (s)
for i in range(1, len(s)):
    diff = s[i] - s[i-1]
    jolts.append(diff)

print (jolts)
print (jolts.count(1), jolts.count(3))
print (jolts.count(1)*jolts.count(3))
from matplotlib import pyplot as plt
plt.hist(jolts)
plt.show()
    
