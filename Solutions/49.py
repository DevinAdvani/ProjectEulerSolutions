def PC(a):
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

def f(a,b):
    a1 = [0,0,0,0,0,0,0,0,0,0]
    b1 = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(str(a))):
        a1[int(str(a)[i])-1] += 1
    for i in range(0,len(str(b))):
        b1[int(str(b)[i])-1] += 1
    if a1 == b1:
        return True
    else:
        return False

primes = []

for i in range(1000,10000):
    if PC(i):
        primes.append(i)

for i in range(0,len(primes)):
    first = primes[i]
    for j in range(i+1,len(primes)):
        second = primes[j]
        difference = second - first
        third = second + difference
        if PC(third) and f(first,second) and f(first,third):
            print(first,second,third)
