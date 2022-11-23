import math

def f(x):
    sum = 0
    for i in range(0,len(str(x))):
        sum += math.factorial(int(str(x)[i]))
    return sum

def g(x):
    n = f(x)
    count = 1
    while int(n) != int(x):
        n = f(n)
        count += 1
    return count

print(g(169))
