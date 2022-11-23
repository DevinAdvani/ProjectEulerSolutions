import math

def PC(a):#Prime Checker
    b = 0
    for i in range (2,round(math.sqrt(a))+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

def D(x):#divisors creator
    list = []
    for i in range(1,x+1):
        if x % i == 0:
            list.append(i)
    return list

def TC(x): #Triangle Checker
    a = 0
    d = 1
    while True:
        a += d
        d += 1
        if a == x:
            return True
        if a > x:
            return False

#create a list of a decent quantity of prime numbers
#then create a combination of all the different prime numbers so that there are over 500 divisors
#while one can do one of each prime number, one can get a lower number based simply off of repeats

def PG():#prime generator below 100
    l = []
    for i in range(2,100):
        if PC(i):
            l.append(i)
    return l

def FTN():#converting the concept of a list of factors into the actual number
    n = 1
    for i in range(0,25):
        n *= PG()[i] ** factors[i]
    return n

print(len(D(2**4 * 3**4 * 5**4 * 7 * 11)))
