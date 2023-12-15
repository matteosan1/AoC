import time
from utils import readInput

def loadInput():
    with open("input_15.txt", "r") as f:
        line = f.readline()
    instructions = line[:-1].split(",")
    return instructions

def hash_algo(instr):
    val = 0
    for c in instr:
        val += ord(c)
        val *= 17
        val %= 256
    return val
    
def part1(inputs):
    codes = []
    for instr in inputs:
        codes.append(hash_algo(instr))
    return sum(codes)

def focusing_power(boxes):
    val = 0
    for nb, box in boxes.items():
        val += sum([(nb+1) * (i+1) * b for i,b in enumerate(box.values())])
    return val
    
def part2(inputs):
    boxes = {k:{} for k in range(0, 256)}
    for instr in inputs:
        add = True
        if "=" in instr:
            label, value = instr.split("=")
        else:
            add = False
            label = instr[:-1]
        box = hash_algo(label)
        if not add and label in boxes[box]:
            del boxes[box][label]
        elif add:
            boxes[box][label] = int(value)
                
    return focusing_power(boxes)

if __name__ == '__main__':
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    print("⛄ Day 15: Lens Library ⛄")
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
