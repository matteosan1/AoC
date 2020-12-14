import re
import time
start_time = time.time()

class Docking():
    def __init__(self, filename):
        self.memory = {}
        self.r_instruction = re.compile("mem\[(\d+)\]\s=\s(\d+)")
        with open(filename) as f:
            for i, l in enumerate(f):
                l = l.split("\n")[0]
                if "mask" in l:
                    self.mask = self.prepareMask(l)
                else:
                    self.apply(l)

    def prepareMask(self, l):
        l = l.split(" ")[-1]
        bits = {}
        for it, i in enumerate(list(l)):
            if i == 'X':
                continue
            else:
                bits[it] = i
        return bits

    def apply(self, l):
        res = self.r_instruction.match(l)
        if res is not None:
            addr = res[1]
            value = list("{0:b}".format(int(res[2])).zfill(36))
            for k, v in self.mask.items():
                value[k] = v
            value = int("".join(value), 2)
            self.memory[addr] = value

d = Docking("input_14a.txt")
print('🎄 Part 1: {} 🎄'.format(sum(d.memory.values())))

print("\n--- %.7s secs ---" % (time.time() - start_time))