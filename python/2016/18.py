from utils import readSingleLine

line = readSingleLine("input_18.txt")

part = 1
if part == 1:
    steps = 39
else:
    steps = 399999
    
c = line.count(".")
for s in range(steps):
    newline = ""
    for i in range(len(line)):
        if i == 0:
            if (line[i] == "^" and line[i+1] == "^") or (line[i+1] == "^"):
                newline += "^"
            else:
                newline += "."
        elif i == len(line)-1:
            if (line[i] == "^" and line[i-1] == "^") or (line[i-1] == "^"):
                newline += "^"
            else:
                newline += "."
        else:
            if (line[i] == "^" and line[i-1] == "^" and line[i+1] == ".") or \
               (line[i] == "^" and line[i-1] == "." and line[i+1] == "^") or \
               (line[i-1] == "^" and line[i] == "." and line[i+1] == ".") or \
               (line[i+1] == "^" and line[i] == "." and line[i-1] == "."):
                newline += "^"
            else:
                newline += "."
    c += newline.count(".")
    line = newline

if part == 1:
    print ("🎄Part 1: {}".format(c))
else:
    print ("🎁🎄Part 2: {}".format(c))
