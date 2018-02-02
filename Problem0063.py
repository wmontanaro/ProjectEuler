'''
Project Euler Problem 63:

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

def check(n):
    powers = []
    num_digits = 0
    i = 0
    while num_digits < n:
        i += 1
        num_digits = len(str(i**n))
    while num_digits == n:
        power = i**n
        powers.append(power)
        i += 1
        num_digits = len(str(i**n))
    #print(powers)
    return len(powers)

def main():
    wins = 0
    for i in range(1, 10):
        wins += check(i)
    return wins

print("Problem 63 solution: " + str(main()))
