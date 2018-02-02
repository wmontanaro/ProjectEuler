'''
Project Euler Problem 50:

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
'''

import Utilities, copy

##def primechain(prime, primes):
##    #primes is the list of primes smaller than prime
##    longest = []
##    idx = 0 #start looking for a chain here
##    while idx < len(primes):
##        tidx = idx
##        chain = []
##        total = 0
##        #print("testing starting with " + str(primes[idx]))
##        while total < prime and tidx < len(primes):
##            total += primes[tidx]
##            #print("new total " + str(total))
##            chain.append(primes[tidx])
##            tidx += 1
##        if total == prime:
##            #print("new chain " + str(chain))
##            if len(chain) > len(longest):
##                longest = copy.deepcopy(chain)
##        idx += 1
##    return longest
##
##def get_max(prime, primes, length):
##    #primes is the list of primes smaller than prime
##    #length is the length of the longest found chain
##    backtotal = 0
##    counter = -1
##    while backtotal < prime:
##        try:
##            backtotal += primes[counter]
##            counter -= 1
##        except IndexError:
##            return 1
##    return len(primes)-counter+1
##
##def brute(n):
##    primes = Utilities.primesbelow(n)
##    longest_chain = []
##    for i in range(len(primes)):
##        prime = primes[i]
##        max_idx = get_max(prime, primes[:i], len(longest_chain))
##        chain = primechain(prime, primes[:max_idx])
##        if len(chain) > len(longest_chain):
##            print(str(prime))
##            longest_chain = copy.deepcopy(chain)
##    return sum(longest_chain)

##def build(n):
##    #find consecutive sums, repeating when a longer prime chain is found
##    #start with length 22 (from problem statement)
##    #note we assume that there are at least 22 primes below n
##    primes = Utilities.primesbelow(n)
##    longest_chain = [i for i in range(22)] #dummy, doesn't matter
##    counter = 22
##    plen = len(primes)
##    while counter < plen-len(longest_chain):
##        chain = []
##        for idx in range(plen-counter-1-len(longest_chain)):
##            tsum = sum(primes[idx:idx+counter])
##            if tsum >= n:
##                break
##            if tsum in primes:
##                longest_chain = primes[idx:idx+counter]
##                break
##        counter += 1
##    return sum(longest_chain)
##

def ptest(p, primes, sprimes):
    #we add terms to p, getting the longest chain starting with p resulting in
    #a prime sum; we assume primes is the list of primes greater than p
    total = p
    winner = p
    maxp = primes[-1]
    counter = 1
    wincounter = 1
    for prime in primes:
        total += prime
        counter += 1
        if total > maxp:
            return(winner, wincounter)
        if total in sprimes:
            winner = total
            wincounter = counter
    return(winner, wincounter)
            
def main(n):
    primes = Utilities.primesbelow(n)
    sprimes = set(primes)
    cprimes = copy.deepcopy(primes)
    winner = (0, 0)
    winstart = 0
    while len(primes) >= winner[1]:
        p = primes.pop(0)
        curlen = ptest(p, primes, sprimes)
        if curlen[1] > winner[1]:
            winner = curlen
            #winstart = p
    #print(winstart)
    return winner

print("Problem 50 solution: " + str(main(1000000)[0]))
