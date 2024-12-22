import timeit, networkx as nx

from collections import deque
from functools import cache

from utils import readInput

K1 = nx.DiGraph()
K1.add_edges_from([("A", "0"), ("A", "3")])
K1.add_edges_from([("0", "2"), ("0", "A")])
K1.add_edges_from([("1", "4"), ("1", "2")])
K1.add_edges_from([("2", "1"), ("2", "5"), ("2", "3"), ("2", "0")])
K1.add_edges_from([("3", "2"), ("3", "6"), ("3", "A")])
K1.add_edges_from([("4", "7"), ("4", "5"), ("4", "1")])
K1.add_edges_from([("5", "4"), ("5", "8"), ("5", "6"), ("5", "2")])
K1.add_edges_from([("6", "5"), ("6", "9"), ("6", "3")])
K1.add_edges_from([("7", "8"), ("7", "4")])
K1.add_edges_from([("8", "7"), ("8", "5"), ("8", "9")])
K1.add_edges_from([("9", "8"), ("9", "6")])

K1move = {
    ('A', '0'): '<', ('A', '3'): '^',
    ('0', '2'): '^', ('0', 'A'): '>',
    ('1', '4'): '^', ('1', '2'): '>', 
    ('2', '1'): '<', ('2', '5'): '^', ('2', '3'): '>', ('2', '0'): 'v',
    ('3', '2'): '<', ('3', '6'): '^', ('3', 'A'): 'v', 
    ('4', '7'): '^', ('4', '5'): '>', ('4', '1'): 'v', 
    ('5', '4'): '<', ('5', '8'): '^', ('5', '6'): '>', ('5', '2'): 'v', 
    ('6', '5'): '<', ('6', '9'): '^', ('6', '3'): 'v',
    ('7', '8'): '>', ('7', '4'): 'v', 
    ('8', '7'): '<', ('8', '5'): 'v', ('8', '9'): '>', 
    ('9', '8'): '<', ('9', '6'): 'v'
}

def loadInput():
    codes = readInput("input_21.txt")
    #codes = ["029A", "980A", "179A", "456A", "379A"]
    return codes

def pathsK1(A, B):
    paths = []
    for p in nx.all_shortest_paths(K1, A, B):
        seq = []
        for i in range(len(p)-1):
            move = (p[i], p[i+1])
            seq += [K1move[move]]
        seq += ['A']
        paths.append("".join(seq))
    return paths

def solveK1(code):
    paths = []
    _code = "A" + code
    for i in range(len(_code)-1):
        paths.append(pathsK1(_code[i], _code[i+1]))
    sequences = [""]
    i = 0
    while i < len(paths):
        sequences_new = []
        for s in sequences:
            for p in paths[i]:
                sequences_new.append(s+p)
        sequences = sequences_new
        i += 1
    return sequences

K2 = nx.DiGraph()
K2.add_edges_from([("A", "^"), ("A", ">")])
K2.add_edges_from([("^", "A"), ("^", "v")])
K2.add_edges_from([("<", "v")])
K2.add_edges_from([("v", "<"), ("v", "^"), ("v", ">")])
K2.add_edges_from([(">", "v"), (">", "A")])

K2move = {
    ('A', '^'): "<", ('A', '>'): "v",
    ('^', 'A'): ">", ('^', 'v'): "v",
    ('<', 'v'): ">",
    ('v', '<'): "<", ('v', '^'): "^", ('v', '>'): ">",
    ('>', 'v'): "<", ('>', 'A'): "^",
}

def pathsK2(A,B):
    paths = []
    for p in nx.all_shortest_paths(K2,A,B):
        seq = []
        for i in range(len(p)-1):
            move = (p[i],p[i+1])
            seq += [ K2move[move] ]
        seq += ['A'] # press A
        paths.append("".join(seq))
    return paths

def solveK2(code):
    paths = []
    _code = "A"+code
    for i in range(len(_code)-1):
        paths.append(pathsK2(_code[i],_code[i+1]))
    sequences = [""]
    i = 0
    while i<len(paths):
        sequences_new = []
        for s in sequences:
            for p in paths[i]:
                sequences_new.append(s+p)
        sequences = sequences_new
        i+=1
    return sequences

