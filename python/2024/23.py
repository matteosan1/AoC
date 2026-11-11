import time

from utils import readInput

# CHANGE FIRST PART TO USE DICT OF SETS 

def loadInput(filename):
    lines = readInput(filename)
    connections = []
    for l in lines:
        connections.append([*l.split("-")])
    graph = {}
    for c1, c2 in connections:
        graph.setdefault(c1, []).append(c2)
        graph.setdefault(c2, []).append(c1)
    return graph

def find_lan_party_sets(graph):
    sets_of_three = []
    for computer in graph:
        neighbors = graph[computer]
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if neighbors[i] in graph[neighbors[j]]:
                    sets_of_three.append(set(sorted([computer, neighbors[i], neighbors[j]])))
    sets_of_three = [set(s) for s in set(frozenset(s) for s in sets_of_three)]
    return sets_of_three

def part1(connections):
    sets_of_three = find_lan_party_sets(connections)

    count_t_sets = 0
    for s in sets_of_three:
        if any(computer.startswith("t") for computer in s):
            count_t_sets += 1
    print (f"🎄 Part 1: {count_t_sets}", end='')
    
def bron_kerbosch(R, P, X, graph):
    """
    Finds all maximal cliques in an undirected graph using the Bron-Kerbosch algorithm.

    Args:
        R: Set of vertices already in the current clique.
        P: Set of candidate vertices to be added to the current clique.
        X: Set of vertices that cannot be added to the current clique.
        graph: A dictionary representing the graph, where keys are nodes and values are 
              sets of neighboring nodes.

    Yields:
        Maximal cliques found in the graph.
    """
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(R | {v}, P & graph[v], X & graph[v], graph)
        X.add(v)

def part2(graph):    
    graph = {k:set(v) for k, v in graph.items()}
    all_cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))
    largest_clique = sorted(max(all_cliques, key=len, default=[]))
    print (f"🎄🎅 Part 2: {",".join(sorted(max(all_cliques, key=len, default=[])))}", end='')

if __name__ == '__main__':
    title = "Day 23: LAN Party"
    sub = "❄ "*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_23.txt")
    
    t0 = time.time()
    part1(inputs)
    print (" - {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print (" - {:.5f}".format(time.time()-t0))