import time, copy, numpy as np

from utils import readInput

def loadInput():
    lines = readInput("input_16.txt")
    input = list(map(int, lines[0]))
    return input

def pattern(phase, length):
    c = phase+1
    pattern = [0]*c + [1]*c + [0]*c + [-1]*c
    if len(pattern) <= length:
        pattern = pattern*((length//len(pattern))+1)
    return pattern[1:length+1]
    
def part1(input):
    fft = copy.deepcopy(input)
    for phase in range(100):
        temp = []
        for i in range(len(input)):
            p = pattern(i, len(input))
            val = 0
            for x in range(len(input)):
                val += (p[x]*fft[x])
            temp.append(abs(val)%10)
        fft = temp
    print (f"🎅 Part 1: {''.join(list(map(str, fft[:8])))}")
    
def part2(input):
    offset = int("".join([str(t) for t in input[:7]]))
    input = np.array(list(reversed((input*10000)[offset:])))
    for phase in range(100):
        fft = np.mod(np.cumsum(input), 10)
        input = fft.copy()
    print (f"🎅🎄 Part 2: {''.join(list(map(str, reversed(input[-8:]))))}")

if __name__ == "__main__":
    title = "Day 16: Flawed Frequency Transmission"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(copy.deepcopy(inputs))
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

    
