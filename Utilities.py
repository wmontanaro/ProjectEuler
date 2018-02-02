##def primes(n):
##    """
##        list of primes not exceeding n in ascending
##        order; assumes n is an integer greater than
##        1; uses Sieve of Eratosthenes
##    """
##    m = (n-1) // 2
##    b = [True] * m
##    i, p, ps = 0, 3, [2]
##    while p*p < n:
##        if b[i]:
##            ps.append(p)
##            j = 2*i*i + 6*i + 3
##            while j < m:
##                b[j] = False
##                j = j + 2*i + 3
##        i += 1; p += 2
##    while i < m:
##        if b[i]:
##            ps.append(p)
##        i += 1; p += 2
##    return ps
##
##def is_prime(n):
##    """
##        False if n is provably composite, else
##        True if n is probably prime; assumes n
##        is an integer greater than 1; uses
##        Miller-Rabin test on prime bases < 100
##    """
##    ps = [2,3,5,7,11,13,17,19,23,29,31,37,41,
##         43,47,53,59,61,67,71,73,79,83,89,97]
##    def is_spsp(n, a):
##        d, s = n-1, 0
##        while d%2 == 0:
##            d /= 2; s += 1
##        if pow(a,d,n) == 1:
##            return True
##        for r in xrange(s):
##            if pow(a, d*pow(2,r), n) == n-1:
##                return True
##        return False
##    if n in ps: return True
##    for p in ps:
##        if not is_spsp(n,p):
##            return False
##    return True
##
##def factors(n):
##    """
##        list of prime factors of n in ascending
##        order; assumes n is an integer, may be
##        positive, zero or negative; uses Pollard's
##        rho algorithm with Floyd's cycle finder
##    """
##    def gcd(a,b):
##        while b: a, b = b, a%b
##        return abs(a)
##    def facts(n,c,fs):
##        f = lambda(x): (x*x+c) % n
##        if is_prime(n): return fs+[n]
##        t, h, d = 2, 2, 1
##        while d == 1:
##            t = f(t); h = f(f(h))
##            d = gcd(t-h, n)
##        if d == n:
##            return facts(n, c+1, fs)
##        if is_prime(d):
##            return facts(n//d, c+1, fs+[d])
##        return facts(n, c+1, fs)
##    if -1 <= n <= 1: return [n]
##    if n < -1: return [-1] + factors(-n)
##    fs = []
##    while n%2 == 0:
##        n = n//2; fs = fs+[2]
##    if n == 1: return fs
##    return sorted(facts(n,1,fs))

##def primefactors(n, sort=False):
##    factors = []
##
##    limit = int(n ** .5) + 1
##    for checker in smallprimes:
##        print(smallprimes[-1])
##        if checker > limit: break
##        while n % checker == 0:
##            factors.append(checker)
##            n //= checker
##
##
##    if n < 2: return factors
##    else : 
##        factors.extend(bigfactors(n,sort))
##        return factors
##
##def bigfactors(n, sort = False):
##    factors = []
##    while n > 1:
##        if isprime(n):
##            factors.append(n)
##            break
##        factor = pollard_brent(n) 
##        factors.extend(bigfactors(factor,sort)) # recurse to factor the not necessarily prime factor returned by pollard-brent
##        n //= factor
##
##    if sort: factors.sort()    
##    return factors

import random

def primesbelow(N):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    #""" Input N>=6, Returns a list of primes, 2 <= p < N """
    correction = N % 6 > 1
    N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
    sieve = [True] * (N // 3)
    sieve[0] = False
    for i in range(int(N ** .5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

smallprimeset = set(primesbelow(100000))
_smallprimeset = 100000
def isprime(n, precision=7):
    # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
    if n < 1:
        raise ValueError("Out of bounds, first argument must be > 0")
    elif n <= 3:
        return n >= 2
    elif n % 2 == 0:
        return False
    elif n < _smallprimeset:
        return n in smallprimeset


    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for repeat in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1: continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == 1: return False
            if x == n - 1: break
        else: return False

    return True

# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent(n):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3

    y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g==1:
            ys = y
            for i in range(min(m, r-k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x-y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return g

smallprimes = primesbelow(1000) # might seem low, but 1000*1000 = 1000000, so this will fully factor every composite < 1000000
def primefactors(n, sort=False):
    factors = []

    for checker in smallprimes:
        while n % checker == 0:
            factors.append(checker)
            n //= checker
        if checker > n: break

    if n < 2: return factors

    while n > 1:
        if isprime(n):
            factors.append(n)
            break
        factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
        factors.extend(primefactors(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort: factors.sort()

    return factors

def factorization(n):
    factors = {}
    for p1 in primefactors(n):
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors

totients = {}
def totient(n):
    if n == 0: return 1

    try: return totients[n]
    except KeyError: pass

    tot = 1
    for p, exp in factorization(n).items():
        tot *= (p - 1)  *  p ** (exp - 1)

    totients[n] = tot
    return tot

def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return abs((a // gcd(a, b)) * b)
