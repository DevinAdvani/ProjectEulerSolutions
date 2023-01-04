"""
n can't equal 8 or 9, or 5 or 6 as the digits add up to a multiple of 3 which makes it divisble by 3
therefore 4 or 7 is the only answer
"""
nums = {7,6,5,4,3,2,1}

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
              
    return a
    
pans = []

for a in range(1,8,2):
    for b in nums-{a}:
        for c in nums-{a,b}:
            for d in nums-{a,b,c}:
                for e in nums-{a,b,c,d}:
                    for f in nums-{a,b,c,d,e}:
                        for g in nums-{a,b,c,d,e,f}:
                            pans.append(int(str(g)+str(b)+str(c)+str(d)+str(e)+str(f)+str(a)))
                            

primes = set(primes_sieve2(7654321))

print(max(set(pans).intersection(primes)))