'''
Project Euler Problem 40:

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''

def main():
    s = ""
    counter = 0
    #while len(s) < 100:
    while len(s) < 1000000:
        counter += 1
        s += str(counter)
    prod = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999])
    prod *= int(s[99999]) * int(s[999999])
    #print(prod)
    #return s
    return prod

print("Problem 40 solution: " + str(main()))
