from utils import readInput

lines = readInput("input_3.txt")

thrs = len(lines)/2
gamma = {}
for l in lines:
    for key, n in enumerate(l):
        gamma[key] = gamma.get(key, 0) + int(n)

print (gamma)
gamma_val = ""
for k, v in gamma.items():
    if v>thrs:
        gamma_val += "1"
    else:
        gamma_val += "0"
print (gamma_val)

epsilon_val = "".join(["0" if n == "1" else "1" for n in gamma_val])
print (epsilon_val)

gamma_val = int(gamma_val, 2)
epsilon_val = int(epsilon_val, 2)

print ("🎄 Part 1: ", epsilon_val*gamma_val)
