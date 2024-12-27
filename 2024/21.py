import time

from functools import cache
from itertools import pairwise

from utils import readInput

# CONVERT TO USE CACHE
numeric_pad = {'7': 0, '8': 1, '9': 2, '4': 1j, '5': (1+1j), 
               '6': (2+1j), '1': 2j, '2': (1+2j), '3': (2+2j), '0': (1+3j), 'A': (2+3j)}

remote_pad = {'^': 1, 'A': 2, '<': 1j, 'v': (1+1j), '>': (2+1j)}

def loadInput(filename):
    codes = readInput(filename)
    return codes

def possible_paths(key1, key2, keypad):
    pos1, pos2 = keypad[key1], keypad[key2]
    dp = pos2 - pos1
    horizontal = abs(int(dp.real)) * ('>' if dp.real > 0 else '<')
    vertical   = abs(int(dp.imag)) * ('v' if dp.imag > 0 else '^')
    if pos1 + complex(dp.real, 0) in keypad.values():
        yield horizontal + vertical + 'A'
    if pos1 + complex(0, dp.imag) in keypad.values(): 
        yield vertical + horizontal + 'A'

def complexity(code, num_presses: int): 
    return int(code[:-1]) * num_presses

def min_keypresses(code: str, levels: int, numeric_keypad=numeric_pad, remote_keypad=remote_pad) -> int:
    def total_presses(keys: str, level: int) -> int:
        return sum(one_button_path_lengths[level, key1, key2] 
                   for key1, key2 in pairwise('A' + keys))
    
    one_button_path_lengths = {(0, key1, key2): 1
                               for key1 in remote_keypad for key2 in remote_keypad}
    for level in range(1, levels):
        keypad = numeric_keypad if level == levels - 1 else remote_keypad
        for key1 in keypad:
            for key2 in keypad:
                paths = possible_paths(key1, key2, keypad)
                one_button_path_lengths[level, key1, key2] = min(total_presses(path, level - 1) for path in paths)
    return total_presses(code, levels - 1)

def part1(codes):
    print (f"🎄 Part 1: {sum(complexity(code, min_keypresses(code, levels=4)) for code in codes)}", end='')

def part2(codes):
    print (f"🎄🎅 Part 2: {sum(complexity(code, min_keypresses(code, levels=27)) for code in codes)}", end='')

if __name__ == '__main__':
    title = "Day 21: Keypad Conundrum"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_21.txt")

    t0 = time.time()
    part1(inputs)
    print (" - {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print (" - {:.5f}".format(time.time()-t0))