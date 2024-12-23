import timeit

from math import floor

from utils import readInput

def loadInput():
    #lines = readInput("input_22_prova.txt")
    lines = readInput("input_22.txt")
    return list(map(int, lines))

# mix = lambda val, n: val ^ n
# prune = lambda n: n % 16777216

# def generate(n):
#     n = (n << 6 ^ n) & 0xFFFFFF
#     n = (n >> 5 ^ n) & 0xFFFFFF
#     return (n << 11 ^ n) & 0xFFFFFF

def part1(secret_numbers):
    secret_sum = 0
    for n in secret_numbers:
        #print (f"{n}: ", end='')
        for i in range(2000):
            n = (n << 6 ^ n) & 0xFFFFFF
            n = (n >> 5 ^ n) & 0xFFFFFF
            n = (n << 11 ^ n) & 0xFFFFFF
            #n = generate(n)
        #print (n)
        secret_sum += n
    print (f"🎄 Part 1: {secret_sum}")
    
def part2(secret_numbers):
    totals = {}
    for n in secret_numbers:
        seqs = {}
        seq = (0,0,0,0)
        for i in range(2000):
            prev = n%10
            n = (n << 6 ^ n) & 0xFFFFFF
            n = (n >> 5 ^ n) & 0xFFFFFF
            n = (n << 11 ^ n) & 0xFFFFFF
            #n = generate(n)
            seq = (*seq[1:], n%10-prev)
            if i >= 3 and seq not in seqs:
                seqs[seq] = n%10
        for s in seqs:
            totals[s] = totals.get(s, 0) + seqs[s]
    x = max(totals.values())
    print (f"🎄🎅 Part 2: {x}")

if __name__ == '__main__':
    title = "Day 22: Monkey Market"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print (f"{t2*1000:.3f} ms")
