'''
Project Euler Problem 46:

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
'''

import Utilities

def squaresbelow(n):
    squares = [1]
    counter = 1
    while squares[-1] < n:
        counter += 1
        squares.append(counter ** 2)
    return squares

def inc_counter(counter):
    new_counter = counter + 2
    while Utilities.isprime(new_counter):
        new_counter += 2
    return new_counter

def brute():
    #strategy: find next odd composite, use primes and squares smaller than
    #that composite to check until we find a winner
    counter = 9
    squares = [1,4]
##    winner = False
##    while not winner:
##        primes = Utilities.primesbelow(counter)
##        squares = squaresbelow(counter)
##        for p in primes:
##            for s in squares:
##                if (p+(2*s)) == counter:
##                    counter += 2
##                    while Utilities.isprime(counter):
##                        counter += 2
##                    print("counter is " + str(counter))
##                    break
    satisfied = True
    while satisfied:
        satisfied = False
        primes = Utilities.primesbelow(counter)
        squares = squaresbelow(counter)
        for p in primes:
            for s in squares:
                if (p+(2*s)) == counter:
                    satisfied = True
                    counter = inc_counter(counter)
    return counter


print("Problem 46 solution: " + str(brute()))
