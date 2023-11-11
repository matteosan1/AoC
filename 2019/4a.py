from utils import readInput

lines = readInput("input_4.txt")
c = 0
for l in lines:
    pwds = l.split()
    temp = set(pwds)
    if len(pwds) == len(temp):
        c += 1

print ("🎄Part 1: {}".format(c))
