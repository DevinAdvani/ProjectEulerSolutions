date = [1,1,1900]
day = 1
count  = 0
while True:
    print(date)
    print(day)
    date[0] += 1
    day += 1
    if day == 8:
        day = 1
    if date[0] == 31:
        if date[1] == 9 or date[1] == 4 or date[1] == 6 or date[1] == 11:#need to add month variations and leap year
            date[0] = 1
            date[1] += 1
    if date[0] == 29 and date[1] == 2 and (not date[2] % 4 == 0 or (date[2] % 100 == 0 and not date[2] % 400 == 0)):
        date[0] = 1
        date[1] += 1
    if date[0] == 30 and date[1] == 2 and (date[2] % 4 == 0 or (date[2] % 100 == 0 and date[2] % 400 == 0)):
        date[0] = 1
        date[1] += 1
    if date[0] == 32:
        if date[1] == 1 or date[1] == 3 or date[1] == 5 or date[1] == 7 or date[1] == 8 or date[1] == 10 or date[1] == 12:#need to add month variations and leap year
            date[0] = 1
            date[1] += 1
    if date[1] == 13:
        date[1] = 1
        date[2] += 1
    if date[0] == 1 and day == 7 and date[2] >= 1901:
        count += 1
    if date == [31,12,2000]:
        break

print(count)
