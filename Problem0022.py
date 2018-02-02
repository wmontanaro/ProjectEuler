'''
Project Euler Problem 22:

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

def score(name):
    total = 0
    for char in name:
        total += ord(char)-64
    return total

def main(fname):
    f = [item for item in open(fname).readlines()]
    d = f[0].replace('"', '')
    s = d.split(",")
    s.sort()
    tot_score = 0
    for ind in range(len(s)):
        name_score = score(s[ind])
        tot_score += (name_score * (ind+1))
    return tot_score

print("Problem 22 solution: " + str(main("Problem0022data.txt")))
