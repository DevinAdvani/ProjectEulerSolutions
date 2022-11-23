eightynine = []
one = []
numbers = []

for i in range(1,10000000):
    numbers.append(i)

def f(x):
    y = str(x)
    n = 0
    for i in range(0,len(y)):
        n += int(y[i]) ** 2
    return n

for a in numbers:
    print(a)
    sequence = [a]
    p = a
    while True:
        p = f(p)
        sequence.append(p)
        if p == 89 or p == 1 or p in eightynine or p in one:
            break
    if p == 89 or p in eightynine:
        for b in sequence:
            eightynine.append(b)
    if p == 1 or p in one:
        for b in sequence:
            one.append(b)

print(len(eightynine))
