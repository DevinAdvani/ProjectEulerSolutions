inputlimit = 50
outputlimit = round(-0.5 + (inputlimit + 0.25)**0.5)
if outputlimit%2==0:
    outputlimit -= 1

for m in range(3,outputlimit+2,2):
    for n in range(1,m,2):
        print(m*n + m**2,m*n,(m**2-n**2)/2,(m**2+n**2)/2)