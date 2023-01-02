def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
              
    return a

primes = list(primes_sieve2(100))

for i in range(0,len(primes)):
    for j in range(i+1,len(primes)):
        