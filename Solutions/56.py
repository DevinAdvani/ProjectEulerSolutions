list = []
for a in range(1,100):
    for b in range(1,100):
        list.append(a**b)

def f(x):
    sum = 0
    for i in range(0,len(str(x))):
        sum += int(str(x)[i])
    return sum

set = []

for i in range(0,len(list)):
    set.append(f(list[i]))

print(max(set))
