from utils import readInput
import statistics

class Compiler:
    def __init__(self, filename):
        self.lines = readInput(filename)
        self.wrong = ["(]", "(}", "(>", "[)", "[}", "[>",
                      "{)", "{]", "{>", "<)", "<]", "<}"]
        self.good = ["()", "[]", "{}", "<>"]
        self.counter = [0, 0, 0, 0]
        self.scores = []
    
    def check(self, l):
        found = -1
        while found != 0:
            found = 0
            for g in self.good:
                idx = l.find(g)
                if idx != -1:
                    l = l.replace(g, "", 1)
                    found += 1
                #print (found, l)

            for iw, w in enumerate(self.wrong):
                idx = l.find(w)
                if idx != -1:
                    if w[1] == ")":
                        self.counter[0] += 1
                    elif w[1] == "]":
                        self.counter[1] += 1
                    elif w[1] == "}":
                        self.counter[2] += 1
                    elif w[1] == ">":
                        self.counter[3] += 1
                    #print (w)
                    #print ("--------------")
                    return False
        return True

    def complete(self, l):
        found = -1
        while found != 0:
            found = 0
            for g in self.good:
                idx = l.find(g)
                if idx != -1:
                    l = l.replace(g, "", 1)
                    found += 1
                #print (found, l)
        score = 0
        for c in reversed(l):
            score *= 5
            if c == "(":
                score += 1
            elif c == "[":
                score += 2
            if c == "{":
                score += 3
            if c == "<":
                score += 4
        #print (score)
        self.scores.append(score)
        
    def scoringCorrupted(self):
        score = 0
        score += self.counter[0]*3
        score += self.counter[1]*57
        score += self.counter[2]*1197
        score += self.counter[3]*25137
        return score

c = Compiler("input_10.txt")
for l in c.lines:
    c.check(l)

print ("🎄 Part 1: {}".format(c.scoringCorrupted()))

for l in c.lines:
    if c.check(l):
        c.complete(l)
        
score = statistics.median(c.scores)
print ("🎄🎅 Part 2: {}".format(score))
