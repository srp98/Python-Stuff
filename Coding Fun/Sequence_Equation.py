"""
Given a sequence of distinct integers, for each 'x' we have to find a integer 'y' such that p(p(y)) = x.
"""


def perm_eq(s):
    for i in range(n):
        x = i+1
        first_index = s.index(x)
        second_index = s.index(first_index + 1)
        y = second_index + 1
        return y


if __name__ == '__main__':
    n = int(input('Enter the number of elements:\n'))
    p = list(map(int, input().rstrip().split()))
    print(perm_eq(p))
