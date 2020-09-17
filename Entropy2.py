import math 
import re
import string
import operator as op
from functools import reduce



# Computes n choose r. In python 3.8 the function math.comb is available
def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


# Read the entire file, make it all lower case. 
file = open('text_files/1kinghenryiv.txt')
file_contents = file.read()

# Strip everything not a letter
pattern = re.compile('[\d\W_]+')
file_contents = pattern.sub('', file_contents)
file_contents = file_contents.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# possible_combinations = nCr(26, 1)
length_of_text = len(file_contents)

# This is for the case where strings are just a single character long 
total_entropy = 0
for letter in alphabet:
    count = file_contents.count(letter)
    prob = count / length_of_text
    total_entropy -= prob * math.log2(prob)

print(total_entropy)
