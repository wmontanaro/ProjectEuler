'''
Project Euler Problem 28:

Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
'''

'''
Reasoning: top right will be 1001^2; subtract 1000 to get top left, subtract
1000 to get bottom left, subtract 1000 to get bottom right. That total is
1001^2 + (1001^2 - 1000) + (1001^2 - 2000) + (1001^2 - 3000) =
4*1001^2 - (1001 - 1)*(6)

Repeat for every inner square (subtracting 2 each time - odd squares stopping
at 3), add 1.
'''

def f(n):
    val = (4*(n**2)) - (6*(n-1))
    return val

def main(n):
    total = 0
    for i in range(n, 1, -2):
        total += f(i)
    total += 1
    return total

print("Problem 28 solution: " + str(main(1001)))
