'''
Project Euler Problem 16:

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

def sum_digits(n):
    s = str(n)
    total = 0
    for char in s:
        total += int(char)
    return total

print("Problem 16 solution: " + str(sum_digits(2**1000)))
