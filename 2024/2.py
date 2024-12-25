import time

from itertools import combinations

from utils import readInput

def loadInput(filename: str) -> list[list[int]]:
    lines = readInput(filename)
    reports: list[list[int]] = []
    for l in lines:
        reports.append(list(map(int, l.split())))
    return reports

def check_safe(diffs: list[int]) -> bool:
    if all(0 < d <= 3 for d in diffs) or all(-3 <= d < 0 for d in diffs):
        return True
    return False
    
def part1(reports: list[list[int]]) -> None:
    n = 0
    for report in reports:
        n += check_safe([report[i]-report[i-1] for i in range(1, len(report))])
    print (f"🎄 Part 1: {n}")

def problem_dampener(report: list[int]) -> bool:
    for c in combinations(report, len(report)-1):
        diffs: list[int] = [c[i]-c[i-1] for i in range(1, len(c))]
        if check_safe(diffs):
            return True
    return False

def part2(reports: list[list[int]]) -> None:
    n = 0
    for report in reports:
        diffs: list[int] = [report[i]-report[i-1] for i in range(1, len(report))]
        if check_safe(diffs) or problem_dampener(report):
            n += 1
    print (f"🎄🎅 Part 2: {n}")

if __name__ == "__main__":
    title = "Day 2: Red-Nosed Reports"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_2.txt")
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
