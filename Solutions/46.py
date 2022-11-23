#composite is a number that can be written as the product of two smaller positive integers 8 = 2 * 4
composite = []
for i in range(3,1000,2):
    for j in range(3,1000,2):
        composite.append(i*j)
print(sorted(list(set(composite))))

def PC(a):
    if a <= 1:
        return False
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

def Gb(x):
    for i in range(1,round(x**0.5)):
        if PC(x - (2 * (i**2))):
            return True
    else:
        return False

for n in sorted(list(set(composite))):
    print(n,Gb(n))
    if not Gb(n):
        print(n)
        break
