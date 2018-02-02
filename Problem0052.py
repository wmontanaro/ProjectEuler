'''
Project Euler Problem 52:

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

import itertools

def get_perms(n):
    #return the integers formed from permutations of the digits in n
    permints = set([int("".join([str(i) for i in p])) \
                for p in itertools.permutations(str(n))])
    return permints

def brute():
    digits = 1
    while True:
        lowerbound = 1*(10**(digits-1))
        upperbound = int(1*(10**digits)/6)
        #print(lowerbound)
        for num in range(lowerbound, upperbound): 
            mults = [list(str(num*j)) for j in range(2, 7)]
##            perms = get_perms(num)
##            winning = True
##            for item in mults:
##                if item not in perms:
##                    winning = False
##                    break
##            if winning:
##                return num
            chars = list(str(num))
            try:
                for mult in mults:
                    for char in chars:
                        mult.remove(char)
                return num
            except ValueError:
                pass
        digits += 1

print("Problem 52 solution: " + str(brute()))
