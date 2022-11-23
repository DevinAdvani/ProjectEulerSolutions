list = []

def f(x):
    sum = 0
    for i in range(0,len(str(x))):
        sum += int(str(x)[i])**5
    return sum

for i in range(2,1000001):
    print(i)
    print(list)
    if i == f(i):
        list.append(i)

print(list)
