import time, re

r1 = re.compile(r"(\d)\1{1,}")

def check(n, part=1):
    if part == 1:
        g = r1.findall(str(n))
        if len(g) > 0:
            return True
    else:
        s = str(n)
        repeat = 1
        old = s[0]
        for i in range(1, len(s)):
            if s[i] == old:
                repeat += 1
            else:
                if repeat == 2:
                    return True
                old = s[i]
                repeat = 1
        if repeat == 2:
            return True
    return False

def main_loop(part=1):
    counter = 0
    for i1 in range(1, 6):
        for i2 in range(i1, 10):
            for i3 in range(i2, 10):
                for i4 in range(i3, 10):
                    for i5 in range(i4, 10):
                        for i6 in range(i5, 10):
                            n = i1*100000+i2*10000+i3*1000+i4*100+i5*10+i6
                            if n > 576723:
                                return counter
                            if check(n, part):
                                counter += 1
def part1():
    c = main_loop()
    print (f"🎅 Part 1: {c}")

def part2():
    c = main_loop(2)
    print (f"🎅🎄 Part 2: {c}")

if __name__ == "__main__":
    title = "Day 4: Secure Container"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
        
    t0 = time.time()
    part1()
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2()
    print ("Time: {:.5f}".format(time.time()-t0))
