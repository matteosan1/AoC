from utils import readLine
from anytree import AnyNode, LevelOrderGroupIter

line = readLine("license.txt")

license = list(map(int, line.split()))

def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (totals, sum(scores[k-1] for k in data[:metas] if k>0 and k<=len(scores)), data[metas:])

total, value, remaining = parse(license)

print ('part 1:', total)
print ('part 2:', value)

#nodes = []

#level = 0
#root = AnyNode(id=str(level) + "_0", nmetadata = 0, metadata = 0)
#nodes.append(root)

#n = LevelOrderGroupIter(root)
#print (n)
# j = 0
# current_node = root
# while j < len(license):
#     children = int(license[j])
#     level = level + 1
#     for i in range(children):
#         nodes.append(AnyNode(id=str(level) + "_" + str(i), nmetadata = 0, metadata = 0, parent=current_node))
#     j = j + 1
#     current_node.nmetadata = int(license[j])
#
#
#     nodes[j] = Node(license[j], license[j+1])
#     if nchildren == 0:
#         j = j + 1
#         for i in range(nmetadata):
#             metadata = metadata + license[j + 1 + i]
#         j = j + 1 + nmetadata
#     else:
#         for i in range(nchildren
