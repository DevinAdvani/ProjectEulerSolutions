s = '0'
n = 0
while len(s) < 1000005:
    n += 1
    s += str(n)
    print(n)


print(int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000]))
