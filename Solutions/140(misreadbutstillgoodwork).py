def G(k):#Basically just the nth fibonacci number with the first numbers being one and four
    ks = [1,4]
    if k == 1:
        return 1
    if k == 2:
        return 4
    while len(ks) != k:
        ks.append(ks[-1]+ks[-2])
    return ks[-1]

def AG(x):#input x into the function with o being the order, i.e. the final power
    sum = 0
    for n in range(1,1001):
        sum += (x**n)*(G(n))
    return sum

def BS(n,into):#n is number trying to be inverted, into is the list
    list = []
    for i in into:
        list.append(AG(i))
    low = list
    high = list
    low = [x for x in low if x < n]
    high = [x for x in high if x > n]
    low = max(low)
    high = min(high)
    return((into[list.index(low)]+into[list.index(high)])/2)

def C(x):#x is the number trying to be found out
    l = [0,1]
    z = 0.5
    while round(AG(z),8) != x:
        z = BS(x,l)
        l.append(BS(x,l))
        print(l)
    return round(z,8)

sigma = 0

for i in range(1,31):
    sigma += C(i)

print(sigma)
