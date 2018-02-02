'''
Project Euler Problem 58:

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
'''

'''
analysis: bottom right diag is odd prime squares. note that this means they
will never be prime. it also means we can figure out the other corners, right?
nth odd val. bottom right is n^2. bottom left is n^2 - (n-1). top left is
n^2 - 2(n-1). top right is n^2 - 3(n-1).
'''

#note that n=1 is a trivial solution. we proceed assuming they do not want
#that answer.

import Utilities

def get_results(n):
    cur_num = n**2 #bottom left
    wins = 0
    losses = 1
    for i in range(3):
        cur_num -= (n-1)
        #print(cur_num)
        if Utilities.isprime(cur_num):
            wins += 1
        else:
            losses += 1
    return(wins, losses)
    

def main(ratio):
    #ratio is the (decimal form of the) percentage at which we stop; to avoid
    #the trivial solution(n=1 has ratio 0), we start with n=3.
    n = 3
    wins = 3
    losses = 2
    while wins/(wins+losses) > ratio:
        n += 2 #next odd integer
        results = get_results(n)
        wins += results[0]
        losses += results[1]
    return n

    
    

print("Problem 58 solution: " + str(main(0.1)))
