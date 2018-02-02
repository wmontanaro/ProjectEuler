'''
Project Euler Problem 59:

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text.
'''

#import, cycle through combinations, xoring and looking for " the "
#note that the ASCII range for lowercase characters is 97-122 (inclusive)

import itertools

def get_data():
    s = [line.rstrip() for line in \
         open("Problem0059Data.txt", "r").readlines()]
    d = [int(item) for item in s[0].split(",")]
    return d

def get_ascii(word):
    ascii_word = [ord(char) for char in word]
    return ascii_word

def get_longkey(key, length):
    #cycle through key until its length is length
    l = []
    cycle_len = len(key)
    cycle_ind = 0
    while len(l) < length:
        l.append(key[cycle_ind])
        cycle_ind += 1
        if cycle_ind == cycle_len:
            cycle_ind = 0
    return l

def is_sublist(sublist, longlist):
    sublen = len(sublist)
    for i in range(len(longlist)-sublen+1):
        if longlist[i:i+sublen] == sublist:
            return True
    return False

def dec(words):
    #words is a list containing the dictionary strings we are searching for
    asciiwords = [get_ascii(word) for word in words]
    encmsg = get_data()
    msglength = len(encmsg)
    #format of keyspace is (a,b,c)
    keyspace = [p for p in itertools.product(range(97,123), repeat = 3)]
    for key in keyspace:
        longkey = get_longkey(key, len(encmsg))
        decmsg = [i^j for i,j in zip(encmsg, longkey)]
        for word in asciiwords:
            if is_sublist(word, decmsg):
                return decmsg

def main(words):
    decmsg = dec(words)
    #s = "".join([chr(c) for c in decmsg])
    #print(s)
    return sum(decmsg)

print("Problem 59 solution: " + str(main([" the "])))
