def PF(x):
    factors = []
    a = 2
    while x != 1:
        if x % a == 0:
            factors.append(a)
            x = x/a
        else:
            a += 1
    return factors

print(PF(525806))
#factorise into simpler forms
#equations simplifier
#for numbers and powers themselves
