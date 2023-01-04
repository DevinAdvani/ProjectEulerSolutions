
def b(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if (n-2) % 3 == 0:
        return 2*((n-2)/3 + 1)
    else:
        return 1

A = [2,3]

for i in range(0,98):  
    m = len(A)
    A.append(int(b(m)*A[-1] + A[-2]))

n = 100


res = sum(int(digit) for digit in str(A[n-1]))
print(A[n-1])


# 
# Solution to Project Euler problem 65
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 


def compute():
	numer = 1
	denom = 0
	for i in reversed(range(100)):
		numer, denom = e_contfrac_term(i) * numer + denom, numer
        print(numer)
	ans = sum(int(c) for c in str(numer))
	return numer


def e_contfrac_term(i):
	if i == 0:
		return 2
	elif i % 3 == 2:
		return i // 3 * 2 + 2
	else:
		return 1


if __name__ == "__main__":
	print(compute())