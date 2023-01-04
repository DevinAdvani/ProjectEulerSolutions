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

primedatastructure = [0]
count = 0 
for i in range(0,len(primes)):
    count += primes[i]
    primedatastructure.append(count) 

max = 0
answer = 0

def f(start,end):
    return primedatastructure[end]-primedatastructure[start]

for i in range(0,len(primes)-max):
    for j in range(i+1+max,len(primes)):
        length = j-i 
        amount = f(i,j)
        if amount > 1000000:
            break
        if amount in primes:
            if length > max:
                max = length  
                print(amount)
print(max,amount)