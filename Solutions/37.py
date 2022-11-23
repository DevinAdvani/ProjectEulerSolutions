def PC(a):
    if a == 1:
        return False
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

def Tr(x):
    for i in range(0,len(str(x))):
        if not (PC(int(str(x)[i:]))):
            return False
    for i in range(0,len(str(x))):
        if not (PC(int(str(x)[0:i+1]))):
            return False
    return True

l = []
i = 1
while len(l) != 11:
    i += 2
    print(len(l),i)
    if Tr(int('2'+str(i))):
        l.append(int('2'+str(i)))
    if Tr(int('3'+str(i))):
        l.append(int('3'+str(i)))
    if Tr(int('5'+str(i))):
        l.append(int('5'+str(i)))
    if Tr(int('7'+str(i))):
        l.append(int('7'+str(i)))

print(l,len(l),sum(l))

#add 2,3,5,7 onto the end as it is more efficient
