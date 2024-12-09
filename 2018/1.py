import time

from utils import readInput


def loadInput():
    lines = readInput("input_1.txt")
    return list(map(int, lines))

def get_fuel(mass, tot_fuel=0):
    new_mass = mass//3-2
    print (new_mass)
    if new_mass > 0:
        tot_fuel += new_mass
        return get_fuel(new_mass, tot_fuel)
    else:
        return tot_fuel
    
def part1(freqs):
    freq = 0
    for f in freqs:
        freq += f
    print (f"🎄 Part 1: {freq}")

def part2(freqs):
    old_freqs = []
    freq = 0
    while True:
        for f in freqs:
            print (freq)
            freq += f
            if freq in old_freqs:
                print (f"🎄🎅 Part 2: {freq}")
                return
            old_freqs.append(freq)

if __name__ == "__main__":
    title = "Day 1: Chronal Calibration"
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

    
