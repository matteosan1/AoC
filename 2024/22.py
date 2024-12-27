import time

from math import floor

from utils import readInput

def loadInput(filename):
    lines = readInput(filename)
    return list(map(int, lines))

def nth_secret(secret_number, n=2000):
    for i in range(n):
        secret_number ^= (secret_number << 6) & 0xFFFFFF
        secret_number ^= (secret_number >> 5) & 0xFFFFFF
        secret_number ^= (secret_number << 11) & 0xFFFFFF
    return secret_number

def part1(secret_numbers):
    secret_sum = 0
    for secret_number in secret_numbers:
        secret_sum += nth_secret(secret_number)
    print (f"🎄 Part 1: {secret_sum}", end='')
    
from collections import defaultdict
from queue import deque

def total_bananas(secrets, n=2000):
    bananas = defaultdict(int)
    for secret in secrets:
        for deltas, price in price_timeline(secret, n).items():
            bananas[deltas] += price
    return bananas
    
def price_timeline(secret, n=2000):
    timeline = {}             # {delta-4-tuple: price} pairs
    deltas = deque(maxlen=4)  # The 4 most recent price deltas  
    price = secret % 10       # Initial price
    for _ in range(n):
        secret = nth_secret(secret, 1)
        price, previous_price = secret % 10, price
        deltas.append(price - previous_price)
        D = tuple(deltas)
        if len(D) == 4 and D not in timeline:
            timeline[D] = price
    return timeline

def part2(secret_numbers):
    print (f"🎄🎅 Part 2: {max(total_bananas(secret_numbers).values())}", end='')

if __name__ == '__main__':
    title = "Day 22: Monkey Market"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_22.txt")
    
    t0 = time.time()
    part1(inputs)
    print (" - {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print (" - {:.5f}".format(time.time()-t0))
