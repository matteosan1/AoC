from utils import readInput
from collections import Counter

lines = readInput("input_6.txt")

words = ["" for _ in  range(len(lines[0]))]
for l in lines:
    for i in range(len(l)):
        words[i] += l[i]

msg = ""
for i in range(len(words)):
    d = Counter(words[i])
    #print (d)
    msg += max(d, key=d.get)

print ("🎄Part 1: {}".format(msg))
