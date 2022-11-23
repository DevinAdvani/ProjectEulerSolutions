d = {
0 : '',
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
10 : 'ten',
11 : 'eleven',
12 : 'twelve',
13 : 'thirteen',
14 : 'fourteen',
15 : 'fifteen',
16 : 'sixteen',
17 : 'seventeen',
18 : 'eighteen',
19 : 'nineteen',
20 : 'twenty',
30 : 'thirty',
40 : 'forty',#fucking americans
50 : 'fifty',
60 : 'sixty',
70 : 'seventy',
80 : 'eighty',
90 : 'ninety',
100 : 'hundred',
1000 : 'thousand'
}

def STW(x):#need to convert to physical words
    if x <= 20:
        a = d[x]
        return a
    elif len(str(x)) == 2:
        a = d[int(str(x)[0] + '0')]
        b = d[int(str(x)[1])]
        return a + b
    elif len(str(x)) == 3:
        if int(str(x)[1:3]) <= 20:
            a = d[int(str(x)[1:3])]
        else:
            a = d[int(str(x)[1] + '0')] + d[int(str(x)[2])]
        c = d[int(str(x)[0])]
        if x % 100:
            e = 'and'
        else:
            e = ''
        return c + 'hundred' + e + a
    elif x == 1000:
        return 'onethousand'

count = 0

for i in range(1,1001):
    count += len(STW(i))

print(count)
