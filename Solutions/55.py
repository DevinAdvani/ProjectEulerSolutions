def PalC(x):
    if str(x) == str(x)[::-1]:
        return True

def LycC(x):
    for i in range(0,50):
        x = x + int(str(x)[::-1])
        if PalC(x):
            return False
    return True

print(LycC(4994))
#Lychrel never forms a palindrome

count = 0
for i in range(1,10000):
    if LycC(i):
        count += 1

print(count)
