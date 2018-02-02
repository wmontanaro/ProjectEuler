'''
Project Euler Problem 48:

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def main(n):
    total = 0
    for i in range(1, n+1):
        total += i**i
    s = str(total)
    return int(s[-10:])

print("Problem 48 solution: " + str(main(1000)))
