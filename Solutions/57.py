from fractions import Fraction
'''
did some algebra and if Fn = a/b
then Fn+1 = 2b + a / b + a
'''

a = [3]
b = [2]

for i in range(1,1000):
    a1 = 2 * b[-1] + a[-1]
    b1 = b[-1] + a[-1]
    a.append(a1)
    b.append(b1)

count = 0

for i in range(0,1000):
    c = (str(Fraction(a[i],b[i])))
    x = (c.split('/'))
    if len(x[0]) > len(x[1]):
        count += 1

print(count)
