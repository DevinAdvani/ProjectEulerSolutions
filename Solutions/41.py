#only goes up to nine digits
#try for nine digits
#prime check each one

def PC(a):
    b = 0
    for i in range (2,round(a**0.5)+1):
        if a/i == int(a/i):
            b += 1
    if b == 0:
        return True
    else:
        return False

print(PC(123456789))
