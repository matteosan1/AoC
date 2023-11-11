from utils import readLines

inputs = readLines("input_1.txt")

freq = 0
freqs = []
while True:
    for i in inputs:
        #print (freq, i)
        freq = freq + int(i)
        if freq in freqs:
            print ("PRIMA RIPETUTA: ", freq)
            import sys
            sys.exit()
        freqs.append(freq)

print (freq)
