filename = "instructions14a.txt"
#filename = "examples14a.txt"

with open(filename, "r") as f:
    data = f.readlines()

def scoring(reindeers):
    kms = []
    for r in reindeers:
        kms.append(r.km)

    m = max(kms)
    for i, k in enumerate(kms):
        if k == m:
            reindeers[i].points += 1
    return reindeers

class Reindeer:
    def __init__(self, name, speed, energy, recover):
        self.name = name
        self.speed = speed
        self.energy = energy
        self.recover = recover
        self.km = 0
        self.state = self.energy
        self.points = 0

    def __repr__(self):
        return (self.name + " " + str(self.km) + " " + str(self.points))

    def run(self):
        if self.state < 0:
            self.state += 1
            if self.state == 0:
                self.state = self.energy
        else:
            self.state -= 1
            self.km += self.speed
            if self.state == 0:
                self.state = -self.recover


reindeers = []
distance = {}
time = 2503

for d in data:
    d = d.split("\n")[0].split(" ")
    reindeers.append(Reindeer(d[0], int(d[3]), int(d[6]), int(d[-2])))

for t in range(time):
    for r in reindeers:
        r.run()
    reindeers = scoring(reindeers)

for r in reindeers:
    print (r)
