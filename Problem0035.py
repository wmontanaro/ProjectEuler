'''
Project Euler Problem 35:

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import Utilities, collections

def check_prime(p, primes):
    s = str(p)
    g = collections.deque(s)
    for i in range(len(g)):
        test_num = int("".join(list(g)))
        if test_num not in primes:
            return False
        g.rotate(1)
    return True

def main(n):
    #n is the maximum number we are looking at
    primes = Utilities.primesbelow(n)
    primeset = set(primes)
    winners = []
    for prime in primes:
        if check_prime(prime, primeset):
            winners.append(prime)
            #print(prime)
    return len(winners)

print("Problem 35 solution: " + str(main(1000000)))
