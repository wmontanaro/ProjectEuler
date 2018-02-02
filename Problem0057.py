'''
Project Euler Problem 57:

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
'''

import fractions

def generate_fracs(n):
    #list of fractional parts of expansion
    f = [0 for i in range(n)]
    f[0] = fractions.Fraction(1,2)
    for i in range(1, n):
        f[i] = fractions.Fraction(1,2+f[i-1])
    return f

def is_winner(frac):
    #we expect frac to be a fractions.Fraction
    strnum = str(frac.numerator)
    strden = str(frac.denominator)
    if len(strnum) > len(strden):
        return True
    return False

def brute(n):
    #n is the number of iterations we consider
    winners = 0
    fracs = generate_fracs(n)
    for i in range(1, n+1):
        cur_num = 1 + fracs[i-1]
        if is_winner(cur_num):
            #print(cur_num)
            winners += 1
    return winners

print("Problem 57 solution: " + str(brute(1000)))
