seq = [1]
step = 0
while seq[-1] != 1001**2:
    step += 2
    for i in range(0,4):
        seq.append(seq[-1]+step)
    print(seq[-1])

print(sum(seq))
