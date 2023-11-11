import math

with open("input_25.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split("\n")[0]

a = 0
while True:
    registry = {"a":a, "b":0, "c":0, "d":0}

    outs = []
    line = 0
    n = 0
    while line < len(lines):
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
        elif cmd == "out":
            try:
                x = int(params[0])        
            except ValueError:
                x = registry[params[0]]
            outs.append(x)
            n += 1
            if n == 10:
                #print (outs)
                if outs == [0,1,0,1,0,1,0,1,0,1]:
                    print("🎁🎄Last part 2016: {}".format(a))
                    import sys
                    sys.exit()
                break
        elif cmd == "jnz":
            try:
                x = int(params[0])        
            except ValueError:
                x = registry[params[0]]
                
            try:
                y = int(params[1])        
            except ValueError:
                y = registry[params[1]]
            if x != 0:
                jump = True
                line += int(y)
        elif cmd == "sum":
            try:
                y = int(params[1])        
            except ValueError:
                y = registry[params[1]]
                
            registry[params[0]] += y

        elif cmd == "fac":
            try:
                y = int(params[1])        
            except ValueError:
                y = registry[params[1]]

            registry[params[0]] = math.factorial(y)
        elif cmd == "mlt":
            try:
                x = int(params[0])        
            except ValueError:
                x = registry[params[0]]

            try:
                y = int(params[1])        
            except ValueError:
                y = registry[params[1]]

            try:
                z = int(params[2])        
            except ValueError:
                z = registry[params[2]]
            registry[params[0]] = y*z
            
        elif cmd == "tgl":
            try:
                x = int(params[0])        
            except ValueError:
                x = registry[params[0]]
                
            if 0 <= line + x < len(lines):
                l = lines[line + x]
                nparams = len(l.split())
                if nparams == 2:
                    if l.startswith("inc"):
                        lines[line+x] = l.replace("inc", "dec")
                    else:
                        lines[line+x] = "inc" + l[3:]
                elif nparams == 3:
                    if l.startswith("jnz"):
                        lines[line+x] = l.replace("jnz", "cpy")
                    else:
                        lines[line+x] = "jnz" + l[3:]
                        
        if not jump:
            line += 1
    a += 1
