import time, networkx as nx, random, graphviz

from dataclasses import dataclass
from collections import defaultdict

from utils import readInput

@dataclass(frozen=True)
class Graph:
    edges: dict
    def add_edge(self, u, v):
        self.edges[u].add(v)
        self.edges[v].add(u)
    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        self.edges[v].remove(u)
    def visualise(self):
        dot = graphviz.Graph(format='svg')
        for u, nbrs in self.edges.items():
            for v in nbrs:
                if u < v:
                    dot.edge(u, v)
        dot.render()
    def remove_node(self, u):
        for v in self.edges[u]:
            self.edges[v].remove(u)
        del self.edges[u]
    def get_component_size(self, u):
        q = [u]
        visited = {u}
        while q:
            current = q.pop()
            for nbr in self.edges[current]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        return len(visited)

def preload():
    g = Graph(defaultdict(set))
    with open('input_25.txt', 'r') as f:
        for line in f.readlines():
            left, right = line.strip().split(': ')
            for v in right.split():
                g.add_edge(left, v)

    n = len(g.edges)
    # these bridge edges were found by eye by visualising with graphviz
    g.visualise()
    #g.remove_edge('psj', 'fdb')
    #g.remove_edge('ltn', 'trh')
    #g.remove_edge('rmt', 'nqh')
    
    #k = g.get_component_size('psj')
    #print(k * (n-k))

def loadInput():
    lines = readInput("prova.txt")
    lines = readInput("input_25.txt")
    components = {}
    for l in lines:
        parts = l.replace(":", "").split()
        for p in parts[1:]:
            components.setdefault(parts[0], []).append(p)
            components.setdefault(p, []).append(parts[0])
    return components

def part1(components):
    gr = nx.Graph()

    for k, v in components.items():
        for p in v:
            gr.add_edge(k, p, capacity=1)
    while True:
        nodes = list(gr.nodes())
        a, b = random.choices(nodes, k=2)
        if a == b:
            continue
        cut, partition = nx.minimum_cut(gr, a, b)
        if cut == 3:
            return len(partition[0])*len(partition[1])
            break

if __name__ == '__main__':
    title = "Day 25: Snowverload"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)

    preload()
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f})")
