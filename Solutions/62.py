cubes = []
for i in range(1,1000000):
    if len(str(i**3)) == 5:
        cubes.append(i**3)
print(cubes)

#put through certain number of digits - all numbers of n digits
#function that adds the q of each digit and checks them
def f(a,b):
    a1 = [0,0,0,0,0,0,0,0,0,0]
    b1 = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(str(a))):
        a1[int(str(a)[i])-1] += 1
    for i in range(0,len(str(b))):
        b1[int(str(b)[i])-1] += 1
    if a1 == b1:
        return True
    else:
        return False

for i in (0,len(cubes)):
    n = 0
    for j in (i,len(cubes)):
        if f(cubes[i],cubes[j]):
            n += 1
    print(n)
