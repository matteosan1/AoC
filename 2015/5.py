import time

from utils import readInput

def loadInput():
    lines = readInput("instructions5a.txt")
    return lines

vowels = ("a", "e", "i", "o", "u")
def check_vowels(m):   
    v = 0 
    for c in m:
        if c in vowels:
            v += 1
    if v >= 3:
        return True
    else:
        return False

def check_repeated(m):
    for ic in range(0, len(m)-1):                    
        if m[ic] == m[ic+1]:
            return True
    return False

bad = ("ab", "cd", "pq", "xy")
def check_bad(m):
    for b in bad:
        if b in m:
            return True
    return False

def part1(msgs):
    good_msg = 0
    for m in msgs:
        if check_bad(m):
            continue

        if check_vowels(m) and check_repeated(m):
            good_msg += 1
    print (f"🎄 Part 1: {good_msg}")

def check_better_rules(m):
    last_pair = ""
    for ic in range(0, len(m)-3):
        pair = m[ic:ic+2]
        if pair in m[ic+2:]:
            for ic in range(0, len(m)-2):                    
                if m[ic] == m[ic+2]:
                    return True
    return False

def part2(msgs):
    good_msg = 0
    for m in msgs:
        if check_better_rules(m):
            good_msg += 1
        
    print (f"🎄🎅 Part 2: {good_msg}")

if __name__ == "__main__":
    title = "Day 5: Doesn't He Have Intern-Elves For This?"
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
