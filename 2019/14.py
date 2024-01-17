import time

from collections import defaultdict
from math import ceil

from utils import readInput

def loadInput():
    #lines = readInput("prova.txt")
    lines = readInput("input_14.txt")
    def parse_chem(s):
        units, name = s.split(' ')
        return int(units), name

    reactions = {}
    for reaction in lines:
        input, output = reaction.split(' => ')
        inputs = []
        for chem in input.split(', '):
            inputs.append(parse_chem(chem))
        out_units, out_chem = parse_chem(output)
        reactions[out_chem] = (out_units, inputs)
    return reactions

def minimum_ore(reactions, chem='FUEL', units=1, waste=None):
    if waste is None:
        waste = defaultdict(int)

    if chem == 'ORE':
        return units

    # Re-use waste chemicals.
    reuse = min(units, waste[chem])
    units -= reuse
    waste[chem] -= reuse

    # Work out how many reactions we need to perform.
    produced, inputs = reactions[chem]
    n = ceil(units / produced)

    # Determine the minimum ore required to produce each input.
    ore = 0
    for required, input in inputs:
        ore += minimum_ore(reactions, input, n * required, waste)

    # Store waste so it can be re-used
    waste[chem] += n * produced - units
    return ore
    
def part1(reactions):
    ore = minimum_ore(reactions)
    print (f"ðŸŽ… Part 1: {ore}")
    
def part2(reactions):
    target = 1000000000000
    lower = None
    upper = 1

    # Find upper bound.
    while minimum_ore(reactions, units=upper) < target:
        lower = upper
        upper *= 2

    # Binary search to find maximum fuel produced.
    while lower + 1 < upper:
        mid = (lower + upper) // 2
        ore = minimum_ore(reactions, units=mid)
        if ore > target:
            upper = mid
        elif ore < target:
            lower = mid

    print (f"ðŸŽ…ðŸŽ„ Part 2: {lower}")

if __name__ == "__main__":
    title = "Day 14: Space Stoichiometry"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
