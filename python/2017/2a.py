from utils import readInput

lines = readInput("input_2.txt")

checksum = 0
for l in lines:
    parts = list(map(int, l.split()))
    checksum += max(parts) -  min(parts)
    
print ("🎄Part 1: {}".format(checksum))
