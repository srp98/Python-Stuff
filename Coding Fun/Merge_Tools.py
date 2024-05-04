"""
Given a string 's' of length of 'n' and an integer 'k' where 'k' is a factor of 'n', we can split 's' into 'n/k'
sub-segments where each segment is a contiguous block of 'k' characters in 's'.

Using these segments to create strings such that:
- The characters are sub-sequence of characters from these segments
- Any repeat occurrence of a character is removed from the strings

Print n/k lines where each line denotes sub string
"""
from collections import OrderedDict


def merge_the_tools(string, k):
    for x in range(0, len(string), k):
        print(''.join(list(OrderedDict.fromkeys(string[x: x+k]))))
