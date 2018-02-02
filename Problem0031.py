'''
Project Euler Problem 31:

In England the currency is made up of pound, £, and pence, p, and there
are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

import copy

def amount(array):
    total = 0
    for item in array:
        total += item
    return total

def new_round(combos, n, pos):
    over = []
    under = []
    for item in combos:
        for p in pos:
            titem = copy.deepcopy(item)
            titem.append(p)
            if amount(titem) >= n:
                over.append(titem)
            else:
                under.append(titem)
    return(over, under)

def brute(n, pos):
    #n is the number that is the goal
    #pos is the possible denominations
    unchecked = []
    checked = []
    for item in pos:
        titem = [item]
        if amount(titem) >= n:
            checked.append(titem)
        else:
            unchecked.append(titem)
    while (len(unchecked) > 0):
        cur_round = new_round(unchecked, n, pos)
        checked += cur_round[0]
        unchecked = cur_round[1]
    count = 0
    for item in checked:
        if amount(item) == n:
            #print(item)
            count += 1
    return count

def reaching(n, pos):
    d = {i : 0 for i in range(n+1)}
    d[0] = 1
    pos.sort()
    for i in range(len(pos)):
        cur_denom = pos[i]
        for j in range(cur_denom, n+1):
            cur_val = j - cur_denom
            d[j] += d[cur_val]
    #print(d)
    return d[n]
            
print("Problem 31 solution: " + str(reaching(200, [1,2,5,10,20,50,100,200])))
