# IDK still quite confused

def PG(x):
    return int(x * (3*x -1)/2)

def PC(x):
    if (24*x + 1)**0.5 % 1 == 0:
        return True
    return False

Pentagons = []
for i in range(1,10000):
    Pentagons.append(PG(i))
    
for i in range(0,len(Pentagons)-1):
    for j in range(i+1,len(Pentagons)):
        if PC(Pentagons[i]+Pentagons[j]):
            if PC(Pentagons[j]-Pentagons[i]):
                print(i,j,Pentagons[i],Pentagons[j],Pentagons[j]-Pentagons[i])
                
