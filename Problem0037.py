'''
Project Euler Problem 37:

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import Utilities

def is_truncatable(p, primes):
    s = str(p)
    for i in range(1, len(s)):
        right_test_num = int(s[:i]) #start rightmost digit, add from left
        left_test_num = int(s[-i:]) #start leftmost digit, add from right
        if left_test_num not in primes or right_test_num not in primes:
            return False
    return True

def main(n):
    #we know there are 11 solutions by the problem statement
    winners = []
    primes = Utilities.primesbelow(n)
    primeset = set(primes)
    for prime in primes:
        if is_truncatable(prime, primeset):
            winners.append(prime)
            if len(winners) == 15:
                break
    winners.remove(2)
    winners.remove(3)
    winners.remove(5)
    winners.remove(7)
    #print(winners)
    return sum(winners)

print("Problem 37 solution: " + str(main(1000000)))
