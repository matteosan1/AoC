import time

from utils import readInput, ALL_DIRECTIONS

diagonal_pairs: tuple[tuple[int, int], ...] = ((1, 3), (7, 5), (1, 7), (3, 5))

def loadInput(filename: str) -> dict[complex, str]:
    lines = readInput(filename)
    xwords: dict[complex, str] = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            xwords[complex(x, y)] = lines[y][x]
    return xwords

def find_word(xwords: dict[complex, str], start: complex, dir: complex, word: str) -> bool:
    return all(xwords.get(start + i*dir, "") == word[i] for i in range(len(word)))

def part1(xwords: dict[complex, str], word:str="XMAS"):
    occurrencies: int = sum([find_word(xwords, start, dir, word)                    
           for start in xwords if xwords[start] == word[0] for dir in ALL_DIRECTIONS.values()])
    print (f"🎄 Part 1: {occurrencies}", end='')

def part2(xwords: dict[complex, str], word: str="MAS"):
    occurrencies: int = sum([find_word(xwords, mid_pos-ALL_DIRECTIONS[dir1], 
                                       ALL_DIRECTIONS[dir1], word) and
                             find_word(xwords, mid_pos-ALL_DIRECTIONS[dir2], 
                                       ALL_DIRECTIONS[dir2], word)
                             for mid_pos in xwords if xwords[mid_pos] == word[1] 
                             for dir1, dir2 in diagonal_pairs])
    print (f"🎄🎅 Part 2: {occurrencies}", end='')

if __name__ == "__main__":
    title = "Day 4: Ceres Search"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_4.txt")
    
    t0 = time.time()
    part1(inputs)
    print (" - {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print (" - {:.5f}".format(time.time()-t0))
