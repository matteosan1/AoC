import time

from utils import readInput

def loadInput(filename: str) -> dict:
    nodes = {}
    lines = readInput(filename)
    for line in lines:
        parts = line.split(":")
        nodes[parts[0]] = parts[1].split()
    return nodes

def dfs(nodes: dict, start: str = "you", end:str = "out") -> list:
    all_paths = []

    def dfs_helper(current_node, current_path):
        current_path = current_path + [current_node]
        if current_node == end:
            all_paths.append(current_path)
            return
        
        if current_node in nodes:
            for neighbor in nodes[current_node]:
                if neighbor not in current_path:
                    dfs_helper(neighbor, current_path)
    dfs_helper(start, [])
    return all_paths

def part1(nodes: dict) -> None:
    paths = dfs(nodes)
    print (f"🎄 Part 1: {len(paths)}")

def dfs_memoized(graph, start_node, end_node, memo=None):
    if memo is None:
        memo = {}
   
    memo_key = (start_node, end_node)
    if memo_key in memo:
        return memo[memo_key]

    if start_node == end_node:
        return 1
    
    if start_node not in graph:
        return 0
    
    count = 0
    for neighbor in graph.get(start_node, []):
        count += dfs_memoized(graph, neighbor, end_node, memo)
    memo[memo_key] = count
    return count

def part2(nodes: dict) -> None:
    memo = {}
    Psa = dfs_memoized(nodes, "svr", "dac", memo)
    Pba = dfs_memoized(nodes, "fft", "dac", memo)
    memo = {}
    Pbe = dfs_memoized(nodes, "fft", "out") 
    Pae = dfs_memoized(nodes, "dac", "out")
    memo = {}
    Pab = dfs_memoized(nodes, "dac", "fft")
    Psb = dfs_memoized(nodes, "svr", "fft")
    print (f"🎄🎅 Part 2: {(Psa * Pab * Pbe) + (Psb * Pba * Pae)}")

def main():
    title = "Day 11: Reactor"
    sub = "❄ "*(len(title)//2-1+2)
    print()
    print(f" {title} ")
    print(sub)

    t0 = time.perf_counter()
    inputs = loadInput("input_11.txt")
    print ("Loding Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part1(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

    t0 = time.perf_counter()
    part2(inputs)
    print ("Time: {:.5f}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    main()