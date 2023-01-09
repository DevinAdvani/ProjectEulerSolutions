import math
def increasing(start,length):
    if length == 1:
        return 0
    if start == 9:
        return 1
    phi = 1
    for i in range(1,10-start):
        phi *= (length + i)
    return phi/math.factorial(9-start)

def decreasing(start,length):
    return increasing(9-start,length)-1

"""
numbers below 10^n are not bouncy
10^6, 12951 numbers are not bouncy
not bouncy nums = all nums - bouncy nums
bouncy nums = 
"""

power = 100
amount = 9
for i in range(2,power+1):
    amount += decreasing(9,i)
    amount += increasing(1,i)
    amount -= 9
    
print(amount)