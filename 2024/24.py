import timeit

from utils import readInput

def loadInput():
    lines = readInput("input_24_prova.txt")
    #lines = readInput("input_24.txt")
    graph = {}
    return graph

def part1(connections):
    print (f"🎄 Part 1: {count_t_sets}")
    
def part2(graph):    
    print (f"🎄🎅 Part 2: {graph}")

if __name__ == '__main__':
    title = "Day 24: "
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print (f"{t2*1000:.3f} ms")
