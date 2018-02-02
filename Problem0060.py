'''
Project Euler Problem 60:

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''

import Utilities, itertools

#the below function is too slow for 1000 primes and combos of size 5
##def get_primesums(primes, n):
##    primesums = dict()
##    combinations = [item for item in itertools.combinations(primes, n)]
##    for c in combinations:
##        total = sum(c)
##        if total in primesums:
##            primesums[total].append(c)
##        else:
##            primesums[total] = [c]
##    return primesums

##def testconcat(known, new):
##    #known is a set of primes which are concatenable to get another prime
##    #new is the prime to be tested
##    snew = str(new)
##    for prime in known:
##        sprime = str(prime)
##        testprime1 = sprime + snew
##        if not Utilities.isprime(int(testprime1)):
##            return False
##        testprime2 = snew + sprime
##        if not Utilities.isprime(int(testprime2)):
##            return False
##    return True
##
##def brute():
##    primes = Utilities.primesbelow(3500) #10000 as first upper bound
##    winners = []
##    for i in range(len(primes)-4):
##        p1 = primes[i]
##        for j in range(i+1, len(primes)-3):
##            p2 = primes[j]
##            if testconcat([p1], p2):
##                testset = [p1, p2]
##                for k in range(j+1, len(primes)-2):
##                    p3 = primes[k]
##                    if testconcat(testset, p3):
##                        testset.append(p3)
##                        for l in range(k+1, len(primes)-1):
##                            p4 = primes[l]
##                            if testconcat(testset, p4):
##                                testset.append(p4)
##                                for m in range(l+1, len(primes)):
##                                    p5 = primes[m]
##                                    if testconcat(testset, p5):
##                                        testset.append(p5)
##                                        winners.append(testset)
##    return winners
##
##def build():
##    primes = Utilities.primesbelow(10000)
##    maybes = [[p] for p in primes]
##
##def get_pairs(n):
##    primes = Utilities.primesbelow(n)
##    pairs = []
##    for i in range(len(primes)-1):
##        for j in range(i+1, len(primes)):
##            if testconcat(set([primes[i]]), primes[j]):
##                pairs.append(set([primes[i], primes[j]]))
##    return pairs
##
##def get_triples(n, pairs):
##    primes = Utilities.primesbelow(n)
##    triples = []
##    for prime in primes:
##        for pair in pairs:
##            if prime not in pair:
##                if testconcat(pair, prime):
##                    newset = pair.add(prime)
##                    triples.append(newset)
##    return triples
##
##def faster_concat_test(primes, newprime, primeset):
##    sprime = str(newprime)
##    for prime in primes:
##        testprime = int(str(prime)+sprime)
##        if testprime not in primeset:
##            return False
##        testprime = int(sprime+str(prime))
##        if testprime not in primeset:
##            return False
##    return True
##
##import math

##def faster_attempt(n):
##    primes = Utilities.primesbelow(n)
##    primeset = Utilities.primesbelow(10**(1+int(math.log(n, 10))))
##    pairs = set()
##    for i in range(len(primes)-1):
##        for j in range(i+1, len(primes)):
##            if faster_concat_test([primes[i]], primes[j], primeset):
##                newset = [primes[i], primes[j]]
##                pairs.add(newset)
##    print("found " + str(len(pairs)) + " pairs")
##    triples = set()
##    for prime in primes:
##        for pair in pairs:
##            if prime not in pair:
##                if faster_concat_test(pair, prime, primeset):
##                    triples.add(pair.add(prime))
##    print("found " + str(len(triples)) + " triples")
##    quads = set()
##    for prime in primes:
##        for triple in triples:
##            if prime not in triple:
##                if faster_concat_test(triple, prime, primeset):
##                    quads.add(triple.add(prime))
##    print("found " + str(len(quads)) + " quads")
##    quints = set()
##    for prime in primes:
##        for quad in quads:
##            if prime not in quad:
##                if faster_concat_test(quad, prime, primeset):
##                    quints.add(triple.add(prime))
##                    print("winner! " + str(triple.add(prime)))
##    print("found " + str(len(quints)) + " quints")
##    return quints

##def faster(n):
##    primes = Utilities.primesbelow(n)
##    primeset = Utilities.primesbelow(10**(2*(1+int(math.log(n, 10)))))
##    pairs = []
##    triples = []
##    for i in range(len(primes)-2):
##        print("checking " + str(primes[i]))
##        for j in range(i+1, len(primes)-1):
##            if faster_concat_test([primes[i]], primes[j], primeset):
##                pair = [primes[i], primes[j]]
##                pairs.append(pair)
##                for k in range(j+1, len(primes)):
##                    if faster_concat_test(pair, primes[k], primeset):
##                        triple = pair.append(primes[k])
##                        triples.append(triple)
##    print("found " + str(len(pairs)) + " pairs")
##    print("found " + str(len(triples)) + " triples")
##    return(pairs, triples)

##def test_again(oldprime, newprime):
##    if Utilities.isprime(int(str(oldprime) + str(newprime))):
##        if Utilities.isprime(int(str(newprime) + str(oldprime))):
##            return True
##    return False
##
##primes = Utilities.primesbelow(10000)
##
##def find_next(chain):
##    global primes
##    if len(chain) == 5:
##        return chain
##    for p in primes:
##        if p > chain[-1] and all(test_again(oldprime, p) for oldprime in chain):
##            new_chain = find_next(chain + [p])
##            if new_chain:
##                return new_chain
##    return False
##
##def brute_again(n):
##    global primes
##    winners = []
##    while len(primes) > 0:
##        p = [primes.pop(0)]
##        if find_next(p):
##            winners.append(p)
##    return winners

primes = Utilities.primesbelow(10000)
set_size = 5

def make_chain(chain):
    if len(chain) == set_size:
        return chain 
    for p in primes:
        if p > chain[-1] and all_prime(chain+[p]):
            new_chain = make_chain(chain+[p])
            if new_chain:
                return new_chain
    return False  
        
def all_prime(chain):
    return all(Utilities.isprime(int(str(p[0]) + str(p[1]))) \
               for p in itertools.permutations(chain, 2))

def main():
    global primes, set_size
    global chain
    chain = 0
    while not chain:
        chain = make_chain([primes.pop(0)])
    print("Project Euler 60 Solution =", sum(map(int, chain)), chain)        

print("Problem 60 solution: " )
