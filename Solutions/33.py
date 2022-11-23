list = []

for n in range(10,100):
    for d in range(10,100):
        if str(n)[0] != '0' and str(d)[0] != '0' and str(n)[1] != '0' and str(d)[1] != '0':
            if n/d < 1:
                for i in range(0,2):
                    for j in range(0,2):
                        if str(n)[i] == str(d)[j]:
                            if n/d == int(str(n)[1-i]) / int(str(d)[1-j]):
                                list.append(str(n) + '/' + str(d))

print(list)

#found it then did da maths
