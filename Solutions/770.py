import itertools
n = 4
l = []
perms = []
for i in range(0,n):
    l.append('G')
    l.append('T')
perms = set(list(itertools.permutations(l)))

set = []

for i in range(0,len(perms)):
    for a in range(0,11):
        Agold = 1
        offering = a*0.1
        for b in range(0,len(list(perms)[i])):
            if (list(perms)[i])[b] == 'G':
                Agold += offering
            else:
                Agold -= offering
        set.append([i,a,Agold])

print(set)
