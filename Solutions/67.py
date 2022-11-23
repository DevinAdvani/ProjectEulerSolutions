k = open('67.txt','r')

Lines = k.readlines()

string = ''

for i in Lines:
    string += i[:-1]
    string += ' '

lol = string.split(" ")

lol.remove(lol[-1])

print(lol)

lam = []

for i in lol:
    lam.append(int(i))

print(lam)

L = lam

def Tri(x):
    return int(x * (x+1) * 0.5)

def iTri(x):
    return int(-0.5 + ((2 * x) + 0.25)**0.5)
list = []
for i in range(0,iTri(len(L))):
    for j in range(0,-Tri(i+1)+Tri(i+2)-1):
        l = []
        l.append(i)
        l.append(j)
        list.append(l)


for i in range(0,len(L)):
    xr = list[i][0]-1
    yr = list[i][1]
    xl = list[i][0]-1
    yl = list[i][1]-1
    try:
        left = L[list.index([xl,yl])]
    except ValueError:
        left = 0
    try:
        right = L[list.index([xr,yr])]
    except ValueError:
        right = 0
    if left > right:
        x = left
    else:
        x = right
    L[i] += x

print(max(L))
