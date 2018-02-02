'''
Project Euler Problem 53:

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5_C_3 = 10.

In general,

n_C_r =	n! / r!(n−r)!,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23_C_10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
greater than one-million?
'''

import math

def main():
    f = {i : math.factorial(i) for i in range(101)}
##    f = {0:1, 1:1}
##    for i in range(2,101):
##        f[i] = i*f[i-1]
    wins = 0
    for i in range(23,101):
        for j in range(1, i+1):
            iCj = f[i] / (f[j] * f[i-j])
            if iCj > 1000000:
                wins += 1
    return wins

print("Problem 53 solution: " + str(main()))
