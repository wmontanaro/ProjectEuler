'''
Project Euler Problem 56:

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
'''

def sum_digits(n):
    s = str(n)
    total = 0
    for char in s:
        total += int(char)
    return total

def brute(a, b):
    #a and b are the maximum base and power we consider
    winners = [0, 0]
    winning_sum = 0
    #could look top down, and stop once numdigits < winning_sum?
    for base in range(1, a):
        for exponent in range(1, b):
            cur_num = base**exponent
            cur_sum = sum_digits(cur_num)
            if cur_sum > winning_sum:
                winning_sum = cur_sum
                winners = [base, exponent]
    #print(winners)
    return winning_sum
    

print("Problem 56 solution: " + str(brute(100, 100)))
