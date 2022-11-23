'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def f(x,y,z): #x is one multiple, y is another, z is the upper limit
    xlist = []
    ylist = []
    for i in range(0,z+1):
        if i % x == 0:
            xlist.append(i)
    for i in range(0,z):
        if i % y == 0:
            ylist.append(i)
    c = set(xlist).union(set(ylist))
    return sum(c)

print(f(3,5,1000))
