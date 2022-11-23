count = 0
for i in range(1,100):
    for j in range(1,100):
        if len(str(i**j)) == j:
            #print(i**j,i,j)
            count += 1

print(count)
