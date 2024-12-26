import time

from utils import readInput

def loadInput(filename: str) -> str:
    return readInput(filename)[0]

def part1(disk: str):
    fragments: list[int] = []
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

    checksum = sum([i*int(fragments[i]) for i in range(idx_rvs+1)])
    print (f"🎄 Part 1: {checksum}", end='')

class Fragment:
    def __init__(self, id: int, length: int):
        self.id = id
        self.length = length

    def checksum(self, idx: int) -> int:
        v = 0
        for i in range(self.length):
            v += self.id*(idx+i)
        return v
    
    def __repr__(self) -> str:
        s = ""
        for _ in range(self.length):
            if self.id == -1:
                s += "."
            else:
                s += str(self.id)
        return s

def part2(disk: str):
    fragments: list[Fragment] = []
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

    idx = 0
    checksum = 0
    for f in fragments:
        if f.id != -1:
            checksum += f.checksum(idx)
        idx += f.length
    print (f"🎄🎅 Part 2: {checksum}", end='')

if __name__ == '__main__':
    title = "Day 9: Disk Fragmenter"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_9.txt")

    t0 = time.time()
    part1(inputs)
    print (f" - {time.time()-t0:.5f}")
    
    t0 = time.time()
    part2(inputs)
    print (f" - {time.time()-t0:.5f}")
