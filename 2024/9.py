import time
from utils import readInput

def loadInput():
    #lines = readInput("input_9_prova.txt")
    lines = readInput("input_9.txt")
    disk = lines[0]
    return disk

def part1(disk):
    fragments = []
    try:
        for i in range(0, len(disk), 2):
            fragments += [i//2]*int(disk[i])
            fragments += [-1]*int(disk[i+1])
    except:
        pass        
    idx_rvs = len(fragments)-1
    for idx in range(len(fragments)):
        if fragments[idx] == -1:
            fragments[idx] = fragments[idx_rvs]
            fragments[idx_rvs] = -1
            idx_rvs -= 1
            while fragments[idx_rvs] == -1:
                idx_rvs -= 1
        if idx == idx_rvs:
            break

    checksum = 0
    for i in range(idx+1):
        checksum += i*int(fragments[i])
    return checksum

class Fragment:
    def __init__(self, id, length):
        self.id = id
        self.length = length

    def checksum(self, idx):
        v = 0
        for i in range(self.length):
            v += self.id*(idx+i)
        return v
    
    def __repr__(self):
        s = ""
        for _ in range(self.length):
            if self.id == -1:
                s += "."
            else:
                s += str(self.id)
        return s

def part2(disk):
    fragments = []
    for i in range(0, len(disk)):
        id = -1
        if i%2 == 0:
            id = i//2
        fragments.append(Fragment(id, int(disk[i])))

    idx_rvs = len(fragments)-1
    while idx_rvs > 1:
        if fragments[idx_rvs].id != -1 and fragments[idx_rvs].length != 0:
            idx = 0
            while idx < len(fragments):
                if idx == idx_rvs:
                    break
                if fragments[idx].id == -1:
                    if fragments[idx].length >= fragments[idx_rvs].length:
                        if fragments[idx].length > fragments[idx_rvs].length:
                            old_length = fragments[idx].length
                            fragments[idx].id = fragments[idx_rvs].id
                            fragments[idx].length = fragments[idx_rvs].length
                            fragments.insert(idx+1, Fragment(-1, old_length - fragments[idx_rvs].length))
                            idx_rvs += 1
                        else:
                            fragments[idx].id = fragments[idx_rvs].id
                        fragments[idx_rvs].id = -1
                        break
                idx += 1
        idx_rvs -= 1
    # for f in fragments:
    #     print (f, end="")
    # print()

    idx = 0
    checksum = 0
    for f in fragments:
        if f.id != -1:
            checksum += f.checksum(idx)
        idx += f.length
    return checksum

if __name__ == '__main__':
    title = "Day 9: Disk Fragmenter"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
