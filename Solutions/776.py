import matplotlib.pyplot as plt

def d(n):
    l = []
    m = 0
    for i in range(0,len(str(n))):
        l.append(int(str(n)[i]))
    for i in range(0,len(str(n))):
        m += l[i]
    return m

def F(N):
    sum = 0
    for n in range(1,N+1):
        print(n)
        sum += n/d(n)
    return sum

x=[]
y=[]
for i in range(1,100):
    x.append(i)
    y.append(F(i))

plt.scatter(x, y)
plt.show()
