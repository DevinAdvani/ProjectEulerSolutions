def M(n):
    count = 0
    for a in range(n,0,-1):
        for b in range(a,0,-1):
            for c in range(b,0,-1):
                if (a**2 + (b+c)**2)**0.5%1 == 0:
                    count += 1
                    #print(a,b,c)
    return (count)
    
i = -1
while True:
    i += 1
    print(i,M(i))