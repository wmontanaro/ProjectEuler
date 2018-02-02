'''
Project Euler Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def smallest_prime_divisor(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n

def prime_divisors(n):
    divisor = None
    divisors = set()
    number = n
    while divisor != number:
        divisor = smallest_prime_divisor(number)
        divisors.add(divisor)
        number = int(number / divisor)
    return divisors
    
print("Problem 3 solution: " + str(max(prime_divisors(600851475143))))
