"""
Given a string of integers S which contains character which repeat X times, replace consecutive occurrences of these
characters with (X, c) in the string.
"""
from itertools import groupby

print('Enter the string:')
s = str(input())
print(*[(len(list(c)), int(k)) for k, c in groupby(s)])
