import time, re

from utils import readInput

r = re.compile('\\\\x\\w\\w')

def loadInput():
    lines = readInput("instructions8a.txt")
    return lines

def part1(inputs):
    real_length = 0
    length = 0
    for d in inputs:
        d = d.split("\n")[0]
        real_length += len(d)
        d = d[1:-1]
        d = d.replace('\\"', '"')
        d = d.replace('\\\\', '\\')
        matches = r.findall(d)
        for m in matches:
            try:
                d = d.replace(m, chr(int("0x"+m[2:], 16)))
            except:
                continue
        length += len(d)

    print (f"🎄 Part 1: {real_length-length}")

def part2(inputs):
    real_length = 0
    length = 0
    for d in inputs:
        d = d.split("\n")[0]
        real_length += len(d)
        d = d.replace('"', '/"')
        d = d.replace('\\', '\\\\')
        d = '"' + d + '"'
        length += len(d)
    print (f"🎄🎅 Part 2: {length - real_length}")

if __name__ == "__main__":
    title = "Day 8: Matchsticks"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))