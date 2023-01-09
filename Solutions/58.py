def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

num = 3
denom = 5
goal = 0.1
start = 9
step = 4
while goal < num/denom:
    for i in range(0,4):
        start += step 
        if is_prime(start):
            num += 1
    denom += 4
    step += 2
    print(num,denom,num/denom,(denom+1)/2)