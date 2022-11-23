def Sieve(n):
    """This function calculates all prime numbers up to a given limit(n)"""

    #Defining the inintial list, all equal to True
    primes = [True for i in range(n+1)]
    primes [0] = primes [1] = False

    #The starting number
    p = 2

    #Running a loop to check all numbers below the square root of the given number
    while p ** 2 < n:
        #Check to see if it is equal to True (if the number is prime or not)
        if primes[p]:
            #If it was a prime number, kill every other multiple of it
            for number in range(p*2, n+1, p):
                primes[number] = False

        #Increment the starting number by one to keep the loop working
        p += 1

    prime_numbers = [i for i in range (n+1) if primes[i]==True]
    #If you want to see the list of prime numbers in the output
    #return prime_numbers

    #If you want to see how many prime numbers are there in a given range
    return prime_numbers

list = Sieve(1000000)

for length in range(2,10):
    for position in range(0,len(list)-length):
        print(position)
        if sum(list[position:position+length]) in list:
            print(sum(list[position:position+length]))
