'''
Project Euler Problem 21:

Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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

def buddies(n):
    dofn = {1 : 1}
    total = 0
    for i in range(2, n+1):
        divs = proper_divisors(i)
        tot = sum(divs)
        dofn[i] = tot
    while len(dofn) > 0:
        test = dofn.popitem()
        if test[1] in dofn and dofn[test[1]] == test[0]:
                #print(str(test[0]) + " and " + str(test[1]) + " are buddies!")
                total += test[0]
                total += test[1]
                dofn.pop(test[1])
    return total

print("Problem 21 solution: " + str(buddies(10000)))
