'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def f(x,y):#x is lower bound and y is the upper bound
    list = []
    for a in range(x,y+1):
        for b in range(x,y+1):
            z = a*b
            if str(z) == str(z)[::-1]:
                list.append(a*b)
    return max(list)

print(f(100,999))
