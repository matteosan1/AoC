
class MyTree:
    def __init__(self):
        self.tree = {}

    def addNode(self, node):
        self.tree[node.name] = node

    def traverse(self, start, to, ok=0):
        print (start, self.tree[start].children.keys())
        for c in self.tree[start].children.keys():
            print (ok, "\t", c)
            if c == to:
                return True
            else:
                ok += 1
                x = self.traverse(c, to, ok)
                if x:
                    return True

        return False

class MyNode:
    def __init__(self, name, children=None):
        self.name = name.replace("bags", "bag")
        self.children = {}
        for c in children:
            if c[:2] == 'no':
                continue
            self.children[c[2:].replace("bags", "bag")] = int(c[:2])

lines = []
with open ("input_7a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

tree = MyTree()

for l in lines:
    items = l.split(" contain ")
    tree.addNode(MyNode(items[0],
                        items[1][:-1].split(", ")))

#print (len(tree.tree))
ok = 0
for t in tree.tree.keys():
    print ("START:", t)
    if tree.traverse(t, "shiny gold bag"):
        ok += 1
        print ("YES")
    print ("-----\n")
print (ok)