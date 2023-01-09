import collections 
import itertools
remaining = []
for i in range(2,1000000):
    remaining.append(i)

def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n

def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)

def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result
    
def trans(n):
    return sum(list(get_divisors(n)))-n
done = []
def chain(n):
    chain = [n]
    done.append(n)
    while True:
        m = trans(chain[-1])
        if m in chain or m > 1000000 or m in done:
            break
        done.append(m)
        chain.append(m)
    return chain


for i in range(2,1000000):
    if i in remaining:
        print(chain(i))

        
        
