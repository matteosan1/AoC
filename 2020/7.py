import time
from utils import readInput

def loadInput():
    lines = readInput("input_7.txt")

    return lines

class MyTree:
    def __init__(self):
        self.tree = {}

    def addNode(self, node):
        self.tree[node.name] = node

    def traverse(self, start, to, ok=0):
        for c in self.tree[start].children.keys():
            if c == to:
                return True
            else:
                ok += 1
                x = self.traverse(c, to, ok)
                if x:
                    return True

        return False

    def traverse2(self, start, tot = 0):
        for k, v in self.tree[start].children.items():
            res = self.traverse2(k, 1)
            tot += v * res

        return tot


class MyNode:
    def __init__(self, name, children=None):
        self.name = name.replace("bags", "bag")
        self.children = {}
        for c in children:
            if c[:2] == 'no':
                continue
            self.children[c[2:].replace("bags", "bag")] = int(c[:2])
            
def part1(lines):
    tree = MyTree()

    for l in lines:
        items = l.split(" contain ")
        tree.addNode(MyNode(items[0],
                            items[1][:-1].split(", ")))

    ok = 0
    for t in tree.tree.keys():
        if tree.traverse(t, "shiny gold bag"):
            ok += 1
    print ("🎄 Part 1: {}".format(ok))

def part2(lines):
    tree = MyTree()

    for l in lines:
        items = l.split(" contain ")
        tree.addNode(MyNode(items[0],
                            items[1][:-1].split(", ")))

    t = "shiny gold bag"
    print ("🎄🎅 Part 2: {}".format(tree.traverse2(t)))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 7         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))
