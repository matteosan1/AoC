import time
from utils import readInput

def loadInput():
    lines = readInput("input_25.txt")
    return [int(n) for n in lines]
 
def transform(subject_number, target):
    ls = 0
    s = 1
    while True:
        s *= subject_number
        s = s%20201227
        if s == target:
            return ls+1
        ls += 1

def encr_key(loop_size, subject_number):
    s = 1
    for _ in range(loop_size):
        s *= subject_number
        s = s % 20201227
    return s

def part1(card_pub_key, door_pub_key):
    card_loop_size = transform(7, card_pub_key)
    print ("🎄 Part 1: {}".format(encr_key(card_loop_size, door_pub_key)))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 25        ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

card_pub_key, door_pub_key = loadInput()

t0 = time.time()
part1(card_pub_key, door_pub_key)
print ("Time: {:.5f}".format(time.time()-t0))

