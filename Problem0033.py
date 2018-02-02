'''
Project Euler Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

def get_options():
    opts = []
    for i in range(10,99):
        for j in range(i+1,100):
            opts.append([i,j])
    return opts

def remove_trivials(opts):
    to_remove = []
    for item in opts:
        if item[0] % 10 == 0 or item[1] % 10 == 0:
            to_remove.append(item)
    for item in to_remove:
        opts.remove(item)
    return opts

##def remove_uncancellable(opts):
##    to_remove = []
##    for item in opts:
##        numer_dig = set([int(item[0]/10), item[0] % 10])
##        denom_dig = set([int(item[1]/10), item[1] % 10])
##        if len(numer_dig.intersection(denom_dig)) == 0:
##            to_remove.append(item)
##    for item in to_remove:
##        opts.remove(item)
##    return opts

def check_fake(opt):
    numer = opt[0]
    denom = opt[1]
    numer_digits = [int(numer/10), numer % 10]
    denom_digits = [int(denom/10), denom % 10]
    numer_set = set(numer_digits)
    denom_set = set(denom_digits)
    common = numer_set.intersection(denom_set)
    if len(common) == 0:
        return False
    true_value = numer/denom
    fake_factor = common.pop()
    numer_digits.remove(fake_factor)
    denom_digits.remove(fake_factor)
    fake_value = numer_digits[0]/denom_digits[0]
    if true_value == fake_value:
        return True
    return False

import fractions

def main():
    opts = get_options()
    opts = remove_trivials(opts)
    winners = []
    for opt in opts:
        if check_fake(opt):
            winners.append(opt)
    prod_numer = 1
    prod_denom = 1
    for item in winners:
        prod_numer *= item[0]
        prod_denom *= item[1]
    f = fractions.Fraction(prod_numer, prod_denom)
    return f.denominator
    

print("Problem 33 solution: " + str(main()))
