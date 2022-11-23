import math
import decimal

def f(y):
    b = [y]
    for i in range(0,24):
        b.append(math.floor(b[-1])*(b[-1]-math.floor(b[-1])+1))
    a = []
    for x in b:
        a.append(str(math.floor(x)))
    e = ''.join(a)
    h = decimal.Decimal(e[0:1]+'.'+e[1:25])
    return h

def g(theta):
    return decimal.Decimal(str(decimal.Decimal(theta) - f(theta))[:26])


def BS(n,inputlist):#n is number trying to be inverted, into is the list
    outputlist = []
    for i in inputlist:
        outputlist.append(g(i))
    low = list
    high = list
    print(low,high)
    low = [x for x in low if x < n]
    high = [x for x in high if x > n]
    low = max(low)
    high = min(high)
    return((inputlist[outputlist.index(low)]+inputlist[outputlist.index(high)])/2)

#increase and decrease number magnitude by 10^24 in order for functions to work properly

BS(0,[2,3])
