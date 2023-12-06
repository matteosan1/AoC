import time
from numpy import sqrt, prod

from utils import readInput

def loadInput():
    lines = readInput("input_6.txt")
    return lines 

def find_interval(times, distances):
    diff = (times + sqrt(times**2 - 4*distances)) // 2 - (times - sqrt(times**2 - 4*distances)) // 2
    return diff

def part1(lines):
    times = list(map(int, lines[0][5:].split()))
    distances = list(map(int, lines[1][9:].split()))
    
    counts = []
    for it, best_time in enumerate(times):
        counts.append(find_interval(times[it], distances[it]))
        
    print (f"🎄 Part 1: {prod(counts)}")
    
def part2(lines):
    times = int("".join(lines[0][5:].split()))
    distances = int("".join(lines[1][9:].split()))    
    print (f"🎄🎅 Part 2: {find_interval(times, distances)}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 5         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(inputs)
print (f"Time: {time.time()-t0:.5f}")
