def f(n):
    list = [290797]
    for i in range(0,n):
        list.append((list[-1]**2)%50515093)
    products = []
    for i in range(1,n):
        for j in range(1,n):
            if i < j:
                products.append(list[i]*list[j])
    print(products)

f(3)
