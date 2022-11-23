def PC(a):
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

def C(x):#circulate
    list = []
    for i in range(0,len(str(x))):
        list.append(int(str(x)[i:]+str(x)[:i]))
    return(list)

def f(b):
    list = C(b)
    for c in list:
        if not(PC(c)):
            return False
    return True

set = [2]

for i in range(3,1000000,2):
    print(i)
    if f(i):
        set.append(i)

print(len(set))
