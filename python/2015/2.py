import time
from utils import readInput

def loadInput():
    lines = readInput("instructions2a.txt")
    return lines

def part1(lines):
    tot_surf = 0
    for l in lines:
        l = l.split("\n")[0]
        l, w, h = map(int, l.split("x"))
        surf = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
        tot_surf += surf        

    print (f"🎄 Part 1: {tot_surf}")

def part2(lines):
    tot_ribbon = 0
    for l in lines:
        l = l.split("\n")[0]
        l, w, h = map(int, l.split("x"))
        ribbon = h*l*w + min(2*(l+w), 2*(w+h), 2*(h+l))
        tot_ribbon += ribbon
        
    print (f"🎄🎅 Part 2: {tot_ribbon}")
         
if __name__ == "__main__":
    title = "Day 2: I Was Told There Would Be No Math"
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
