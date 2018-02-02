'''
Project Euler Problem 26:

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
'''

def main(n):
    #n is the maximum demonimator
    #10^n mod p = 1 implies p has a cycle of n digits (for prime p)
    #by Fermat's Little Theorem. In addition, a prime p can have a cycle of
    #length up to p-1. We start at the top, and when we find a denominator
    #with longer period than the index, we can break.
    longest_cycle = 0
    winner = None
    for i in range(n-1, 0, -1):
        remainders = []
        val = 1
        rem = 1
        while rem not in remainders and rem != 0:
            remainders.append(rem)
            val = rem*10
            rem = val % i
        if len(remainders) > longest_cycle:
            #print(str(i), str(remainders))
            longest_cycle = len(remainders)
            winner = i
        if longest_cycle - 1 >= i:
            break
    return winner
            

print("Problem 26 solution: " + str(main(1000)))
