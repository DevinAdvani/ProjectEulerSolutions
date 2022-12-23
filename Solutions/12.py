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

def divisor_count(n):
    factors_list = prime_factors(n)
    factors_set = list(set(factors_list))
    divisors = 1
    for i in range(0,len(factors_set)):
        divisors *= (1 + factors_list.count(factors_set[i]))
    return divisors

n = 0
max = 0
while True:
    divisors = 0
    n += 1
    m = n*(n+1)/2
    divisors = divisor_count(m)
    if divisors > max:
        max = divisors 
        print(n,m,max)