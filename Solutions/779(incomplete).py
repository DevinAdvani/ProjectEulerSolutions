'''
For a positive integer , let  be the smallest prime dividing , and let  be its p-adic order, i.e. the largest integer such that
 divides .

For a positive integer , define the function
 by:


Also define

 by:





It can be verified that

.

Find


. Give your answer rounded to  digits after the decimal point.
'''
def p(n): #THIS WORKS
    x = 1
    while True:
        x += 1
        if n % x == 0:
            return x

def a(n): # THIS DOESN'T WORK BECAUSE THE COMPUTER CANT COMPUTER HIGH DIGITS
    y = n
    while True:
        y -= 1
        if rnd(n/(p(n)**y) == n/(p(n)**y:
            return y

def f(k,n):
    return (a(n)-1)/(p(n)**k)

def fk(K,N):#let N tend to infinity
    SUM = 0
    for i in range(2,N+1):
        SUM += f(K,i)
    return (1/N)*(SUM)

print(a(2011))

#IDK how to do this because numbers get too big for computer to process properly
