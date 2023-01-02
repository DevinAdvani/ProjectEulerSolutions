import math
def S(p):
    sum = 0
    for k in range(1,6):
        sum += math.factorial(p-k)
    return (sum % p)
    
def sigma(q):
    sum = 0
    for n in range(5,q):
        sum += S(n)
    return sum 

for i in range(5,200):
    print(i,S(i))