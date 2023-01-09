fdict = {}
fdict[1] = 1
fdict[3] = 3
sdict = {}
sdict[1] = 1

def f(n):
    try:
        return fdict[n]
    except:
        pass
    try:
        if n%2 == 0:
            a = f(n/2)
            fdict[n/2] = a
            return a
    except:
        pass
    try:
        if (n-1)%4 == 0:
            k = (n-1)/4
            a = f(2*k + 1)
            b = f(k)
            fdict[2*k + 1] = a 
            fdict[k] = b
            return 2*a - b
    except:
        pass 
    try:
        if (n-3)%4 == 0:
            k = (n-3)/4
            a = f(2*k + 1)
            b = f(k)
            fdict[2*k + 1] = a
            fdict[k] = b 
            return 3*a - 2*b
    except:
        pass

def S(n):
    count = 0
    for i in range(1,n+1):
        count += f(i)
    return count

p = 0
count = 0
while True:
    p += 1
    count += f(p)
    print(p,count)