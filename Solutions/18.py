def b(x):
    binary = format(x,'014b')

    return binary

def f(x):
    a = x.replace(' ','')
    list = []
    for i in range(0,len(a),2):
        list.append(int(a[i:i+2]))
    choices = []
    for i in range(0,2**14):
        choices.append(b(i))
    counts = []
    for a in choices:
        level = 0
        position = 0
        count = 0
        while level != 14:
            print(count)
            position += int(str(a)[level]) + 1 + level
            level += 1
            count += list[position]
        counts.append(count)
    print(counts)

#something is correct and something is wrong

f('75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23')

#answer was 999 plus 75 as i left it out
