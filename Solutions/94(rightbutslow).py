def f(x):#x+1  -  return true if integral area
    s = (3*x + 1)/2
    A = (s*(s-x)*(s-x)*(s-(x+1)))**0.5
    if round(A) == A:
        return True
    else:
        return False
def g(x):#x-1  -  return true if intergral area
    s = (3*x - 1)/2
    A = (s*(s-x)*(s-x)*(s-(x-1)))**0.5
    if round(A) == A:
        return True
    else:
        return False


sum = 4

for i in range(2,333333334):
    print(i)
    if f(i):
        sum += 3*i + 1
    if g(i):
        sum += 3*i - 1

print(sum)
