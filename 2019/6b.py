from treelib import Node, Tree

def findParent(orbits, node):
    global tree

    #parent = tree.get_node(node).bpointer
    if node == "com":
        return
    else:
        findParent(orbits, tree.get_node(node).bpointer)
    orbits[node] = tree.depth(tree.get_node(node))

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
#"K)L",
#    "K)YOU",
#"I)SAN"
#]

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
tree.show()
s_orbits = {}
e_orbits = {}
start = tree.get_node("you")
end = tree.get_node("san")

findParent(s_orbits, start.identifier)
findParent(e_orbits, end.identifier)

max_key = None
max_orbit = 0
for k in s_orbits.keys():
    if k in e_orbits:
        if s_orbits[k] > max_orbit:
            max_orbit = s_orbits[k]
            max_key = k
            
distance = s_orbits["you"] - s_orbits[max_key] + e_orbits["san"] - e_orbits[max_key] - 2
print (distance, max_key)
