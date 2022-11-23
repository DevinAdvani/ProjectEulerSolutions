#pandigital checker for identity
#only need to cycle from 1 to 9999 i think:
def f(a,b):
    count = []
    string = ''
    string += str(a) + str(b) + str(a*b)
    if len(string) == 9:
        for i in range(0,9):
            count.append(int(string[i]))
        if set(count) == {1,2,3,4,5,6,7,8,9}:
            return True
        else:
            return False
    else:
        return False

num = []

for i in range(1,10000):
    for j in range(1,10000):
        if f(i,j):
            num.append(i*j)


print(sum(set(num)))
