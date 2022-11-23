import itertools
def f(code,login):#LOGIN IS THREE DIGITS
    code = str(code)
    login = str(login)
    try:
        one = code.index(login[0])
    except ValueError:
        one = 0
    try:
        two = code.index(login[1],one)
    except ValueError:
        two = 0
    try:
        three = code.index(login[2],two)
    except ValueError:
        three = 0
    if one < two < three:
        return True
    else:
        return False

keylog = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]

lol = []
for i in keylog:
    for j in range(0,3):
        lol.append(str(i)[j])

p = list(set(lol))

g = list(itertools.permutations(list(p)))

#need to turn g into a code

e = []
for i in g:
    e.append(str(''.join(i)))


for i in range(0,len(e)):
    check = 0
    for j in range(0,len(keylog)):
        if not f(e[i],keylog[j]):
            check += 1
    if check == 0:
        print(e[i])
        break
