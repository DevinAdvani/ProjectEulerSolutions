import numpy as np
import math

def v2(n):
    r = round(np.log(n)/np.log(2))
    while n % (2**r) != 0:
        r -= 1
    if n % (2**r) == 0:
        return r

def mag(x):
    return math.sqrt(sum(i**2 for i in x))

def S(n):
    sum = np.matrix([[0],[0]])
    for i in range(1,n+1):
        sum += np.matrix([[(2*i)*((-2)**i)],[(i*((-2)**i))]])
    return mag(sum)

print(S(4))
