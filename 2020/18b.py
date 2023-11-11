import time
start_time = time.time()

class Parser:
    def __init__(self):
        self.op = []
        with open("input_18a.txt") as f:
            for l in f:
                l = l.split("\n")[0]
                self.op.append(l)

    def blocks(self, l):
        while l.rfind("(") != -1:
            popen = l.rfind("(")
            pclose = l[popen:].find(")") + popen
            res = self.evaluate2(l[popen+1:pclose])
            l = l.replace(l[popen:pclose+1], str(res))
            #print (l)
        res = self.evaluate2(l)
        return res

    def evaluate2(self, l):
        l = l.split(" ")
        for i in range(1, len(l)):
            if l[i] == "+":
                l[i-1] = "("+l[i-1]
                l[i+1] = l[i+1]+")"
        return str(eval("".join(l)))

    def evaluate(self, l):
        l = l.split(" ")
        while True:
            if len(l) == 3:
                return str(eval("".join(l[:3])))
            else:
                l = [str(eval("".join(l[:3])))] + l[3:]
            #print (l)

    def run(self):
        res = []
        for l in self.op:
            #print (self.blocks(l))
            res.append(int(self.blocks(l)))
        return res

p = Parser()
res = p.run()
print (res)
print('🎄 Part 2: {} 🎄'.format(sum(res)))
print("\n--- %.7s secs ---" % (time.time() - start_time))
