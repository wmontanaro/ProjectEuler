'''
Project Euler Problem 62:

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
'''

##import itertools
##
##def get_permutations(num):
##    s = str(num)
##    l = [char for char in s]
##    v = [p for p in itertools.permutations(l)]
##    n = set([int("".join(i)) for i in v if i[0] != "0"])
##    return n
##
##def naive(n):
##    #n is the number of permutations which are cubes
##    cubes = [i**3 for i in range(1, 1300)]
##    scubes = set(cubes)
##    checked = set()
##    for cube in cubes[1200:]:
##        if cube not in checked:
##            perms = get_permutations(cube)
##            inters = scubes.intersection(perms)
##            if len(inters) == n:
##                return cube
##            checked = checked.union(inters)
##            for item in inters:
##                scubes.remove(item)

def main(n):
    #n is the number of permutations which are cubes
    cubes = dict()
    min_cube = float('inf')
    i = 1
    while min_cube == float('inf'):
        cube = i**3
        diglist = list(str(cube))
        diglist.sort()
        digmin = "".join(diglist)
        if digmin in cubes:
            cubes[digmin].append(cube)
        else:
            cubes[digmin] = [cube]
        if len(cubes[digmin]) == n:
            return cubes[digmin]
        i += 1
            
print("Problem 62 solution: " + str(main(5)[0]))
