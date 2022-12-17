def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
    
def PEF(x):
    return x/phi_func(x)

generatedprimes = []

def SieveOfEratosthenes(num):
    x = 1
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
  
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
  
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
  
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            x *= p
            print(x)
            if x > 1000000:
                exit()
            
SieveOfEratosthenes(1000)