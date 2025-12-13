import time

def loadInput(filename: str) -> tuple:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    sections = content.strip().split("\n\n")
    region_section = sections[-1]

    regions = []
    for line in region_section.split("\n"):
        if not line or ": " not in line:
            continue
        area_part, nums_part = line.split(": ", 1)
        if "x" not in area_part:
            continue

        width, height = map(int, area_part.split("x"))
        nums = list(map(int, nums_part.split()))
        regions.append((width, height, nums))

    patterns = [section.count("#") for section in sections[:-1]]
    return (patterns, regions)

def part1(patterns: list, regions: list) -> None:
    filled_regions = 0
    for region in regions:
        area = region[0] * region[1]
        size = sum(p * n for p, n in zip(patterns, region[2]))
        if size <= area:
            filled_regions += 1

    print (f"🎄 Part 1: {filled_regions}")

def main():
    title = "Day 12: Christmas Tree Farm"
    sub = "❄ "*(len(title)//2-1+2)
    print()
    print(f" {title} ")
    print(sub)

    inputs = loadInput("input_12.txt")
    t0 = time.perf_counter()
    part1(*inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    main()