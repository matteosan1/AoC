def generator(N, C, M=1):
    while True:
        N = N * C % 2147483647
        if N % M == 0:
            yield N & 0xffff

A, B = 703, 516

gA, gB = generator(A, 16807), generator(B, 48271)
print ("🎄Part 1: {}".format(sum(next(gA) == next(gB) for _ in range(40000000))))

gA, gB = generator(A, 16807, 4), generator(B, 48271, 8)
print ("🎁🎄Part 2: {}".format(sum(next(gA) == next(gB) for _ in range(5000000))))

