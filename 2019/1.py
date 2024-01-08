import time
from utils import readInput

def loadInput():
    lines = readInput("input_1.txt")
    ships = list(map(int, lines))
    return ships

def get_fuel(mass, tot_fuel=0):
    new_mass = mass//3-2
    print (new_mass)
    if new_mass > 0:
        tot_fuel += new_mass
        return get_fuel(new_mass, tot_fuel)
    else:
        return tot_fuel
    
def part1(ships):
    fuel = 0
    for s in ships:
        fuel += s//3-2
    print (f"🎄 Part 1: {fuel}")

def part2(ships):
    fuel = 0
    for s in ships:
        fuel += get_fuel(s)
    print (f"🎄🎅 Part 2: {fuel}")

if __name__ == "__main__":
    title = "Day 1: The Tyranny of the Rocket Equation"
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

    
