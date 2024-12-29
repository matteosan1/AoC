import time

from itertools import product
from operator import __add__, __mul__

from utils import readInput

operators = {"+":__add__, "*":__mul__}

# TRY USING RECURSION
def loadInput(filename: str) -> tuple[list[int], list[list[int]]]:
    lines = readInput(filename)
    results: list[int] = []
    operations: list[list[int]] = []
    for l in lines:
        oper: list[int] = list(map(int, l.split(": ")[1].split(" ")))
        operations.append(oper)
        results.append(int(l.split(": ")[0]))
    return results, operations

def part1(results: list[int], operations: list[list[int]]) -> None:
    valid = 0
    for i in range(len(results)):
        spaces = len(operations[i])-1
        for seq in product(["+", "*"], repeat=spaces):
            result = operations[i][0]
            for j in range(spaces):
                result = operators[seq[j]](result, operations[i][j+1])
                if result > results[i]:
                    break
            if results[i] == result:
                print (results[i], seq)
                valid += result
                break
    print (f"🎄 Part 1: {valid}", end='')

def concat(num1: int, num2: int) -> int:
    return int(str(num1) + str(num2))

def is_sum_concat_possible(nums: list[int], result: int, current: int, index: int) -> int:
    if index == 0:
        return is_sum_concat_possible(nums, result, nums[0], 1)

    if index == len(nums) - 1:
        return (current + nums[index] == result) or (current * nums[index] == result) or (concat(current, nums[index]) == result)

    return is_sum_concat_possible(nums, result, current + nums[index], index + 1) or \
           is_sum_concat_possible(nums, result, current * nums[index], index + 1) or \
           is_sum_concat_possible(nums, result, concat(current, nums[index]), index + 1)

def part2(results: list[int], operations: list[list[int]]) -> None:
    valid = 0
    for i in range(len(operations)):
        if is_sum_concat_possible(operations[i], results[i], 0, 0):
            valid += results[i]
    print (f"🎄🎅 Part 2: {valid}", end='')


if __name__ == '__main__':
    title = "Day 7: Bridge Repair"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_7.txt")

    t0 = time.time()
    part1(*inputs)
    print (f" - {time.time()-t0:.5f}")
    
    t0 = time.time()
    part2(*inputs)
    print (f" - {time.time()-t0:.5f}")
