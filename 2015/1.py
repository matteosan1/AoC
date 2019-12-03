with open("instructions1a.txt", "r") as f:
#with open("example1a.txt", "r") as f:
    lines = f.readlines()

char = 0
floor = 0
for l in lines:
    l = l.split("\n")[0]
    for c in l:
        if c == "(":
            char += 1
            floor += 1
        elif c == ")":
            char += 1
            floor -= 1
        if floor == -1:
            print ("char to reach -1:", char)

print (floor)
