from functools import reduce
filename = "input16a.txt"

with open(filename, "r") as f:
    fft = f.readline()
fft = fft.split("\n")[0]
pattern = [1, 0, -1, 0]

#fft = "80871224585914546619083218645595"
#fft = "19617804207202209144916044189917"
times = 100

offset = reduce(lambda acc, x: 10 * acc + x, value[:7], 0)
logical_len = 10000 * len(value)
assert offset < logical_len <= 2 * offset
value = [value[i % len(value)] for i in range(offset, logical_len)]
for _ in range(times):
    for i in reversed(range(1, len(value))):
        value[i - 1] += value[i]
    for i in range(len(value)):
        value[i] = abs(value[i]) % 10
print (''.join(map(str, value[:8])))

