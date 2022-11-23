for i in range(0,999999999+1,1):
    a = []
    for b in range(0,9):
        a.append('0')
    for j in range(1,10):
        try:
            a[-j] = str(i)[-j]
        except IndexError:
            pass
    c = []
    for d in range(1,10):
        c.append(str(d))
        c.append(a[d-1])
    c.append('0')
    e = ''
    for f in c:
        e += f
    g = int(e)
    print(g)
    if g**0.5 % 1 == 0:
        print(g**0.5)
        break
    #insert into thing
    #check if square root is a proper integer
