'''
Project Euler Problem 61:

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following
formulae:

Triangle:
P(3,n)=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square:
P(4,n)=n^2	 	1, 4, 9, 16, 25, ...
Pentagonal:
P(5,n)=n(3n−1)/2     	1, 5, 12, 22, 35, ...
Hexagonal:
P(6,n)=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal:
P(7,n)=n(5n−3)/2	1, 7, 18, 34, 55, ...
Octagonal:
P(8,n)=n(3n−2)	 	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

The set is cyclic, in that the last two digits of each number is the first
two digits of the next number (including the last number with the first).

Each polygonal type: triangle (P(3,127)=8128), square (P(4,91)=8281), and
pentagonal (P(5,44)=2882), is represented by a different number in the set.

This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.
'''

def tri(n):
    #get the nth triangular number
    num = int(n*(n+1)/2)
    return num

def sq(n):
    num = int(n**2)
    return num

def pen(n):
    num = int(n*((3*n)-1)/2)
    return num

def hexn(n):
    num = n*((2*n)-1)
    return num

def hep(n):
    num = int(n*((5*n)-3)/2)
    return num

def octn(n):
    num = n*((3*n)-2)
    return num

def slen(n):
    s = str(n)
    return len(s)

def diglist(n):
    s = list(str(n))
    return s

def comblist(l):
    s = ''
    for char in l:
        s += char
    return int(s)

##def rot(n, m):
##    #n is the number to cycle, m is how many digits
##    d = diglist(n)
##    rotd = d[-m:] + d[:-m]
##    return comblist(rotd)

def iscyc(n, m):
    nlist = diglist(n)
    mlist = diglist(m)
    if nlist[-2:] == mlist[:2]:
        return True
    else:
        return False

def getwins():
    #get sets of four digit numbers of each type; 150 is an upper bound
    #found by trial and error
    wins = [set([tri(i) for i in range(1,150) if slen(tri(i)) == 4]), \
            set([sq(i) for i in range(1,150) if slen(sq(i)) == 4]), \
            set([pen(i) for i in range(1,150) if slen(pen(i)) == 4]), \
            set([hexn(i) for i in range(1,150) if slen(hexn(i)) == 4]), \
            set([hep(i) for i in range(1,150) if slen(hep(i)) == 4]), \
            set([octn(i) for i in range(1,150) if slen(octn(i)) == 4])]
    return wins

def match3(wins):
    paths = []
    for item in wins[0]:
        for i in range(1, 6):
            for e in wins[i]:
                if iscyc(item, e):
                    paths.append([(item, 3), (e, i+3)])
    return paths

def rematch(paths, wins):
    newpaths = []
    for path in paths:
        visited = [node[1] for node in path]
        last = path[-1][0]
        for i in range(1,6):
            if i+3 not in visited:
                for test in wins[i]:
                    if iscyc(last, test):
                        newpaths.append(path + [(test, i+3)])
    return newpaths
        


def main():
    wins = getwins()
    paths = match3(wins)
    for i in range(4):
        paths = rematch(paths, wins)
    for path in paths:
        if iscyc(path[-1][0], path[0][0]):
            #print(path)
            return sum(item[0] for item in path)
    
            
            
            


print("Problem 61 solution: " + str(main()))
