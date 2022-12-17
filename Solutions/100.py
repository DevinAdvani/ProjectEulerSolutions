n = 1
while True:
    if float((2*n*n - 2*n + 1)**0.5).is_integer():
        print(n,(2*n*n - 2*n + 1)**0.5)
    n += 1