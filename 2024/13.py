import time, numpy as np

from utils import readInput

class Machine:
    def __init__(self):
        self.buttonA = None
        self.buttonB = None
        self.button = np.zeros(shape=(2, 2))
        self.prize = None

    def solve(self, use_numpy=False):
        if use_numpy:
            sol = np.linalg.solve(self.button.T, self.prize)
            if all(np.abs(np.round(sol) - sol) < 1e-3):
                return sol
            else:
                return None
        else:
            a = round((self.prize[1]-((self.button[1,1]*self.prize[0])/self.button[1,0]))/(self.button[0,1]-((self.button[1,1]*self.button[0,0])/self.button[1,0])))
            b = round((self.prize[0]-self.button[0,0]*a)/self.button[1,0])
            if self.button[0,0]*a+self.button[1,0]*b==self.prize[0] and self.button[0,1]*a+self.button[1,1]*b==self.prize[1]:
                return (a, b)
            else:
                return None

    def cost(self):
        pushes = self.solve()
        if pushes is None:
            return 0
        else:
            return pushes[0]*3 + pushes[1]*1
    
    def __repr__(self):
        return (f"A: {self.buttonA}, B: {self.buttonB}, prize: {self.prize}")

def loadInput(filename: str) -> list[Machine]:
    lines = readInput(filename)
    machines: list[Machine] = []
    for l in lines:
        if l == "":
            continue
        if l.startswith("Button A"):
            machine: Machine = Machine()
            #machine.buttonA = [int(item.split("+")[1]) for item in l.split(",")]
            machine.button[0] = np.array([int(item.split("+")[1]) for item in l.split(",")])
        elif l.startswith("Button B"):
            #machine.buttonB = [int(item.split("+")[1]) for item in l.split(",")]
            machine.button[1] = np.array([int(item.split("+")[1]) for item in l.split(",")])
        elif l.startswith("Prize"):
            machine.prize = [int(item.split("=")[1]) for item in l.split(",")]
            machines.append(machine)
    return machines

def part1(machines: list[Machine]):
    cost = sum([m.cost() for m in machines])
    print (f"🎄 Part 1: {cost}", end='')
    
def part2(machines: list[Machine]):
    const = 10000000000000
    cost = 0
    for m in machines:
        m.prize = [const+p for p in m.prize]
        cost += m.cost()
    print (f"🎄🎅 Part 2: {cost}", end='')

if __name__ == '__main__':
    title = "Day 13: Claw Contraption"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_13.txt")
    
    t0 = time.time()
    part1(inputs)
    print (" - {:.6f} s".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print (" - {:.6f} s".format(time.time()-t0))
