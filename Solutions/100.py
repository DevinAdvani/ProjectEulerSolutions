def Blue(x):
    return -((2*x -1)/2) + (x**2 - x + ((2*x -1)/2)**2)**0.5

B = 707107

print((B + Blue(B)))
#just use algebra x is greater than 707107

while True:
    B += 1
    if (B + Blue(B))%1 == 0:
        print(B)
        break

#331255 if
#need to not fuck up the algebra and find the minimum q and then justiterate from there
