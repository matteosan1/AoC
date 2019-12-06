from treelib import Node, Tree

def findParent(node):
    global n_ind_orbits, tree

    #parent = tree.get_node(node).bpointer
    if node == "com":
        return
    else:
        findParent(tree.get_node(node).bpointer)
    n_ind_orbits[node] = tree.depth(tree.get_node(node))

inputs = []
with open("input6a.txt") as f:
    for i, l in enumerate(f):
        inputs.append(l.split("\n")[0])
#inputs = [
#    "COM)B",
#"B)C",
#"C)D",
#"D)E",
#"E)F",
#"B)G",
#"G)H",
#"D)I",
#"E)J",
#"J)K",
#"K)L",]

n_ind_orbits = {}
tree = Tree()
tree.create_node("COM", "com")
i = 0
to_recover = []
while len(inputs) != 0:
    
    try:
        items = inputs[i].split(")")
        tree.create_node(items[1], items[1].lower(), parent=items[0].lower())
    except:
        to_recover.append(inputs[i])
    finally:
        i += 1
        if i == len(inputs):
            i = 0
            inputs = list(to_recover)
            to_recover = []
#tree.show()

for l in tree.leaves():
    findParent(l.identifier)

orbits = 0
for o in n_ind_orbits.values():
    orbits += o
print (orbits)
