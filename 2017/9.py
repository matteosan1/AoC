def removeJunk(line):
    new_line = ""
    i = 0
    while i < len(line):
        if line[i] == "!":
            i += 2
        else:
            new_line += line[i]
            i += 1
    return new_line

def removeGarbage(line):
    new_line = ""
    i = 0
    ngarbage = 0
    while i < len(line):
        if line[i] == "<":
            ngarbage += 1
            v = line[i:].find(">")
            i += v+1
        else:
            new_line += line[i]
            i += 1
    print ("🎁🎄Part 2: {}".format(len(line) - len(new_line) - ngarbage*2))
    return new_line

def findGroup(line, nest=0, score=0):
    i = 0
    while i < len(line):
        if line[i] == "{":
            nest += 1
            off, nest, score = findGroup(line[i+1:], nest, score)
            i += off+1
        elif line[i] == "}":
            score += nest
            nest -= 1
            i += 1
            return i, nest, score
        else:
            i += 1
    return i, nest, score
        
line = ""
with open("input_9.txt") as f:
    for l in f:
        if l.startswith("###"):
            break
        line = l.split("\n")[0]
        line = removeGarbage(removeJunk(line))
        print ("🎄Part 1: {}".format(findGroup(line)[-1]))
        
