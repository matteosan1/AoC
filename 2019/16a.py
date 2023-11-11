from functools import reduce
filename = "input16a.txt"

with open(filename, "r") as f:
    fft = f.readline()
fft = fft.split("\n")[0]
pattern = [1, 0, -1, 0]

#fft = "80871224585914546619083218645595"
#fft = "19617804207202209144916044189917"
times = 100

patterns = []
for shift in range(len(fft)):
    new_pattern = [] #[0]*shift
    for p in pattern:
        new_pattern.extend([p]*(shift+1))
    patterns.append(new_pattern)

for phase in range(times):
    out = ""
    for j in range(len(fft)):
        np = len(patterns[j])
        temp = 0
        for i in range(len(fft)-j):  
            #print (fft[i+j], patterns[j][i%np])
            temp += int(fft[i+j]) * patterns[j][i%np]
            #print ("temp", temp)
        #print ("TEMP ", temp)
        out += str(abs(temp)%10)
    #print ("OUT", out)
    fft = out
print (fft[:8])
