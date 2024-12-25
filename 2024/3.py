import time, re, math

from utils import readInput

def loadInput(filename: str) -> list[str]:
    return readInput(filename)
    
def part1(memory: list[str]) -> None:
    r = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    tot = 0
    for mem in memory:
        matches = r.findall(mem)
        for m in matches:
            tot += math.prod(list(map(int, m)))
    print (f"🎄 Part 1: {tot}")

def part2(memory: list[str]) -> None:
    r = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    enabled = True
    tot = 0
    for mem in memory:
        matches = r.findall(mem)
        for m in matches:
            if m == "do()":
                enabled = True
            elif m == "don't()":
                enabled = False
            else:
                if enabled:
                    m = list(map(int, m[4:-1].split(",")))
                    tot += math.prod(list(map(int, m)))
    print (f"🎄🎅 Part 2: {tot}")

if __name__ == "__main__":
    title = "Day 3: Mull It Over"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_3.txt")
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
