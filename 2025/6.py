import time, numpy as np, re

from utils import readInput

def loadInput(filename: str) -> list:
    return readInput(filename)
    
def part1(lines: list) -> None:
    numbers = []
    for y in range(len(lines)-1):
        numbers.append(list(map(int, re.split(r"\s+", lines[y].strip()))))
    operators = re.split(r"\s+", lines[-1].strip())
    numbers = np.array(numbers)
    
    grand_total = 0
    for col in range(numbers.shape[1]):
        if operators[col] == "+":
            grand_total += np.sum(numbers[:, col])
        else:
            grand_total += np.prod(numbers[:, col])
    print (f"🎄 Part 1: {grand_total}", end='')

def part2():
    with open("input_6.txt") as f:
        lines = f.readlines()
    numbers = []
    for i in range(len(lines)-1):
        numbers.append(list(lines[i].split("\n")[0])[::-1])
    numbers = list(zip(*numbers))
    operators = re.split(r"\s+", lines[-1].strip())[::-1]

    grand_total = 0
    operation = 0
    result = 0
    for i in range(len(numbers)):
        cephal_number = "".join(numbers[i])
        if cephal_number == "    ":
            grand_total += result
            result = 0
            operation += 1
        else:
            if operators[operation] == "+":
                result += int(cephal_number)
            else:
                if result == 0:
                    result = int(cephal_number)
                else:
                    result *= int(cephal_number)
    grand_total += result
    print (f"🎄🎅 Part 2: {grand_total}", end='')

def main():
    title = "Day 6: Trash Compactor"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_6.txt")
    
    t0 = time.perf_counter()
    part1(inputs)
    print (" - {:.5f}".format(time.perf_counter()-t0))
    
    t0 = time.perf_counter()
    part2()
    print (" - {:.5f}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    main()