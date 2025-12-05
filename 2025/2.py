import time, re

from utils import readInput

def loadInput(filename: str) -> list[list[int]]:
    lines = readInput(filename)
    ranges = [list(map(int, r.split("-"))) for r in lines[0].split(",")]
    return ranges
    
def find_repeated_sequence_numbers(start: int, end: int) -> list[int]:
    matching_numbers = []

    for n in range(start, end + 1):
        s = str(n)
        length = len(s)

        if length % 2 == 0:
            half_length = length // 2

            first_half = s[:half_length]
            second_half = s[half_length:]

            if first_half == second_half:
                matching_numbers.append(n)

    return matching_numbers

def part1(ranges: list[list[int]]) -> None:
    invalid = []
    for r in ranges:
        invalid += find_repeated_sequence_numbers(r[0], r[1])
    print (f"🎄 Part 1: {sum(invalid)}")

repeated = re.compile(r"^(..*?)\1{1,}$")

def find_invalid_numbers_in_range(start: int, end: int) -> list[int]:
    invalid_numbers = []
    for n in range(start, end + 1):
        s = str(n)
        length = len(s)

        if length < 2:
            continue
        if repeated.match(s) is not None:
            invalid_numbers.append(n)
    return invalid_numbers

def part2(ranges: list[list[int]]) -> None:
    invalid = []
    for r in ranges:
        invalid += find_invalid_numbers_in_range(r[0], r[1])
    print (f"🎄🎅 Part 2: {sum(set(invalid))}")

if __name__ == "__main__":
    title = "Day 2: Gift Shop"
    sub = "❄ "*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_2.txt")
    
    t0 = time.perf_counter()
    part1(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))
    
    t0 = time.perf_counter()
    part2(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))
