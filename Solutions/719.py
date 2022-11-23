def b(x,n):
    lol = 
    binary = format(x,'014b')

    return binary

def Split(x):
    list = []
    for i in range(0,2 ** (len(str(x)) - 1)):
        list.append(b(i))
    return list

print(Split(8145))
