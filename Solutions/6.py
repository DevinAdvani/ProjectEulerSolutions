'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def f(x):
    sumofsquares = 0
    squareofsum = 0
    for i in range(1,x+1):
        sumofsquares += i**2
    for i in range(1,x+1):
        squareofsum += i
    squareofsum = squareofsum**2
    return abs(squareofsum - sumofsquares)

print(f(100))
