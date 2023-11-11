import time
t = time.time()
val = 20151125
x = [1, 1]
final = [3075, 2981]
ymax = 1
n = 1
while x != final:
    if x[1] == 1:
        x[1] = ymax + 1
        ymax = x[1]
        x[0] = 1
    else:
        x[0] = x[0] + 1
        x[1] = x[1] - 1
    n += 1
    val = (val * 252533) % 33554393
print (x, n, val)
print (time.time()-t)
