"""
Program to count the occurrences of each word given the input 'n' words.
Characters are English alphabets only.

Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1
"""
# Import Iter Lib
from collections import OrderedDict

d = OrderedDict()
word = ""

for _ in range(int(input())):
    string = input()
    string = string.lower()
    d[string] = d.get(string, 0) + 1

print(len(d))
print(*d.values())
