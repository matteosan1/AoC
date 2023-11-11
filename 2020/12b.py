import math

class Directions():
    def __init__(self):
        self.waypoint = [1, 10]
        self.pos = [0,0] # N, E

    def readInstructions(self, filename):
        self.instructions = []
        with open(filename) as f:
            for l in f:
                self.instructions.append(l.split("\n")[0])

    def apply(self, instruction):
        direction = instruction[0]
        param = int(instruction[1:])

        if direction == "F":
            self.pos = [self.pos[0] + param*self.waypoint[0],
                        self.pos[1] + param*self.waypoint[1]]

        if direction == "N":
            self.waypoint[0] += param
        elif direction == "S":
            self.waypoint[0] -= param
        elif direction == "E":
            self.waypoint[1] += param
        elif direction == "W":
            self.waypoint[1] -= param

        if direction == "R" or direction == "L":
            param = math.radians(param)
            if direction == "R":
                self.waypoint = [self.waypoint[0] * math.cos(param) - self.waypoint[1] * math.sin(param),
                                 self.waypoint[0] * math.sin(param) + self.waypoint[1] * math.cos(param)]
            else:
                self.waypoint = [self.waypoint[0] * math.cos(param) + self.waypoint[1] * math.sin(param),
                                 -self.waypoint[0] * math.sin(param) + self.waypoint[1] * math.cos(param)]

    def run(self):
        for i in self.instructions:
            self.apply(i)
            #print (self.pos, self.waypoint)

    def manahattan(self):
        return sum(map(abs, self.pos))

d = Directions()
d.readInstructions("input_12a.txt")
d.run()
print (d.manahattan())