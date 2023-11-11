with open("input_12.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split("\n")[0]

part = 2
if part == 1:    
    registry = {"a":0, "b":0, "c":0, "d":0}
else:
    registry = {"a":0, "b":0, "c":1, "d":0}

line = 0
while line < len(lines):
    #print (lines[line])
    parts = lines[line].split()
    cmd = parts[0]
    params = parts[1:]
    jump = False
    
    if cmd == "cpy":
        try:
            x = int(params[0])
        except ValueError:
            x = registry[params[0]]
        registry[params[1]] = x
    elif cmd == "inc":
        registry[params[0]] += 1
    elif cmd == "dec":
        registry[params[0]] -= 1
    elif cmd == "jnz":
        try:
            x = int(params[0])        
        except ValueError:
            x = registry[params[0]]
        if x != 0:
            jump = True
            line += int(params[1])
    if not jump:
        line += 1

if part == 1:
    print ("🎄Part 1: {}".format(registry['a']))
else:
    print("🎁🎄Part 2: {}".format(registry['a']))
