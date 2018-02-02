'''
Project Euler Problem 14:

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

##def chain_length(n):
##    length = 1
##    while n != 1:
##        if n % 2 == 0:
##            n = int(n/2)
##        else:
##            n = (3*n) + 1
##        length += 1
##    return length
##
##def longest_chain(n):
##    max_length = 0
##    winning_num = 0
##    for i in range(1, n+1):
##        length = chain_length(i)
##        if length > max_length:
##            max_length = length
##            winning_num = i
##    return winning_num

def dict_chain(n):
    lengths = {1 : 1}
    for i in range(1, n):
        if i in lengths:
            continue
        test_num = i
        new_nums = dict()
        while test_num not in lengths:
            new_nums[test_num] = 0
            for num in new_nums:
                new_nums[num] += 1
            if test_num % 2 == 0:
                test_num = int(test_num/2)
            else:
                test_num = (3*test_num) + 1
        for num in new_nums:
            lengths[num] = new_nums[num] + lengths[test_num]
    #return lengths
    winning_num = 0
    max_length = 0
    for num in lengths:
        if lengths[num] > max_length:
            max_length = lengths[num]
            winning_num = num
    return max_length      

print("Problem 14 solution: " + str(dict_chain(1000000)))
