'''
Project Euler Problem 51:

By replacing the 1st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.
'''

import itertools, Utilities

def get_inds(s, char):
    #given a string s, find all indices of the character char
    inds = []
    curind = 0
    while True:
        newind = s.find(char, curind)
        if newind == -1:
            return inds
        inds.append(newind)
        curind = newind+1

def get_matches(s, char):
    #given a string s, find all combinations of matches of the character char
    inds = get_inds(s, char)
    matches = []
    for i in range(1, len(inds)+1):
        matches += [c for c in itertools.combinations(inds, i)]
    return matches

def replace_inds(s, inds, newchar):
    #given a string s, a list of indices to replace inds, and a replacement
    #character newchar, return the string that is a copy of s except with
    #the characters in those indices replaced by newchar
    l = list(s)
    for index in inds:
        l[index] = str(newchar)
    t = "".join(l)
    return t

def get_wins(s, match, primes):
    #given a string s and a list of character matches match, return the
    #number of wins (prime value family) for them
    wins = 0
    for i in range(10):
        news = replace_inds(s, match, i)
        if news[0] != "0":
            #if int(replace_inds(s, match, i)) in primes:
            if int(news) in primes:
                wins += 1
    return wins
    
def test_prime(p, primes):
    #given a prime p, determine what number prime value family it is
    s = str(p)
    chars = set(s)
    maxwins = 0
    winmatch = None
    for char in chars:
        inds = get_inds(s, char)
        for ind in inds:
            matches = get_matches(s, char)
            for match in matches:
                curwins = get_wins(s, match, primes)
                if curwins > maxwins:
                    maxwins = curwins
                    winmatch = match
    return(maxwins, winmatch)

def main(n):
    #n is the number prime family we are looking for
    tenpow = 2 #start with 100
    checked = 0
    while True:
        primes = Utilities.primesbelow(10 ** tenpow)
        newprimes = primes[checked:]
        pset = set(newprimes)
        for prime in newprimes:
            wins = test_prime(prime, pset)
            if wins[0] == n:
                #print(wins)
                return prime
        tenpow += 1
        checked += len(newprimes)


print("Problem 51 solution: " + str(main(8)))
