import time, numpy as np

from collections import deque
from scipy.optimize import linprog

from utils import readInput

def loadInput(filename: str) -> tuple:
    indicators = []
    buttons = []
    joltages = []

    lines = readInput(filename)
    for line in lines:
        _indicators, *_buttons, _joltages = line.split(" ")        
        indicators.append(list(int(i == "#") for i in _indicators[1:-1]))
        buttons.append([list(map(int, x[1:-1].split(","))) for x in _buttons])
        joltages.append(list(map(int, _joltages[1:-1].split(","))))
    return (indicators, buttons, joltages)

def solve(indicator: list, buttons: list):
    target = tuple(indicator)
    num = len(indicator)
    curr = tuple(False for _ in range(num))

    visited = {curr: 0}
    queue = deque([curr])

    while queue:
        curr = queue.popleft()
        times = visited[curr] + 1

        for btn in buttons:
            next_curr = tuple(not curr[i] if i in btn else curr[i] for i in range(num))

            if next_curr not in visited:
                if next_curr == target:
                    return times
                visited[next_curr] = times
                queue.append(next_curr)
 
def part1(indicators: list, buttons: list) -> None:
    c = sum(solve(indicator, button) for indicator, button in zip(indicators, buttons))    
    print (f"🎄 Part 1: {c}")    

def solve2(joltage: list, buttons: list):
    joltage = np.array(joltage)
    for i in range(len(buttons)):
        buttons[i] = np.array([1 if j in buttons[i] else 0 for j in range(len(joltage))])
    buttons = np.array(buttons).T
    num_buttons = buttons.shape[1]

    c = np.ones(num_buttons)
    bounds = [(0, None)] * num_buttons
    integrality = np.ones(num_buttons, dtype=int)
    result = linprog(c, A_eq=buttons, b_eq=joltage, bounds=bounds, integrality=integrality)
    return result.fun

def part2(joltages: list, buttons: list) -> None:
    c = sum(solve2(joltage, button) for joltage, button in zip(joltages, buttons))
    print (f"🎄🎅 Part 2: {int(c)}")

def main():
    title = "Day 10: Factory"
    sub = "❄ "*(len(title)//2-1+2)
    print()
    print(f" {title} ")
    print(sub)

    t0 = time.perf_counter()
    inputs = loadInput("input_10.txt")
    print ("Loding Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part1(inputs[0], inputs[1])
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part2(inputs[2], inputs[1])
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    main()