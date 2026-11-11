import time

from collections import Counter

from utils import readInput

def loadInput(filename: str) -> list:
    lines = readInput(filename)
    return lines

def part1(rotations: list) -> None:
    counts = 0
    pos = 50
    for r in rotations:
        dir = r[0]
        val = int(r[1:])
        if dir == "L":
            pos -= val
        else:
            pos += val
        pos %= 100
        if pos == 0:
            counts += 1     
    print (f"🎄 Part 1: {counts}")

def count_zeros_in_rotation(start_pos: int, direction: str, distance: int) -> int:
    if direction == 'R':
        clicks_to_first_zero = 100 - start_pos            
    elif direction == 'L':
        clicks_to_first_zero = start_pos if start_pos != 0 else 100       

    if distance >= clicks_to_first_zero:
        zero_count = 1
        remaining_distance = distance - clicks_to_first_zero
        zero_count += remaining_distance // 100     
        return zero_count
    return 0

def part2(rotations: list[str]) -> None:
    current_pos = 50
    total_zeros = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        zeros_hit = count_zeros_in_rotation(current_pos, direction, distance)
        total_zeros += zeros_hit
        
        if direction == 'R':
            current_pos = (current_pos + distance) % 100
        elif direction == 'L':
            current_pos = (current_pos - distance) % 100            
    print (f"🎄🎅 Part 2: {total_zeros}")

def main():
    title = "Day 1: Secret Entrance"
    sub = "❄ "*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_1.txt")
    
    t0 = time.perf_counter()
    part1(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))
    
    t0 = time.perf_counter()
    part2(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    main()