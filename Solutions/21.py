def d(n):
    l = []
    for i in range(1,n):
        if n % i == 0:
            l.append(i)
    return sum(l)

list = []

for a in range(1,10000):
    print(a)
    b = d(a)
    if a != b and d(b) == a:
        list.append(a)

print(sum(list))
