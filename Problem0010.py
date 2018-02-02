'''
Project Euler Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def is_prime(n, primes):
    #primes is the list of primes smaller than n
    max_check = int((n ** .5) + 1)
    for prime in primes:
        if prime > max_check:
            return(True)
        if n % prime == 0:
            return(False)
    return(True)

def get_primes(n):
    #gets primes less than n, n > 2
    primes = [2]
    test_num = 3
    while True:
        if is_prime(test_num, primes):
            primes.append(test_num)
        test_num += 2
        if test_num >= n:
            return(primes)

def add_primes(n):
    #primes = get_primes(n)
    primes = rwh_primes(n)
    total = 0
    for prime in primes:
        total += prime
    return(total)

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]


print("Problem 10 solution: " + str(add_primes(2000000)))
