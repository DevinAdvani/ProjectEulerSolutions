P = [1]

def q(n):
    list = []
    change1 = 1
    change2 = 1
    while True:
        if n < 0:
            return list 
        n -= change1 
        change1 += 2
        if n > -1:
            list.append(n)
        if n < 0:
            return list 
        n -= change2 
        change2 += 1
        if n > -1:
            list.append(n)
        
def p(n):
    indexes = q(n)
    count = 0
    posneg = 0
    for i in indexes:
        if posneg < 2:
            count += P[i]
        else:
            count -= P[i]
        posneg += 1
        posneg = posneg%4
    P.append(count) 
    

    
i = 0
while P[-1]%1000000 != 0:
    print(P[-1])
    i += 1
    p(i)
    
print(i,P[-1])