import numpy as np
import itertools

def combinazioni(n, k):
    if n < k:
        return 0
    f = np.math.factorial
    return float(f(n))/float(f(k)*f(n-k))

giocatori = 250
n = 10
for x in range(n, 18):
    p = combinazioni(10, n)*combinazioni(7, x-n)/combinazioni(17, x)
    print "estrazione #{}: prob. {:.3f} vincite {:.0f}".format(x, p, p*giocatori)
