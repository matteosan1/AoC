import math

class Directions():
    def __init__(self):
        self.directions = ["N", "E", "S", "W"]
        self.pos = [0,0] # N, E
        self.face = "E"

    def readInstructions(self, filename):
        self.instructions = []
        with open(filename) as f:
            for l in f:
                self.instructions.append(l.split("\n")[0])

    def apply(self, instruction):
        direction = instruction[0]
        #print (direction)
        param = int(instruction[1:])
        #print (param)

        if direction == "F":
            direction = self.face

        if direction == "N":
            self.pos[0] += param
        elif direction == "S":
            self.pos[0] -= param
        elif direction == "E":
            self.pos[1] += param
        elif direction == "W":
            self.pos[1] -= param

        if direction == "R" or direction == "L":
            param //= 90
            idx = self.directions.index(self.face)
            if direction == "R":
                new_dir = (idx + param) % len(self.directions)
            else:
                new_dir = (idx - param) % len(self.directions)
            self.face = self.directions[new_dir]

    def run(self):
        for i in self.instructions:
            self.apply(i)
            #print (self.pos, self.face)

    def manahattan(self):
        return sum(map(abs, self.pos))

d = Directions()
d.readInstructions("input_12a.txt")
d.run()
print (d.manahattan())