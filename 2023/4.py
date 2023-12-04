import time
from utils import readInput

def loadInput():
    #lines = readInput("prova.txt")
    lines = readInput("input_4.txt")
    scratchcards = {}
    for l in lines:
        game, cards = l.split(":")
        id = int(game[5:])
        winning, mine = cards.split("|")
        winning = list(map(int, winning.split()))
        mine = list(map(int, mine.split()))
        scratchcards[id] = (winning, mine)
    return scratchcards

def winning(wins, cards):
    points = 0
    for c in wins:
        if c in cards:
            points += 1
    return points
    
def printCards(cards):
    for v in cards.values():
        print (v[2])    

def part1(inputs):
    tot = 0
    for id, cards in inputs.items():
        points = winning(cards[0], cards[1])
        if points > 0:
            tot += 2**(points-1)
    print (f"🎄 Part 1: {tot}")

def part2(inputs):
    cards = {}
    for k, v in inputs.items():
        cards[k] = [*v, 1]
    
    for k, v in cards.items():
        points = winning(v[0], v[1])
        if points > 0:
            for i in range(points):
                cards[k+i+1][2] += 1*v[2]
    tot = 0
    for v in cards.values():
        tot += v[2]
    print (f"🎄🎅 Part 2: {tot}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 4         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(inputs)
print (f"Time: {time.time()-t0:.5f}")
