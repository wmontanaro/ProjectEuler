'''
Project Euler Problem 27:

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0<=n<=39. However, when n = 40, 40^2 + 40 + 41 = 40(40+1)+41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0<=n<=79. The product of the coefficients,
-79 and 1601, is -126479.

Considering quadratics of the form: n^2 + an + b, where |a|<1000 and |b|<=1000
where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |-4| = 4)

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''

import Utilities

def f(a, b, n):
    val = (n**2) + (a*n) + b
    return val

def winner(a, b):
    max_counter = 0
    win_a = None
    win_b = None
    for i in range(-a, a, 1):
        for j in range(-(b+1), b+1, 1):
            counter = 0
            val = f(i, j, counter)
            if val <= 0:
                continue
            while Utilities.isprime(val):
                counter += 1
                val = f(i, j, counter)
                if val <= 0:
                    break
            if counter > max_counter:
                max_counter = counter
                win_a = i
                win_b = j
    return(max_counter, win_a, win_b)

def main(a, b):
    prize = winner(a, b)
    mult = prize[1]*prize[2]
    return mult

print("Problem 27 solution: " +str(main(1000, 1000)))
