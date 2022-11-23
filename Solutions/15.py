import itertools

''' #raw power method but inefficient
def f(x):#where x is x by x grid
    single = []
    for i in range(0,x):
        single.append("R")
        single.append("D")
    return len(set(list(itertools.permutations(single))))
'''

def fact(x):
    sum = 1
    while x != 1:
        sum *= x
        x -= 1
    return sum

def f(x):
    return fact(x)/(fact(x/2)**2)


#multiple of two as paths are reflections
print(f(40))
