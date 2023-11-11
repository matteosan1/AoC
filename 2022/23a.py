import time, numpy as np
start_time = time.time()

class CircularList:
    def __init__(self, cups):
        self.cups = self.cupsInt(cups)
        self.current = 0
        self.rounds = 0

    def cupsInt(self, cups):
        return list(map(int, list(cups)))

    def cut(self):
        self.rounds += 1
        #print ("----- move {} -----".format(self.rounds))
        #print ("cups:", self.cups)
        current_value = self.cups[self.current]
        #print ("current ", current_value)
        min = (self.current + 1) % len(self.cups)
        max = (self.current + 4) % len(self.cups)
        if min < max:
            new_cups = self.cups[:min] + self.cups[max:]
            removed = self.cups[min:max]
        else:
            new_cups =  self.cups[max:min]
            removed = self.cups[min:] + self.cups[0:max]
        #print ("pick up ", removed)
        destination = (current_value - 1) % len(self.cups)
        if destination == 0:
            destination = len(self.cups)
        destination_index = -1
        while destination_index == -1:
            try:
                destination_index = new_cups.index(destination) + 1
            except:
                destination -= 1
                destination = destination % len(self.cups)
                if destination == 0:
                    destination = len(self.cups)
        #print ("dest ", destination)
        self.cups = new_cups[:destination_index] + removed + new_cups[destination_index:]
        #print (self.current, self.cups.index(current_value))
        self.rotate(self.current - self.cups.index(current_value))
        self.current += 1
        self.current = self.current % len(self.cups)
        #print ()

    def rotate(self, r):
        self.cups = list(np.roll(self.cups, r))

    def run(self, moves):
        for _ in range(moves):
            self.cut()

    def finalize(self):
        index = self.cups.index(1)
        self.rotate(-index)
        cups = list(map(str, self.cups))
        return "".join(cups[1:])

cups = "872495136"
#cups = "389125467"

c = CircularList(cups)
c.run(100)

print('🎄 Part 1: {} 🎄'.format(c.finalize()))
print("\n--- %.7s secs ---" % (time.time() - start_time))