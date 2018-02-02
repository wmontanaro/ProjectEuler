'''
Project Euler Problem 34:

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

def check_num(num):
    s = str(num)
    chars = [l for l in s]
    fact_sum = 0
    for char in chars:
        fact_sum += math.factorial(int(char))
    if fact_sum == num:
        return True
    return False

def main():
    #note that our maximum is set to 3000000 because 8*9! < 3000000, and that
    #difference will only increase as the number of digits increases. This
    #bound could be lowered with more careful analysis.
    winners = []
    for i in range(10, 3000000):
        if check_num(i):
            winners.append(i)
    #print(winners)
    return sum(winners)

print("Problem 34 solution: " + str(main()))
