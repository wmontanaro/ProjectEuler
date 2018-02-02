'''
Project Euler Problem 30:

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
'''

def power_sum(num, power):
    s = str(num)
    total = 0
    for char in s:
        total += int(char)**power
    return total

def get_max(power):
    counter = 100
    total = 9**power
    while counter < total:
        counter *= 10
        total += 9**power
    return total

def brute(power):
    maximum = get_max(power)
    winners = []
    for i in range(2, maximum):
        cur_sum = power_sum(i, power)
        if cur_sum == i:
            winners.append(i)
    return winners

print("Problem 30 solution: " + str(sum(brute(5))))
