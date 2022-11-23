def Pa(x):#Palindromic Checker
    a = str(x)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False

list = []

for i in range(1,1000000):
    print(i)
    if Pa(i):
        if Pa(bin(i)[2:]):
            list.append(i)


print(sum(list))
