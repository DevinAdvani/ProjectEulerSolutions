#find the probability of a win,draw or loss
#use algebra
#overall win = win + draw(win + draw(..
#overall win = win + draw(overall win)
#overall win - draw(overall win) = win
#overall win(1-draw) = win
#overall win = win/(1-draw)

#use stats knowledge

peter = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    peter.append(a+b+c+d+e+f+g+h+i)
colin = []
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        colin.append(a+b+c+d+e+f)
wins = 0
draws = 0
loss = 0
count = 0
for c in colin:
    count += 1
    print(wins,draws,loss,count)
    for p in peter:
        if p > c:
            wins += 1
        if p == c:
            draws += 1
        if p < c:
            loss += 1

total = wins+draws+loss

print(win,draws,loss,total)
