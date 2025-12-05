import time

from utils import readInput

def loadInput(filename: str) -> list[str]:
    return readInput(filename)
    
def find_max(bank, start, end):
    val = max(bank[start:end])
    return val, bank[start:end].index(val)
    
def part1(banks: list[str]) -> None:
    tot_joltage = 0
    for bank in banks:
        bank = [int(digit) for digit in bank]
        joltage, index = find_max(bank, 0, len(bank)-1)
        joltage = joltage*10 + find_max(bank, index+1, len(bank))[0]
        tot_joltage += joltage
    print (f"🎄 Part 1: {tot_joltage}")

def part2(banks: list[str]) -> None:
    tot_joltage = 0
    for bank in banks:
        bank = [int(digit) for digit in bank]
        joltage = []
        start = 0
        end = len(bank) - 11
        for i in range(12):
            jolt, index = find_max(bank, start, end)
            joltage.append(jolt) 
            start += index + 1
            end = len(bank) - 11 + i + 1
        joltage = int("".join(map(str, joltage)))
        tot_joltage += joltage
    print (f"🎄🎅 Part 2: {tot_joltage}")

if __name__ == "__main__":
    title = "Day 3: Lobby"
    sub = "❄ "*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_3.txt")
    
    t0 = time.perf_counter()
    part1(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))
    
    t0 = time.perf_counter()
    part2(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))
