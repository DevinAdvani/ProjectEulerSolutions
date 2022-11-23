import math as m
def f(x):
    sum = 0
    for i in range(0,len(str(x))):
        sum += m.factorial(int(str(x)[i]))
    return sum

list = []
for i in range(3,1000000):
    if i == f(i):
        list.append(i)

print(sum(set(list)))
