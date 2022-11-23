list = []
for i in range(1,1000000):
    list.append(i)

def f(x):
    l = []
    for i in range(1,round(x/2)+1):
        if x%i == 0:
            l.append(i)
    return sum(l)

print(f(1000000))

#start at one and find the chain
#remove chain from overall list and store lowest number
#iterate through
