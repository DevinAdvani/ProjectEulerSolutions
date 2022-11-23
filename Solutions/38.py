def f(a,n):
    list1 = []
    for i in range(1,n+1):
        list1.append(i)
    list2 = []
    for i in list1:
        list2.append(i*a)
    string = ''
    for i in list2:
        string += str(i)
    return int(string)

list = []

for c in range(1,1000):
    for b in range(1,1000):
        if len(str(f(c,b))) == 9:
            print(c,b)
            list.append(f(c,b))
            print(list)

print(list)

#IDK i can do it but idk im doing something wrong
