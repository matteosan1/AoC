def rotate(l, pos, dir="left"):
    if dir == "right":
        l = l[-pos:] + l[:-pos]
    else:
        l = l[pos:] + l[:pos]
    return l


programs = list('abcdefghijklmnop')

with open("input_16.txt") as f:
    line = f.readline().split('\n')[0]

def dance (line):
    global programs
    for l in line.split(","):
        if l.startswith("s"):
            programs = rotate(programs, int(l[1:]), "right")
        elif l.startswith("p"):
            idx = [programs.index(i) for i in l[1:].split("/")]
            temp = programs[idx[0]]
            programs[idx[0]] = programs[idx[1]]
            programs[idx[1]] = temp
        elif l.startswith("x"):
            idx = list(map(int, l[1:].split("/")))
            temp = programs[idx[0]]
            programs[idx[0]] = programs[idx[1]]
            programs[idx[1]] = temp
        else:
            print ("Unkown command.")
            import sys
            sys.exit()

dance(line)
print ("🎄Part 1: {}".format("".join(programs)))

programs = list('abcdefghijklmnop')

# pattern repeats every 60 dances
# 1000000000 % 60 = 40
turns = []
for i in range(40):
    dance(line)
    #if programs == list('abcdefghijklmnop'):
    #    turns.append(i)
    #    print (turns)

print ("🎁🎄Part 2: {}".format("".join(programs)))
