import time

def part1():
    val = 20151125
    x = [1, 1]
    final = [3075, 2981]
    ymax = 1
    n = 1
    while x != final:
        if x[1] == 1:
            x[1] = ymax + 1
            ymax = x[1]
            x[0] = 1
        else:
            x[0] = x[0] + 1
            x[1] = x[1] - 1
        n += 1
        val = (val * 252533) % 33554393
    print (f"🎄 Part 1: {val}")
    
if __name__ == "__main__":
    title = "Day 25: Let It Snow"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    t0 = time.time()
    part1()
    print ("Time: {:.5f}".format(time.time()-t0))
