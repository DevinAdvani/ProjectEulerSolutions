def f(input,n):
    num = ""
    for i in range(1,n+1):
        num += str(int(input*i))
    return num 
pans = []
m = 2
a = 1
while a < 10000:
    if len(str(f(a,m))) == 9:
        pans.append(str(f(a,m)))
        a += 1
        m = 2  
    else:
        m += 1
    if len(str(f(a,m))) > 9 and len(str(f(a,m-1))) < 9:
        a += 1
        m = 2

def panchecker(n):
    nums = {"0"}
    for i in range(0,len(n)):
        if n[i] in nums:
            return False 
        nums.add(n[i])
    return True


truepans = []
for i in range(0,len(pans)):
    if panchecker(pans[i]):
        truepans.append(pans[i])
        
print(max(truepans))
