import re

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
        #print ("new mask ", self.bits)
        return bits

    def apply(self, l):
        res = self.r_instruction.match(l)
        if res is not None:
            addr = res[1]
            value = int(res[2])
            #self.memory[addr] = value
            value = list("{0:b}".format(int(res[2])).zfill(36))
            #print ("value before ", "".join(value))
            #print (int("".join(value), 2))
            #print ("mask         ", "".join(self.mask))
            for k, v in self.mask.items():
                print (k, v)
                value[k] = v
            #print("value after  ", "".join(value))
            #print(int("".join(value), 2))
            value = int("".join(value), 2)
            #if addr in self.memory.keys():
            #    print ("Changing addr ", addr)
            #else:
            #    print ("Adding new value ", addr)
            self.memory[addr] = value

d = Docking("input_14a.txt")
print (sum(d.memory.values()))
#6317049172545
#3434009980379

#value before  000000000000000010001001100001110000
#              001X11X1X010X1X1010XX10X100101011000
#value after   001000011010011100010001100011111000

#value before  000000000000000010001001100001110000
#               0b1111111010111101011101100101011000
#               0b1011010010010101000100100101011000
              #0b1011010010010101001101100101011000

#val   0101
#mask  0011
#res   0011