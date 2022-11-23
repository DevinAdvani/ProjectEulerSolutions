def PF(x):
    factors = []
    a = 2
    while x != 1:
        if x % a == 0:
            factors.append(a)
            x = x/a
        else:
            a += 1
    return factors

n = 10
ocount = 0

while True:
    print(n)
    n += 1
    z = len(set(PF(n)))
    if 4 == z:
        ocount += 1
    else:
        ocount = 0
    count = z
    print(z)
    if ocount == 4:
        print (n - 3)
        break
