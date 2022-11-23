#make a list of primes and then go through every possible number and create a list with mutliples of whatever
#then combine 2 and 3 if possible then combine that with 4 if possible and keep on going

#ive done it in a really dumb and inefficient manner

primes = [2,3,5,7,11,13,11,17]
list = []
for i in primes:
    sublist = []
    for j in range(1,1000):
        if j % i == 0:
            a = str(j)
            if len(a) == 3:
                sublist.append(a)
            if len(a) == 2:
                sublist.append('0' + a)
            if len(a) == 1:
                sublist.append('00' + a)
    list.append(sublist)

two = []

for i in list[0]:
    for j in list[1]:
        if i[-2:] == j[:2]:
            two.append(i[:-2] + j)

three = []

for i in two:
    for j in list[2]:
        if i[-2:] == j[:2]:
            three.append(i[:-2] + j)

five = []

for i in three:
    for j in list[3]:
        if i[-2:] == j[:2]:
            five.append(i[:-2] + j)

seven = []

for i in five:
    for j in list[4]:
        if i[-2:] == j[:2]:
            seven.append(i[:-2] + j)

eleven = []

for i in seven:
    for j in list[5]:
        if i[-2:] == j[:2]:
            eleven.append(i[:-2] + j)

somelist = []

for i in eleven:
    if int(i[-3:]) % 17 == 0:
        somelist.append(i)

def f(a):
    count = []
    for i in range(0,8):
        count.append(int(a[i]))
    if len(set(count)) == 8:
        return True
    else:
        return False

anotherlist = []

for i in somelist:
    print(f(i))
    if f(i):
        anotherlist.append(i)

print(somelist)
print(anotherlist)

#filter eleven for pandigitial and final multiple of 17
