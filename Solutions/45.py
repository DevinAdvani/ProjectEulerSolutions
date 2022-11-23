def T(n):
    return n*(n+1)*0.5

def P(n):
    return n*(3*n - 1)*0.5

def H(n):
    return n*(2*n - 1)

tri = []
pent = []
hex = []

for i in range(1,100000):
    tri.append(int(T(i)))
    pent.append(int(P(i)))
    hex.append(int(H(i)))

print((set(tri).intersection(set(pent)).intersection(set(hex))))
