'''
Project Euler Problem 43:

The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we
note the following:

d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools

def get_num(p):
    s = ""
    for item in p:
        s += str(item)
    n = int(s)
    return n

def main():
    perms = [item for item in itertools.permutations([i for i in range(10)])]
    winners = []
    for p in perms:  
        p17 = get_num(p[7:])
        if p17 % 17 != 0:
            continue
        p13 = get_num(p[6:9])
        if p13 % 13 != 0:
            continue
        p11 = get_num(p[5:8])
        if p11 % 11 != 0:
            continue
        p7 = get_num(p[4:7])
        if p7 % 7 != 0:
            continue
        p5 = get_num(p[3:6])
        if p5 % 5 != 0:
            continue
        p3 = get_num(p[2:5])
        if p3 % 3 != 0:
            continue
        p2 = get_num(p[1:4])
        if p2 % 2 != 0:
            continue
        winners.append(p)
    #print(winners)
    return sum([get_num(item) for item in winners])
        
print("Problem 43 solution: " + str(main()))
