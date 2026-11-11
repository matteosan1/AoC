import numpy as np
from utils import readInput, printArray
    
class Cave:
    def __init__(self, filename):
        lines = readInput(filename)
        self.cm = np.zeros(shape=(len(lines[0]), len(lines)))
        for i, l in enumerate(lines):
            m = [int(c) for c in l]
            self.cm[:, i] = np.array(m)
        
    def findMinima(self):
        min_locs = []
        for y in range(self.cm.shape[1]):
            for x in range(self.cm.shape[0]):
                vals = [self.cm[a[0], a[1]] for a in self.adjacentLoc([x, y])]
                if min(vals) > self.cm[x, y]:
                    min_locs.append([x, y])
        return min_locs

    def riskFactor(self):
        mins = self.findMinima()
        risk_factors = [self.cm[m[0], m[1]]+1 for m in mins]
        return sum(risk_factors)
    
    def findBasin(self, loc):
        val = self.cm[loc[0], loc[1]]
        basins = [loc]
        adj = self.adjacentLoc(loc)
        while len(adj) > 0:
            new_adj = []
            for a in adj:
                if (self.cm[a[0], a[1]] > val) and (self.cm[a[0], a[1]] != 9):
                    if a not in basins:
                        basins.append(a)
                    if a not in new_adj:
                        new_adj.append(a)
            adj = []
            for a in new_adj:
                adj += [c for c in self.adjacentLoc(a) if (c not in adj) and (self.cm[c[0], c[1]] != 9)]
            val += 1
        return basins

    def adjacentLoc(self, loc):
        adj = []
        if loc[0]-1 >= 0:
            adj.append([loc[0]-1, loc[1]])
        if loc[1]-1 >= 0:
            adj.append([loc[0], loc[1]-1])
        if loc[0]+1 < self.cm.shape[0]:
            adj.append([loc[0]+1, loc[1]])
        if loc[1]+1 < self.cm.shape[1]:
            adj.append([loc[0], loc[1]+1])
        return adj

    def draw(self):
        from matplotlib import cm
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import pyplot as plt
        plt.rcParams['figure.figsize'] = (10, 10)
        
        plt.contour(self.cm, cmap=cm.turbo)
        plt.show()
        
        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection='3d')
        #ax.contour(X, Y, self.cm, cmap=cm.turbo)
        #ax.set_zlim(0, 20)
        ##ax.set_xlim(0.01, .1)
        #ax.set_xlabel('rate')
        #ax.set_ylabel('volatility')
        ##ax.set_ylim(0.15, .6)
        #ax.set_zlabel('price') #absolute error')
        #plt.show()

c = Cave("input_9.txt")
print ("🎄 Part 1: {}".format(c.riskFactor()))
#printArray(c.cm, c.findMinima())

basins = []
locs = c.findMinima()
for l in locs:
    basins.append(c.findBasin(l))

coords = []
for b in basins:
    for coor in b:
        coords.append(coor)
printArray(c.cm, coords)

lengths = [len(b) for b in basins]
tot = 1
for b in sorted(lengths)[-3:]:
    tot *= b

print ("🎄🎅 Part 2: {}".format(tot))

