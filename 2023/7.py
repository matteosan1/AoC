import time
from collections import Counter

from utils import readInput

wins = {(5,):6, (1,4):5, (2,3):4, (1,1,3):3, (1,2,2):2, (1,1,1,2):1, (1,1,1,1,1):0}
cards = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
cards_with_jocker = {'A':13, 'K':12, 'Q':11, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, 'J':0}

class Hand:
    def __init__(self, h, bid, part=1):
        self.part = part
        self.h = h
        self.find_rank()
        self.bid = bid
        
    def find_rank(self):
        self.c = tuple(sorted(Counter(self.h).values()))
        self.rank = wins[self.c]
        if self.part == 2 and 'J' in self.h:
            max_rank = self.rank
            max_hand = self.h
            for c in cards:
                new_hand = self.h.replace("J", c)
                new_rank = wins[tuple(sorted(Counter(new_hand).values()))]
                if new_rank > max_rank:
                    max_hand = new_hand
                    max_rank = new_rank
            self.rank = max_rank
            self.max_h = max_hand
                    
    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        else:
            for i in range(5):
                if self.h[i] != other.h[i]:
                    if self.part == 1:
                        return cards[self.h[i]] < cards[other.h[i]]
                    else:
                        return cards_with_jocker[self.h[i]] < cards_with_jocker[other.h[i]]
    def __str__(self):
        return str(self.h)

def loadInput(part):
    lines = readInput("input_7.txt")
    hands = []
    bids = []
    for l in lines:
        hand, bid = l.split()
        hands.append(Hand(hand, int(bid), part))
        
    return sorted(hands)
    
def part1(hands):
    points  = 0
    for ih, h in enumerate(hands):
        points += (ih+1) * h.bid
    print (f"🎄 Part 1: {points}")

def part2(hands):
    points  = 0
    for ih, h in enumerate(hands):
        points += (ih+1) * h.bid
    print (f"🎄🎅 Part 2: {points}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 7         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

hands = loadInput(1)

t0 = time.time()
part1(hands)
print (f"Time: {time.time()-t0:.5f}")

hands = loadInput(2)

t0 = time.time()
part2(hands)
print (f"Time: {time.time()-t0:.5f}")
