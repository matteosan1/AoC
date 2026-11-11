import re
import time
start_time = time.time()

class Docking():
    def __init__(self, filename):
        self.memory = {}
        self.r_instruction = re.compile("mem\[(\d+)\]\s=\s(\d+)")
        with open(filename) as f:
            lines = [l.split("\n")[0] for l in f.readlines()]
        for i, l in enumerate(lines):
            l = l.split("\n")[0]
            if "mask" in l:
                self.mask = self.prepareMask(l)
            else:
                self.apply(l)

    def prepareMask(self, l):
        l = l.split(" ")[-1]
        bits = list(l)
        #print (bits)
        return bits

    def apply(self, l):
        #print (l)
        res = self.r_instruction.match(l)
        if res is not None:
            addrs = [list("{0:b}".format(int(res[1])).zfill(36))]
            value = int(res[2])
            #print (addrs, value)
            for i in range(36):
                new_addr = []
                for addr in addrs:
                    if self.mask[i] == '0':
                        break
                    elif self.mask[i] == '1':
                        addr[i] = "1"
                    elif self.mask[i] == 'X':
                        addr[i] = "0"
                        new_addr.append(list(addr))
                        addr[i] = "1"

                if new_addr != []:
                    addrs += new_addr
                    #for a in addrs:
                    #    print ("new_addr ", "".join(a))
                    #print (" ----")

            for addr in addrs:
                #print ("".join(addr))
                addr = int("".join(addr), 2)
                #print (addr)
                self.memory[addr] = value

d = Docking("input_14a.txt")

print('🎄 Part 2: {} 🎄'.format(sum(d.memory.values())))

print("\n--- %.7s secs ---" % (time.time() - start_time))