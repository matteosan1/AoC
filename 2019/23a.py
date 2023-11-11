from utils import readInput

lines = readInput("input_23.txt")

def readParam(p):
    global registry
    try:
        val = int(p)
    except:
        val = registry.get(p)

    return val

registry = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0}
counter = 0

line = 0
while 0 <= line < len(lines):
    parts = lines[line].split()
    cmd = parts[0]
    params = parts[1:]

    if cmd == "set":
        registry[params[0]] = readParam(params[1])
    elif cmd == "sub":
        registry[params[0]] = registry.setdefault(params[0], 0) - readParam(params[1])
    elif cmd == "mul":
        registry[params[0]] = registry.setdefault(params[0], 0) * readParam(params[1])
        counter += 1
    elif cmd == "jnz":
        if readParam(params[0]) != 0:
            line += readParam(params[1])
            continue
    
    line += 1
print ("🎄Part 1: {}".format("".join(counter)))
