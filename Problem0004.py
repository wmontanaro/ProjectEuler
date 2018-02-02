'''
Project Euler Problem 4:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(number):
    numlist = list(str(number))
    for i in range(int(len(numlist)/2)):
        if numlist[i] != numlist[-(i + 1)]:
            return False
    return True

def find_biggest_palindrome(digits):
    highest_num = int("".join(["9" for i in range(digits)]))
    palindrome = 0
    for i in range(1, highest_num + 1):
        for j in range(1, highest_num + 1):
            if is_palindrome(i * j):
                #print("i: " + str(i) + ", j:" + str(j) + ", i*j: " + str(i*j))
                if i * j > palindrome:
                    palindrome = i * j
    return palindrome
        
    
    
print("Problem 4 solution: " + str(find_biggest_palindrome(3)))