def solve_code(code,nk2=2):
    solutions = set( solveK1(code) )
    nk = 0
    while True:
        nk+=1
        solutions_next = set()
        while len(solutions):
            s = solutions.pop()
            for k2 in solveK2(s):
                solutions_next.add(k2)
        solutions = solutions_next
        if nk==nk2:
            break
    return min(solutions,key=len)

# def part1(codes):
#     complexity = 0
#     for code in codes:
#         print (code)
#         key = solve_code(code, 2)
#         complexity += int(code[:-1])*len(key)
#     print (f"🎄 Part 1: {complexity}")

from collections import defaultdict

def find_shortest_paths(G, Gmove):
    paths = defaultdict(list)
    for start in G.nodes():
        for end in G.nodes():
            if start != end:
                for p in list(nx.all_shortest_paths(G, start, end)):
                    m = "".join([Gmove[(p[i], p[i+1])] for i in range(len(p)-1)])
                    paths[start+end].append(m)
    return paths

@cache
def minimum_sequence(level, code, nrobots):
    pK1 = find_shortest_paths(K1,K1move)
    pK2 = find_shortest_paths(K2,K2move)

    # end of keypad sequence reached, return lenght of current sequence 
    if level == nrobots + 1:
        return len(code)

    # select dictionary of shortest paths according to level and corresponding keypad
    if level==0:
        pK = pK1
    else:
        pK = pK2

    # recursively cumulate sequence lenght, only considering shortest one
    total = 0
    for start, end in zip('A'+code, code):
        # adding "A" command at end of current step to press the button!
        min_seq = [ minimum_sequence(level+1, p+"A", nrobots) for p in pK[ start+end ] ]
        if min_seq:
            total += min(min_seq)
        else:
            # When the same button is pressed twice in a row account for 1 step in sequence,
            # since  min_seq would be empty (no entry in the shortest path dictionaries), but
            # operation is happening anyway
            total += 1 

    return total

def part1(codes, nrobots=2):
    complexity = 0
    for code in codes:
        complexity += int(code[:-1]) * minimum_sequence(0, code, nrobots)
    print (f"🎄 Part 1: {complexity}")

def part2(codes, nrobots=25):
    complexity = 0
    for code in codes:
        complexity += int(code[:-1]) * minimum_sequence(0, code, nrobots)
    print (f"🎄🎅 Part 2: {complexity}")

# # def solve_BFS_with_path(grid, start, target):
# #     q = [[start]]
# #     visited = set([start])
# #     while len(q) > 0:
# #         path = q.pop()
# #         c = path[-1]
# #         if c == target:
# #             break
# #         for dc in DIRECTIONS:
# #             nc = c + dc
# #             if grid.get(nc, None) is not None and nc not in visited:
# #                 visited.add(nc)
# #                 new_path = list([*path, nc])
# #                 q.append(new_path)
# #     return len(path)

# def find_all_shortest_paths_in_grid(grid, start, target):
#     queue = deque([(start, [])])
#     visited = {start}
#     shortest_paths = []
#     shortest_distance = float('inf')

#     while queue:
#         (current, path) = queue.popleft()
#         #print (grid[current], path)
#         if len(path) > shortest_distance:
#             continue
#         if current == target:
#             #print (len(path), shortest_distance)
#             if len(path) < shortest_distance:
#                 shortest_paths = [path]
#                 shortest_distance = len(path)
#             elif len(path) == shortest_distance:
#                 shortest_paths.append(path)
#             continue

#         for dc in DIRECTIONS:
#             nc = current + dc
#             if grid.get(nc, None) is not None:# and nc not in visited:
#                 new_path = list(path)
#                 new_path.append(DIRECTIONS[dc])
#                 #visited.add(nc)
#                 queue.append((nc, new_path))
#     return shortest_paths

# def dfs_shortest_paths(graph, start, end, path=None, shortest_paths=None, shortest_length=float('inf')):
#     if path is None:
#         path = [start]
    
#     if shortest_paths is None:
#         shortest_paths = []

#     if start == end:
#         if len(path) < shortest_length:
#             shortest_paths = [path]  # New shortest path found
#             shortest_length = len(path)
#         elif len(path) == shortest_length:
#             shortest_paths.append(path)  # Another path of the same shortest length
#         return (shortest_paths, shortest_length)

