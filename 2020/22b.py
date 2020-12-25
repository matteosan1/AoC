import time, copy
start_time = time.time()

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
        #print ("deck", self.deck)

    def checkEnd(self):
        #print ("checking", self.deck)
        if self.deck in self.previous_rounds:
            #print ("Ended by recursion")
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
        #print ("prev", self.previous_rounds)
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

            #print ("run", self.previous_rounds)
            #print ("round", self.rounds)
        return self.winner

    def points(self):
        #print ([(len(self.deck[self.winner])-i)*self.deck[self.winner][i] for i, v in enumerate(self.deck[self.winner])])
        return sum([(len(self.deck[self.winner])-i)*self.deck[self.winner][i] for i, v in enumerate(self.deck[self.winner])])

g = Game()
g.readDeck("input_22a.txt")
print (g.run())

print('🎄 Part 2: {} 🎄'.format(g.points()))
print("\n--- %.7s secs ---" % (time.time() - start_time))