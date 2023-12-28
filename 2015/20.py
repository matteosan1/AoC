import time, numpy as np

def run():
    BIG_NUM = 1000000  # try larger numbers until solution found
    goal = 34000000
    houses_a = np.zeros(BIG_NUM)
    houses_b = np.zeros(BIG_NUM)

    for elf in range(1, BIG_NUM):
        houses_a[elf::elf] += 10 * elf
        houses_b[elf:(elf+1)*50:elf] += 11 * elf
    return np.nonzero(houses_a >= goal)[0][0], np.nonzero(houses_b >= goal)[0][0]

def part1():
    a, b = run()
    print (f"🎄 Part 1: {a}")
    return b

def part2(b):
    print (f"🎄🎅 Part 2: {b}")
    
if __name__ == "__main__":
    title = "Day 20: Infinite Elves and Infinite Houses"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    #inputs = loadInput()
    
    t0 = time.time()
    b = part1()
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(b)
    print ("Time: {:.5f}".format(time.time()-t0))

