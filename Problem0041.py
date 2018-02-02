'''
Project Euler Problem 41:

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import Utilities, itertools

def get_num(p):
    s = ""
    for item in p:
        s += str(item)
    n = int(s)
    return n

def search(n):
    pandigitals = [p for p in itertools.permutations([i for i in range(1, n+1)])]
    pandigitals.sort()
    for i in range(1, len(pandigitals)+1):
        n = get_num(pandigitals[-i])
        if Utilities.isprime(n):
            return n
    return False

def main():
    for i in range(9, 0, -1):
        attempt = search(i)
        if attempt:
            return attempt
    


print("Problem 41 solution: " + str(main()))
