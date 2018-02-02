'''
Project Euler Problem 5:

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
'''

def check(n, test_num):
    for i in range(1, n+1):
        if test_num % i != 0:
            return False
    return True
        
#naive_divide works, but is too slow
def naive_divide(n):
    test_num = 0
    while True:
        test_num += 1
        if check(n, test_num):
            return(test_num)

def top_down_check(n, test_num):
    for i in range(n, 1, -1):
        if test_num % i != 0:
            return False
    return True

#top_down_divide is faster than naive_divide, but still too slow
def top_down_divide(n):
    test_num = 0
    while True:
        test_num += 1
        if top_down_check(n, test_num):
            return(test_num)
    

def check_factors(n, factors):
    test_num = n
    for factor in factors:
        if test_num % factor == 0:
            test_num = int(test_num / factor)
    return(test_num)

def factor_divide(n):
    factors = [1]
    for i in range(1, n+1):
        factors.append(check_factors(i, factors))
    product = 1
    for factor in factors:
        product *= factor
    return(product)

print("Problem 5 solution: " + str(factor_divide(20)))
