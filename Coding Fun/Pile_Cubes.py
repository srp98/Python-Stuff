"""
Program to pile cubes given a horizontal row of cubes with given length,
The pile follows the rule that
    -> cube(i) is on top of cube(j) if len(cube(i)) <= len(cube(j))
"""

from collections import deque
T = int(input())
for _ in range(T):
    pile = True
    n = int(input())
    sideLengths = deque(map(int, input().split()))
    while len(sideLengths) > 1:
        if sideLengths[0] >= sideLengths[1]:
            sideLengths.popleft()
        elif sideLengths[-1] >= sideLengths[-2]:
            sideLengths.pop()
        else:
            pile = False
            break
    print("Yes" if pile else "No")
