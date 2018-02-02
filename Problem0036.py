'''
Project Euler Problem 36:

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''

def is_palindrome(n):
    s = str(n)
    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            return False
    return True

def main(n):
    #n is the cap of numbers we consider
    winners = []
    for i in range(1, n):
        if is_palindrome(i) and is_palindrome("{0:b}".format(i)):
            winners.append(i)
    #print(winners)
    return sum(winners)

print("Problem 36 solution: " + str(main(1000000)))
