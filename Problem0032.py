'''
Project Euler Problem 32:

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

import itertools

def get_perms(options):
    perms = [item for item in itertools.permutations(options)]
    return perms

def array_to_int(arr):
    #join an array of integers (e.g. [1,2,3]) to a big integer (123)
    l = [str(item) for item in arr]
    s = "".join(l)
    n = int(s)
    return n

def main(n):
    #n is the number of digits we are considering, assuming <= 9
    perms = get_perms([i for i in range(1, n+1)])
    winners = set()
    top_end = int(2*n/3)
    for perm in perms:
        for i in range(1, top_end-1):
            for j in range(i+1, top_end):
                multiplicand = array_to_int(perm[:i])
                multiplier = array_to_int(perm[i:j])
                product = array_to_int(perm[j:])
                if multiplicand * multiplier == product:
                    #print(str(multiplicand) + "*" + \
                    #      str(multiplier) + "=" + str(product))
                    winners.add(product)
    #print(winners)
    return sum(winners)
    
print("Problem 32 solution: " + str(main(9)))
