#Player 1 starting position: 9
#Player 2 starting position: 6

class DeterministicDice:
    def __init__(self):
        self.turn = 0
        self.val = 0

    def roll(self):
        res = 0
        for _ in range(3):
            self.val += 1
            res += self.val
            self.turn += 1
            if self.val == 100:
                self.val = 0
        return res
        
class Player:
    def __init__(self, start):
        self.pos = start-1
        self.score = 0

    def move(self, roll):
        self.pos += roll
        #print (self.pos, roll)
        self.pos %= 10
        self.score += self.pos+1
        #print ("pos ", self.score, self.pos)

p1 = Player(9)
p2 = Player(6)
dice = DeterministicDice()
while True:
    p1.move(dice.roll())
    if p1.score >= 1000:
        break
    p2.move(dice.roll())
    if p2.score >= 1000:
        break

print ("🎄 Part 1: {}".format(min(p1.score, p2.score)*dice.turn))
