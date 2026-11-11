import time, matplotlib.pyplot as plt

from itertools import combinations

from utils import readInput

def loadInput(filename: str) -> list:
    lines = readInput(filename)
    reds = []    
    for line in lines:
        parts = list(map(int, line.split(",")))
        reds.append((parts[0], parts[1]))
    return reds

def area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def part1(reds: list) -> None:
    max_area = max([area(c1, c2) for c1, c2 in combinations(reds, 2)])
    print (f"🎄 Part 1: {max_area}")

def is_fully_contained(edges: list[tuple[int, int, int, int]], min_x: int, min_y: int, max_x: int, max_y: int) -> bool:
    for e_min_x, e_min_y, e_max_x, e_max_y in edges:
        if min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y:
            return False
    return True

def plot_region(reds: list) -> None:
    x_coords = [v[0] for v in reds]
    y_coords = [v[1] for v in reds]

    fig, ax = plt.subplots()
    ax.fill(x_coords, y_coords, color='skyblue', alpha=0.7, edgecolor='darkblue', linewidth=2)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

def part2(reds: list) -> None:        
    edges = []
    n = len(reds)

    for i in range(n - 1):
        p1 = reds[i]
        p2 = reds[i + 1]
        edges.append((min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1])))

    p_last = reds[-1]
    p_first = reds[0]
    edges.append((min(p_last[0], p_first[0]), min(p_last[1], p_first[1]),
                  max(p_last[0], p_first[0]), max(p_last[1], p_first[1])))

    #plot_region(reds)

    max_area = 0
    for p1, p2 in combinations(reds, 2):
        a = area(p1, p2)
        if a > max_area:
            min_x, max_x = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
            min_y, max_y = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])

            if is_fully_contained(edges, min_x, min_y, max_x, max_y):
                max_area = a

    print (f"🎄🎅 Part 2: {max_area}")

def main():
    title = "Day 9: Playground"
    sub = "❄ "*(len(title)//2-1+2)
    print()
    print(f" {title} ")
    print(sub)

    t0 = time.perf_counter()
    inputs = loadInput("input_9.txt")
    print ("Loding Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part1(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part2(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    main()