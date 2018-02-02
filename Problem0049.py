'''
Project Euler Problem 49:

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''

import Utilities

def trimprimes(primes):
    for i in range(len(primes)):
        s = str(primes[i])
        if len(s) == 4:
            index = i
            break
    return primes[index:]

def isperm(seq):
    strings = [str(s) for s in seq]
    for word in strings:
        for char in word:
            for t in strings:
                if char not in t:
                    return False
    return True

def brute():
    #strategy: get four digit primes, find sets of arithmetic sequences,
    #determine if they are a permutation of the same four digits
    primes = Utilities.primesbelow(10000)
    primes = trimprimes(primes)
    seqs = []
    for i in range(len(primes)):
        for j in range(i+1, len(primes)-1):
            diff = primes[j] - primes[i]
            if primes[j] + diff in primes:
                seqs.append([primes[i], primes[j], primes[j]+diff])
    wins = []
    for seq in seqs:
        if isperm(seq):
            wins.append(seq)
    wins.remove([1487, 4817, 8147])
    s = ""
    for num in wins[0]:
        s += str(num)
    return int(s)

print("Problem 49 solution: " + str(brute()))
