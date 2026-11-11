from utils import readInput
import re

class Cuboid:
    def __init__(self, x0, x1, y0, y1, z0, z1, on='on'):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1
        self.on = on

    @classmethod
    def from_string(cls, s):
        onoff_str, coords = s.split()
        cbd = cls(*tuple(int(n) for n in re.findall(r'-?\d+', coords)))
        cbd.on = onoff_str == 'on'
        return cbd

    def size(self):
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)

    def coords(self):
        return (self.x0, self.x1, self.y0, self.y1, self.z0, self.z1)
    
    def intersect(self, other):
        x10 = max(self.x0, other.x0)
        x11 = min(self.x1, other.x1)
        y10 = max(self.y0, other.y0)
        y11 = min(self.y1, other.y1)
        z10 = max(self.z0, other.z0)
        z11 = min(self.z1, other.z1)
        if x10 <= x11 and y10 <= y11 and z10 <= z11:
            return Cuboid(x10, x11, y10, y11, z10, z11, on=self.on)
    
    def subtract(self, other):
        cbd = self.intersect(other)
        if cbd is None:
            return []
        L = []
        (x00, x01, y00, y01, z00, z01) = self.coords()
        (x10, x11, y10, y11, z10, z11) = cbd.coords()
        if x10 - x00 > 0:
            L.append(Cuboid(x00, x10-1, y00, y01, z00, z01, on=self.on))
        if x01 - x11 > 0:
            L.append(Cuboid(x11+1, x01, y00, y01, z00, z01, on=self.on))
        if y10 - y00 > 0:
            L.append(Cuboid(x10, x11, y00, y10-1, z00, z01, on=self.on))
        if y01 - y11 > 0:
            L.append(Cuboid(x10, x11, y11+1, y01, z00, z01, on=self.on))
        if z10 - z00 > 0:
            L.append(Cuboid(x10, x11, y10, y11, z00, z10-1, on=self.on))
        if z01 - z11 > 0:
            L.append(Cuboid(x10, x11, y10, y11, z11+1, z01, on=self.on))
        return L

lines = readInput("input_22.txt")
S = set()
for l in lines:
    cbd = Cuboid.from_string(l)
    for other in list(S):
        diffs = other.subtract(cbd)
        if diffs:
            S.remove(other)
            S.update(diffs)
    S.add(cbd)
print ("🎄🎅 Part 2: {}".format(sum(x.size() for x in S if x.on)))
