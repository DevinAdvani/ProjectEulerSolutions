from itertools import permutations

def f(str):
    list = []
    perm = sorted(''.join(chars) for chars in permutations(str))
    for x in perm:
        list.append(x)
        if len(list) == 1000000:
            print(list[-1])
            break

str = '1234567890'

print(f(str))
