def Collatz(x):
    l = []
    while x != 1:
        l.append(x)
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x + 1
    return len(l)

lengths = []

for i in range(1,1000001):
    print(i)
    lengths.append(Collatz(i))

print(lengths.index(max(lengths))+1)
