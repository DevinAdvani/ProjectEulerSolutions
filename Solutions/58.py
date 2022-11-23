def f(x):
    seq = [1]
    step = 0
    while seq[-1] < x**2:
        step += 2
        for i in range(0,4):
            seq.append(seq[-1]+step)
    return seq

def PC(a):
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

def g(l):
    count = 0
    for i in l:
        if PC(i):
            count += 1
    return 100 * count/len(l)

n = 20000

while g(f(n)) > 10:
    print(n,g(f(n)))
    n += 1

print(n)

#manual binary search 15000<x

#more efficient by going backwards from massive matrix then also a more efficient generation of primes
