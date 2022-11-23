def f(x):#x is the denominator
    fractions = []
    decimals = []
    new_fractions = []
    for i in range(1,x):
        print(i)
        for j in range(1,x+1):
            if j > i and not CF(i,j):
                fractions.append(str(i) + '/' + str(j))
                decimals.append(i/j)
    for x in sorted(decimals):
        new_fractions.append(fractions[decimals.index(x)])
    return new_fractions.index('1/2') - new_fractions.index('1/3') -1

def CF(a,b):
    if a < b:
        smallest = a
    else:
        smallest = b
    for i in range(2,smallest+1):
        if a % i == 0 and b % i == 0:
            return True
    return False

print(f(12000))
