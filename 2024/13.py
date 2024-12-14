import timeit, numpy as np

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

def loadInput():
    #lines = readInput("input_13_prova.txt")
    lines = readInput("input_13.txt")
    machines = []
    for l in lines:
        if l == "":
            continue
        if l.startswith("Button A"):
            machine = Machine()
            #machine.buttonA = [int(item.split("+")[1]) for item in l.split(",")]
            machine.button[0] = np.array([int(item.split("+")[1]) for item in l.split(",")])
        elif l.startswith("Button B"):
            #machine.buttonB = [int(item.split("+")[1]) for item in l.split(",")]
            machine.button[1] = np.array([int(item.split("+")[1]) for item in l.split(",")])
        elif l.startswith("Prize"):
            machine.prize = [int(item.split("=")[1]) for item in l.split(",")]
            machines.append(machine)
    return machines

def part1(machines):
    cost = 0
    for m in machines:
        cost += m.cost()
    print (f"🎄 Part 1: {cost}")
    
def part2(machines):
    const = 10000000000000
    cost = 0
    for m in machines:
        m.prize = [const+p for p in m.prize]
        cost += m.cost()
    print (f"🎄🎅 Part 2: {cost}")

if __name__ == '__main__':
    title = "Day 13: Claw Contraption"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print(f"Timing: {t1*1000:.3f} ms")

    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print(f"Timing: {t2*1000:.3f} ms")
