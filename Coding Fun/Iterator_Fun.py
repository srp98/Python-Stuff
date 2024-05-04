"""
Given list of N lowercase English letters, for given integer K select K indices from the list.

Find probability that at atleast one of the K indices selected will contain the letter 'a'
"""
from itertools import combinations

print('Enter an integer denoting the length of the list, followed by lowercase english letters denoting the elements '
      'of the list which are space separated.')
n_l = int(input())
s = input().lower().split()
print('Enter the integer K: ')
k = int(input())
combi = list(combinations(s, k))

n = len(combi)
n_a = sum([True for word in combi if 'a' in word])

print(f'{n_a/n:.3f}')
