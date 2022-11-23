def PG(x):#Pentagonal Generator
    return x*(3*x - 1)*0.5

def PC(x):#Pentagonal Checker
    y = (1/6 + ((1/36)+(2/3)*x)**0.5)
    if y == int(y):
        return True
    else:
        return False

D = 100000000

k = 100000

for i in range(1,k):
    print(i)
    print(D)
    for j in range(i+1,k):#i is less than j
        if PC(PG(i)+PG(j)):
            #if PC(PG(j)-PG(i)):
            #if PC(PG(j)-PG(i)) < D:
                D = PC(PG(j)-PG(i))
                if D == True:
                    break
print(D)
