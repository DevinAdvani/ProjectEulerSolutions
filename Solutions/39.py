def f(a1,p1):
    if p1-a1 == 0:
        return 0
    c1 = (2*a1**2 + p1**2 - 2*a1*p1)/(2*p1-2*a1)#
    return c1

Q = []

for p in range(1,1001):
    sum = 0
    for a in range(1,1001):
        if f(a,p) == int(f(a,p)) and f(a,p) != 0:
            sum += 1
    Q.append(sum)

print(Q.index(max(Q))+1)
