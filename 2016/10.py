from utils import readInput
            
class Bot:
    def __init__(self, number, chip):
        self.number = number
        self.high = chip
        self.low = None

    def get(self, number):
        if number < self.high:
            self.low = number
        else:
            self.low, self.high = self.high, number

    def give(self):
        self.high = None
        self.low = None

    def check(self, high, low):
        if self.high == high and self.low == low:
            print ("🎄Part 1: {}".format(self.number))

    def __str__(self):
        return "BOT{}: H{} L{}".format(self.number, self.high, self.low)

class Output:
    def __init__(self, number, chip):
        self.number = number
        self.bin = [chip]

lines = readInput("input_10.txt")

bots = {}
outputs = {}
new_lines = []

for l in lines:
    if l.startswith("value"):
        parts = l.split()
        number = int(parts[-1])
        if number not in bots:
            b = Bot(number, int(parts[1]))
            bots[number] = b
        else:
            bots[number].get(int(parts[1]))
    else:
        new_lines.append(l)

lines = new_lines
new_lines = []
#for b in bots.values():
#    print (b)

i = 0
while True:
    parts = lines[i].split()
    ibot = int(parts[1])
    ilow = int(parts[6])
    ltobin = parts[5] == 'output'
    ihigh = int(parts[-1])
    htobin = parts[-2] == 'output'
        
    if ibot in bots and bots[ibot].high and bots[ibot].low:
        
        if ltobin:
            if ilow not in outputs:
                outputs[ilow] = Output(ilow, bots[ibot].low)
            else:
                outputs[ilow].bin.append(bots[ibot].low)
        else:
            if ilow not in bots:
                bots[ilow] = Bot(ilow, bots[ibot].low)
            else:
                bots[ilow].get(bots[ibot].low)
            bots[ilow].check(61, 17)
                    

        if htobin:
            if ihigh not in outputs:
                outputs[ihigh] = Output(ihigh, bots[ibot].high)
            else:
                outputs[ihigh].bin.append(bots[ibot].high)
        else:
            if ihigh not in bots:
                bots[ihigh] = Bot(ihigh, bots[ibot].high)
            else:
                bots[ihigh].get(bots[ibot].high)
            bots[ihigh].check(61, 17)                
        bots[ibot].give()

    else:
        new_lines.append(lines[i])
        
    i += 1

    if i == len(lines):
        lines = new_lines
        new_lines = []
        if len(lines) == 0:
            res = outputs[0].bin[0]*outputs[2].bin[0]*outputs[1].bin[0]
            print("🎁🎄Part 2: {}".format(res))
            import sys
            sys.exit()
        i = 0
