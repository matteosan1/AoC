import time, copy
from utils import readInput

def loadInput():
    lines = readInput("input_22.txt")
    deck = [[], []]
    id = -1
    for l in lines:
        if l == "":
            continue
        if "Player" in l:
            id += 1
        else:
            deck[id].append(int(l))

    return deck

def part1(deck):
    rounds = 1
    while len(deck[0]) > 0 and len(deck[1]) > 0:
        if deck[0][0] > deck[1][0]:
            deck[0].append(deck[0][0])
            deck[0].append(deck[1][0])
        elif deck[0][0] < deck[1][0]:
            deck[1].append(deck[1][0])
            deck[1].append(deck[0][0])
        else:
            deck[0].append(deck[0][0])
            deck[1].append(deck[1][0])
        deck[0].pop(0)
        deck[1].pop(0)
        rounds += 1

    if len(deck[1]) > 0:
        points = sum([(len(deck[1])-i)*deck[1][i] for i, v in enumerate(deck[1])])
    elif len(deck[0]) > 0:
        points = sum([(len(deck[0])-i)*deck[0][i] for i, v in enumerate(deck[0])])
    
    print ("🎄 Part 1: {}".format(points))

class Game:
    def __init__(self, deck=[[], []]):
        self.deck = deck
        self.previous_rounds = []
        self.rounds = 0
        self.winner = -1

    def readDeck(self, filename):
        id = -1
        with open(filename) as f:
            for l in f:
                l = l.split("\n")[0]
                if l == "":
                    continue
                if "Player" in l:
                    id += 1
                else:
                    self.deck[id].append(int(l))

    def checkRecursive(self):
        if self.deck[0][0] <= len(self.deck[0])-1:
            if self.deck[1][0] <= len(self.deck[1]) - 1:
                return True
        return False

    def moveCards(self, winner):
        if winner < 0:
            self.deck[0].append(self.deck[0][0])
            self.deck[1].append(self.deck[1][0])
        else:
            self.deck[winner].append(self.deck[winner][0])
            self.deck[winner].append(self.deck[int(not winner)][0])
        self.deck[0].pop(0)
        self.deck[1].pop(0)

    def checkEnd(self):
        if self.deck in self.previous_rounds:
            self.winner = 0
            return True
        elif len(self.deck[0]) == 0:
            self.winner = 1
            return True
        elif len(self.deck[1]) == 0:
            self.winner = 0
            return True
        else:
            return False

    def run(self):
        while not self.checkEnd():
            self.previous_rounds.append(copy.deepcopy(self.deck))
            if self.checkRecursive():
                new_deck = [self.deck[0][1:self.deck[0][0]+1], self.deck[1][1:self.deck[1][0]+1]]
                rec_game = Game(new_deck)
                winner = rec_game.run()
                self.moveCards(winner)
            else:
                if self.deck[0][0] > self.deck[1][0]:
                    self.moveCards(0)
                elif self.deck[0][0] < self.deck[1][0]:
                    self.moveCards(1)
                else:
                    self.moveCards(-1)
            self.rounds += 1
        return self.winner

    def points(self):
        return sum([(len(self.deck[self.winner])-i)*self.deck[self.winner][i] for i, v in enumerate(self.deck[self.winner])])

def part2():
    g = Game()
    g.readDeck("input_22.txt")

    print ("🎄🎅 Part 2: {}".format(g.points()))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 22        ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2()
print ("Time: {:.5f}".format(time.time()-t0))
