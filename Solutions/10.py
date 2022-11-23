'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
primes = []
nonprimes = []
for i in range(2,2000001):
    primes.append(i)

n = -1
while n < 2000000**0.5:
    n += 1
    for i in range(primes[n]*2,2000001,primes[n]):
        nonprimes.append(i)
    print(n)

primes = set(primes) - set(nonprimes)

print(sum(primes))
