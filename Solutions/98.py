def f(x):
    alpha = ' ABCDEFGHIJKLMMNOPQRSTUVWXYZ'
    sum = []
    for i in x:
        sum.append(alpha.index(i))
    print(sum)

f('CARE')

#not letter related
#find every word which has a back to front
#then in that list find the lengths and reverse engineer
#and find square numbers that are x digits long back to front
#figure out zeroes
