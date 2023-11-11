from utils import readInput
import json

class SNumber:
    def __init__(self, obj, level=1):
        self.level = level
        self.obj = []
        for o in obj:
            if type(o) == list:
                #print (self.level + 1)
                self.obj.append(SNumber(o, self.level+1))
            else:
                self.obj.append(o)

    def walk(self, l, found=None):
        for o in self.obj:
            if type(o) == SNumber:
                if o.level == l:
                    return o
                else:
                    found = o.walk(l, found)
            if found:
                return found
        else:
            return None    
                
    def explode(self):
        l3 = self.walk(3)
        if l3 is not None:
            for i in range(len(l3)):
                if type(l3[i]) == SNumber:
                    l3[i] = 0
                    break
                
    def split(self):
        pass
    
    def __str__(self):
        s = "["
        s += ",".join(map(str, self.obj))
        s += "]"
        return s

    def __iter__(self):
        for each in self.obj:
            yield each

    def __len__(self):
        return len(self.obj)

    def __getitem__(self, item):
         return self.obj[item]

    def __setitem__(self, item, val):
         self.obj[item] = val

     
    
lines = readInput("test.txt")
obj = json.loads(lines[6])

n = SNumber(obj)
n.explode()
print (n)
