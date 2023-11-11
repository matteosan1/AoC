from utils import readLines
import networkx as nx

lines = readLines("instructions.txt")

# instr = []
# temp = []
# for l in lines:
#     items = l.split()
#     temp.append((items[1], items[7]))

# for i in range(3):
#     for t in temp:
#         if t[0] not in instr and t[1] not in instr:
#             instr.append(t[0])
#             instr.append(t[1])
#         elif t[0] not in instr:
#             index = instr.index(t[1])
#             i = 1
#             while ord(instr[index-i]) > ord(t[0]):
#                 i = i + 1
#             instr.insert(index-i, t[0])
#         elif t[1] not in instr:
#             index = instr.index(t[0])
#             i = 1
#             while index+i < len(instr) and ord(instr[index+i]) < ord(t[1]):
#                 i = i + 1
#             instr.insert(index+i, t[1])
#         else:
#             index0 = instr.index(t[0])
#             index1 = instr.index(t[1])
#             if index1<index0:
#                 instr.remove(t[1])
#                 instr.insert(index0+1, t[1])
#         print (instr)
#
# for t in temp:
#     index0 = instr.index(t[0])
#     index1 = instr.index(t[1])
#     if index0 > index1:
#         print ("Errore: ", t)
#
# print ("".join(instr))
def solve(lines):
    G = nx.DiGraph()
    for line in lines:
        parts = line.split(" ")
        G.add_edge(parts[1], parts[7])
    print (''.join(nx.lexicographical_topological_sort(G)))
    return G

G = solve(lines)

task_times = []
tasks = []
time = 0
while task_times or G:
    available_tasks = [t for t in G if t not in tasks and G.in_degree(t) == 0]
    if available_tasks and len(task_times) < 5:
        task = min(available_tasks)  # min gets smallest task alphabetically
        task_times.append(ord(task) - 4)
        tasks.append(task)
    else:
        min_time = min(task_times)
        completed = [tasks[i] for i, v in enumerate(task_times) if v == min_time]
        task_times = [v - min_time for v in task_times if v > min_time]
        tasks = [t for t in tasks if t not in completed]
        time += min_time
        G.remove_nodes_from(completed)

print(time)