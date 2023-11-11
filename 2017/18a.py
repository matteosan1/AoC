from utils import readInput

lines = readInput("input_18.txt")

def readParam(p):
    global registry
    try:
        val = int(p)
    except:
        val = registry.get(p)

    return val

registry = {}
mem = None

line = 0
while 0 <= line < len(lines):
    parts = lines[line].split()
    cmd = parts[0]
    params = parts[1:]

    if cmd == "snd":
        mem = readParam(params[0])
    elif cmd == "set":
        registry[params[0]] = readParam(params[1])
    elif cmd == "add":
        registry[params[0]] = registry.setdefault(params[0], 0) + readParam(params[1])
    elif cmd == "mul":
        registry[params[0]] = registry.setdefault(params[0], 0) * readParam(params[1])
    elif cmd == "mod":
        registry[params[0]] = registry.setdefault(params[0], 0) % readParam(params[1])        
    elif cmd == "rcv":
        if (readParam(params[0]) != 0):
            print ("🎄Part 1: {}".format(mem))
            break
    elif cmd == "jgz":
        if readParam(params[0]) > 0:
            line += readParam(params[1])
            continue
    
    line += 1
