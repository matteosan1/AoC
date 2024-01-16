import time, copy

from utils import readInput

def loadInput():
    #lines = readInput("prova.txt")
    lines = readInput("input_16.txt")
    input = list(map(int, lines[0]))
    print (input)
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
            #print (p)
            val = 0
            for x in range(len(input)):
                val += (p[x]*fft[x])
                #print (val)
            #print (abs(val)%10)
            temp.append(abs(val)%10)
        fft = temp
    print ("".join([str(t) for t in fft[:8]]))

    print (f"🎅 Part 1: {0}")
    
def part2(moons):
    init = copy.deepcopy(moons)
    period = [0 for _ in range(3)]
    cycles = 1
    while True:
        move(moons)
        cycles += 1
        for coord in range(3):
            if period[coord] == 0:
                if all([moons[i][coord] == init[i][coord] for i in range(len(moons))]):
                    period[coord] = cycles
        if all([p != 0 for p in period]):
            break
    print (f"🎅🎄 Part 2: {math.lcm(*period)}")


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
    
    #t0 = time.time()
    #part2(inputs)
    #print ("Time: {:.5f}".format(time.time()-t0))

    
