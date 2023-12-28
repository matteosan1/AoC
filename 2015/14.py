import time

from utils import readInput

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

def loadInput():
    lines = readInput("instructions14a.txt")
    reindeers = []
    for d in lines:
        d = d.split("\n")[0].split(" ")
        reindeers.append(Reindeer(d[0], int(d[3]), int(d[6]), int(d[-2])))
    return reindeers

def scoring(reindeers):
    kms = []
    for r in reindeers:
        kms.append(r.km)

    m = max(kms)
    for i, k in enumerate(kms):
        if k == m:
            reindeers[i].points += 1
    return reindeers

def run(reindeers):
    time = 2503

    for t in range(time):
        for r in reindeers:
            r.run()
        reindeers = scoring(reindeers)

def part1(reindeers):
    run(reindeers)
    reindeers.sort(key=lambda r: r.km, reverse=True)
    print (f"🎄 Part 1: {reindeers[0]}")
    return reindeers

def part2(reindeers):
    reindeers.sort(key=lambda r: r.points, reverse=True)
    print (f"🎄🎅 Part 2: {reindeers[0]}")
    
if __name__ == "__main__":
    title = "Day 14: Reindeer Olympics"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    reindeers = part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(reindeers)
    print ("Time: {:.5f}".format(time.time()-t0))

