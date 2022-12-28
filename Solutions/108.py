""" 
pi (2a +1) - 1/ 2 +1
"""

def arraytosolutions(arrayofpowers):
    n = 1
    for i in range(0,len(arrayofpowers)):
        n *= arrayofpowers[i]
        return (n-1)/2 + 1
    
def numtoarray(num):
    n = 1
    index = 0
    powerarray = []
    while num != 1:
        n += 1
        while num % n:
            num /= n

maxsolutionnum = 0
n = 1
while maxsolutionnum < 1000:
    n += 1
    solutions = arraytosolutions(numtoarray(n))
    if solutions > maxsolutionnum:
        maxsolutionnum = solutions
        print(n,maxsolutionnum)
        
print(n,maxsolutionnum)