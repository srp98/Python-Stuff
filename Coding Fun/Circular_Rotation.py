"""
Given an array of integers, we need to perform an right shift operation i.e the last element of array becomes the first
and every element shifts to the next position.
"""
from collections import deque


def rotation(arr, ct, ix):
    dq = deque(arr)
    dq.rotate(ct)
    return dq[ix]


if __name__ == '__main__':
    print('Enter the number of elements in integer, rotation count and number of queries:\n')
    n, k, q = list(map(int, input().rstrip().split()))
    print('Enter the integers in the array:\n')
    a = list(map(int, input().rstrip().split()))
    for _ in range(q):
        m = int(input('Enter the index to check after rotation:\n'))
        print(rotation(a, k, m))
