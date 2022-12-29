""" 
pi (2a +1) - 1/ 2 +1
"""

def arraytosolutions(arrayofpowers):
    n = 1
    for i in range(0,len(arrayofpowers)):
        n *= ((2 * arrayofpowers[i])+1)
    return (n-1)/2 + 1
    
def numtoarray(num):
    primeindex = -1
    index = -1
    powerarray = []
    while num != 1:
        primeindex += 1
        if num % primes[primeindex] == 0:
            index += 1
            powerarray.append(0)
        while num % primes[primeindex] == 0:
            num /= primes[primeindex]
            powerarray[index] += 1
    return powerarray

def f(a):
    return arraytosolutions(numtoarray(a))

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
              
    return a
                

primes = list(primes_sieve2(1000000))


int = 1
maxsol = 0
while maxsol < 1000:
    int += 1
    sol = f(int)
    if sol > maxsol:
        maxsol = sol 
        print(int,maxsol)
