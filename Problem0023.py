'''
Project Euler Problem 23:

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
'''

import Utilities

def proper_divisors(n):
    primes = Utilities.primefactors(n)
    divs = set()
    divs.add(1)
    while len(primes) > 0:
        cur = primes.pop()
        new = set()
        for item in divs:
            new.add(item*cur)
        divs = divs.union(new)
    divs.remove(n)
    return divs

def get_abundants():
    abundants = []
    for i in range(1, 28123): #upper bound from problem statement
        divs = proper_divisors(i)
        if i < sum(divs):
            abundants.append(i)
    return abundants

def get_sums(abundants):
    #sums of two abundant numbers
    sums = set()
    for i in abundants:
        for j in abundants:
            cur_sum = i+j
            if cur_sum < 28123:
                sums.add(cur_sum)
    return sums

def get_missing_sum():
    abundants = get_abundants()
    sums = get_sums(abundants)
    missing_sum = 0
    for i in range(1, 28123): #upper bound from problem statement
        if i not in sums:
            missing_sum += i
    return missing_sum
        

print("Problem 23 solution: " + str(get_missing_sum()))
