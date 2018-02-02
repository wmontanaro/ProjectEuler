'''
Project Euler Problem 24:

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
'''

import itertools

def get_nth_perm_of_l(n, l):
    #n is the number permutation, l is the list to permute
    perms = itertools.permutations(l)
    array = [item for item in perms]
    array.sort()
    perm = array[n+1]
    s = ""
    for item in perm:
        s += str(item)
    return s


print("Problem 24 solution: " + \
      get_nth_perm_of_l(1000000, [0,1,2,3,4,5,6,7,8,9,]))