#     for dc in DIRECTIONS:
#         neighbor = start + dc
#         if neighbor in graph and neighbor not in path:
#             new_path = list(path)
#             new_path.append(neighbor)
#             shortest_paths, shortest_length = dfs_shortest_paths(graph, neighbor, end, new_path, shortest_paths, shortest_length)            
#     return (shortest_paths, shortest_length)

# from itertools import pairwise

# @cache
# def get_all_paths(a, b, nrobots):
#     if nrobots == 2:
#         keypad = {0   :"7", 1   :"8", 2   :"9",
#                   0+1j:"4", 1+1j:"5", 2+1j:"6",
#                   0+2j:"1", 1+2j:"2", 2+2j:"3",
#                             1+3j:"0", 2+3j:"A"}
#     else:
#         keypad = {          1:"^", 2:"A",
#                   0+1j:"<", 1+1j:"v", 2+1j:">"}
#     find_key = lambda c: {value: key for key, value in keypad.items()}.get(c) 
#     start = find_key(a)
#     target = find_key(b)
#     paths, length = dfs_shortest_paths(list(keypad.keys()), start, target)
#     new_paths = []
#     for path in paths:
#         new_paths.append("".join([DIRECTIONS[path[i]-path[i-1]] for i in range(1, len(path))]))
#     return new_paths

# @cache
# def find_sequence(code, nrobots=2):
#     ret = 0
#     code = "A" + code
#     paths = []
#     for a, b in pairwise(code):
#         ps = get_all_paths(a, b, nrobots)
#         if len(paths) == 0:
#             for p in ps:
#                 paths.append(p + "A")
#         else:
#             for p in ps:
#                 for i in range(len(paths)):
#                     paths[i] += p + "A"

#         print (paths)
#         # if nrobots == 0:
#         #     ret += min(len(p) for p in ps)
#         # else:
#         #     #ret += min(find_sequence(p, nrobots-1) for p in ps)
#         #     ret += [find_sequence(p, nrobots-1) for p in ps]
#     return ret
# # <A^A>^^AvvvA, <A^A^>^AvvvA, and <A^A^^>AvvvA
#     find_key = lambda c: {value: key for key, value in keypad.items()}.get(c) 
#     kd_paths = {}
#     for code in codes:
#         kd_paths[code] = [""]
#         start = find_key("A")
#         for c in code:
#             target = find_key(c)
#             if save_path:   
#                 #paths = find_all_shortest_paths_in_grid(keypad, start, target) 
#                 paths, _ = dfs_shortest_paths(frozenset(keypad.keys()), start, target)
#                 temp = []
#                 for path in paths:
#                     p = [keypad[p] for p in path]
#                     p = "".join(p) + "A"
#                     for k in kd_paths[code]:
#                         temp.append(k + p)
#                 kd_paths[code] = temp
#             start = target
#     return kd_paths

# # def new_codes(d):
# #     codes = []
# #     for v in d.values():
# #         codes.extend(v)
# #     return codes


# def part1(codes):
#     complexity = 0
#     for code in codes:
#         print (code)
#         find_sequence(code, 2)
#         # shortest_sequence_length = min([len(v) for v in robot_codes])
#         # complexity += int(code[:-1])*shortest_sequence_length
        
#         # print (robot1)
#         # robot_codes = new_codes(robot1)
#         # for i in range(2):
#         #     robot = find_sequence(robot_codes, keydir, True)
#         #     robot_codes = new_codes(robot)
#         # shortest_sequence_length = min([len(v) for v in robot_codes])
#         # complexity += int(code[:-1])*shortest_sequence_length
#     print (f"🎄 Part 1: {complexity}")
    
# def part2(codes, keypad, keydir):
#     complexity = 0
#     for code in codes:
#         print (code)
#         robot1 = find_sequence([code], keypad, True)
#         robot_codes = new_codes(robot1)
#         for i in range(25):
#             robot = find_sequence(robot_codes, keydir, True)
#             robot_codes = new_codes(robot)
#         shortest_sequence_length = min([len(v) for v in robot_codes])
#         complexity += int(code[:-1])*shortest_sequence_length
#     print (f"🎄🎅 Part 2: {0}")

if __name__ == '__main__':
    title = "Day 21: Keypad Conundrum"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print (f"{t2*1000:.3f} ms")
