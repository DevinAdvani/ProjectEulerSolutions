#find a convertor into a number
#then a deconvertor in to an roman numeral form

def RNTN(x):#Roman Numeral To Number
    count = 0
    for i in range(0,len(x)):
        if x[i] == 'I':
            count += 1
        if x[i] == 'V':
            count += 5
        if x[i] == 'X':
            count += 10
        if x[i] == 'L':
            count += 50
        if x[i] == 'C':
            count += 100
        if x[i] == 'D':
            count += 500
        if x[i] == 'M':
            count += 1000
    return count

def NTRN(x):
    I = 0
    V = 0
    X = 0
    L = 0
    C = 0
    D = 0
    M = 0
    for i in range(0,x):
        I += 1
        if I == 5:
            I = 0
            V += 1
        if V == 2:
            V = 0
            X += 1
        if X == 5:
            X = 0
            L += 1
        if L == 2:
            L = 0
            C += 1
        if C == 5:
            C = 0
            D += 1
        if D == 2:
            D = 0
            M += 1
    string = ''
    for i in range(0,M):
        string += 'M'
    for i in range(0,D):
        string += 'D'
    for i in range(0,C):
        string += 'C'
    for i in range(0,L):
        string += 'L'
    for i in range(0,X):
        string += 'X'
    for i in range(0,V):
        string += 'V'
    for i in range(0,I):
        string += 'I'
    return string

for i in range(1,100):
    print(i,NTRN(i))

#need to increase efficiency
