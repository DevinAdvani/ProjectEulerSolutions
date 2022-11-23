def PC(a):
    if isinstance(a**0.5,complex):
        return False
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

longest = 0
c = 0
d = 0

for a in range(-999,1000,1):
    for b in range(-1000,1001,1):
        n = 0
        l = []
        while PC(n**2 + a*n + b):
            l.append(n**2 + a*n + b)
            n += 1
        if n > longest:
            longest = n
            c = a
            d = b
        print(longest,c,d,a,b)
