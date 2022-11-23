'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def f(x): #enter number to find the largest prime factor
    list = []
    while True == True:
        for i in range(2,int(x)+2):
            print(list,i,x)
            if x % i == 0:
                list.append(i)
                x = x/i
                break
            if 1 == x:
                return max(list)

print(f(123456789))
