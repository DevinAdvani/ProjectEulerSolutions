'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math

def PC(a):
    b = 0
    for i in range (2,round(math.sqrt(a))+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False
x = 1
primes = []
while True:
    x += 1
    if PC(x) == True:
        primes.append(x)
    if len(primes) == 10001:
        print(primes[10000])
        break
