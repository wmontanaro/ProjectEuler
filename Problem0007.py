'''
Project Euler Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
'''

def is_prime(n, primes):
    #primes is the list of primes smaller than n
    for prime in primes:
        if n % prime == 0:
            return(False)
    return(True)

def get_primes(n):
    #we assume n > 2
    primes = [2]
    test_num = 3
    while len(primes) < n:
        if is_prime(test_num, primes):
            primes.append(test_num)
        test_num += 2
    return(primes)

def get_prime(n):
    primes = get_primes(n)
    return(primes[-1])



print("Problem 7 solution: " + str(get_prime(10001)))
