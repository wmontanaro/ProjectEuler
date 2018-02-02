'''
Project Euler Problem 38:

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import itertools

##def is_concat_prod(num):
##    quotients = []
##    for i in range(1, 10):
##        if num % i != 0:
##            break
##        quotients.append(int(num/i))
##    for quotient in quotients:
##        pass

letters = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

def is_pcp(num):
    global letters
    prod_s = ""
    for i in range(1, 10):
        cur_s = str(num*i)
        if len(cur_s) + len(prod_s) <= 9:
            prod_s += cur_s
        else:
            break
    if len(prod_s) != 9:
        return False
    for char in letters:
        if char not in prod_s:
            return False
    return prod_s
    

def main():
    #we assume all 9 digits
    #candidates = [item for item in itertools.permutations([9,8,7,6,5,4,3,2,1])]
    #to find the max we have to check, we note that if we have two items,
    #then they must be four and five digits long (1*n concatenated with 2*n).
    #Hence we can stop after 5 digit numbers.
    winners = []
    for i in range(1, 100000):
        result = is_pcp(i)
        if result != False:
            winners.append([result, i])
            #print(str(i))
    #print(winners)
    winners.sort()
    return winners[-1][0]

print("Problem 38 solution: " + main())
