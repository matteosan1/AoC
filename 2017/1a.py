from utils import readSingleLine

captcha = readSingleLine("input_1.txt")

s = 0
i = 0

while i < len(captcha):
    next = (i+1) % (len(captcha))
    if captcha[i] == captcha[next]:
        s += int(captcha[i])
    i += 1

print ("🎄Part 1: {}".format(s))
