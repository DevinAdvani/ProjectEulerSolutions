list = []

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for k in range(2,1000):
    if not(set(prime_factors(k))=={2}) and not(set(prime_factors(k))=={5}) and not(set(prime_factors(k))=={2,5}):
        for n in range(1,20):
            if ((10**n - 1)/k).is_integer():
                print(k,n,(10**n - 1)/k)