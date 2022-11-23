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

x = 0
while True:
    x += 1
    print(x)
    if f(x,2*x) and f(x,3*x) and f(x,4*x) and f(x,5*x) and f(x,6*x):
        print(x)
        break
