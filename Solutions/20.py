def f(x):
    product = 1
    n = x
    for i in range(0,x):
        product *= n
        n -= 1
    list = []
    for i in range(0,len(str(product))):
        list.append(int(str(product)[i]))
    return sum(list)

print(f(100))
