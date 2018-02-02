'''
Project Euler Problem 42:

The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''

def get_tri_nums(n):
    tri_nums = [1]
    i = 2
    while tri_nums[-1] < n:
        tri_nums.append(int(i*(i+1)/2))
        i += 1
    return set(tri_nums)
        
def get_word_val(word):
    total = 0
    for char in word:
        total += ord(char)-64
    return total

def main():
    d = [line for line in open("Problem0042Data.txt").readlines()]
    s = d[0]
    s = s.replace('"', "")
    words = s.split(",")
    tri_nums = get_tri_nums(14*26) #longest word is 14 chars, 26 is highest val
    winners = set()
    for word in words:
        if get_word_val(word) in tri_nums:
            winners.add(word)
    return winners
    

print("Problem 42 solution: " + str(len(main())))
