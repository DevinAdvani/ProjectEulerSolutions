colindistribution = []
peterdistribution = []


for i in range(0,37):
    colindistribution.append(0)
    peterdistribution.append(0)

for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        colindistribution[a+b+c+d+e+f] += 1#/46656
        

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    peterdistribution[a+b+c+d+e+f+g+h+i] += 1#/262144
           
           
peterwins = 0
peterdraws = 0
peterloss = 0           
                                   
for a in range(0,37):
    for b in range(0,37):
        if a > b:
            peterwins += peterdistribution[a]*colindistribution[b]
        if a == b:
            peterdraws += peterdistribution[a]*colindistribution[b]
        if a < b:
            peterloss += peterdistribution[a]*colindistribution[b]

divisor = 262144*46656

probs = peterwins/(divisor - peterdraws)

print(peterwins/divisor)