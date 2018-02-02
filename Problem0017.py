'''
Project Euler Problem 17:

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
'''

d = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", \
     7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", \
     12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", \
     16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen", \
     20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", \
     60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety", \
     100 : "hundred", 1000 : "thousand"}

def count_1_to_20(n):
    global d
    count = int(len(d[n]))
    return count

def count_21_to_99(n):
    global d
    tens = int(n/10) * 10
    ones = n % 10
    count = int(len(d[tens]))
    if ones != 0:
        count += int(len(d[ones]))
    return count

def count_100_to_999(n):
    global d
    hundreds = int(n/100)
    tens = n % 100
    count = int(len(d[hundreds]))
    count += len("hundred")
    count += len("and")
    if tens in range(21, 100):
        count += count_21_to_99(tens)
    elif tens in range(1, 21):
        count += count_1_to_20(tens)
    return count

def count(n):
    global d
    if n in range(1, 21):
        return count_1_to_20(n)
    elif n in range(21, 100):
        return count_21_to_99(n)
    elif n in range(100, 1000):
        return count_100_to_999(n)
    elif n == 1000:
        return int(len(d[n]))

def add_all(n):
    total = 0
    for i in range(1, n+1):
        total += count(i)
    return total

print("Problem 17 solution: " + str(add_all(1000)))
