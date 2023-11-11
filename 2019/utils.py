def readLines(f):
    with open(f, "r") as f:
        lines = f.readlines()

    inputs  = []
    for l in lines:
        if l.startswith ("#") or l == "\n":
            continue
        inputs.append(l.split("\n")[0])
    
    return inputs

def readLine(f):
    with open(f, "r") as f:
        line = f.readline()
    return line

def manahattanDistance(b1, b2):
    d = abs(b1[0] - b2[0]) + abs(b1[1] - b2[1])
    return d

def manahattanDistance3d(b1, b2):
    d = abs(b1[0] - b2[0]) + abs(b1[1] - b2[1]) + abs(b1[2] - b2[2])
    return d

def manahattanDistance4d(b1, b2):
    d = abs(b1[0] - b2[0]) + abs(b1[1] - b2[1]) + abs(b1[2] - b2[2]) + abs(b1[3] - b2[3])
    return d

