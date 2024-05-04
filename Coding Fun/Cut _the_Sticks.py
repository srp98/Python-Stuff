"""
Given a number of sticks of varying lengths, we iteratively cut the sticks into smaller sticks disregarding the shortest
pieces until there are none left. At iteration we determine the length of the shortest stick remaining, cut that length
from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks
are same length, they cannot be shortened so discard them.
"""


def cut_stick(a):
    """
    Takes in a array of integers and returns the array of integers before performing cutting of high value integers with
    lowest value integer and discarding it. This is repeated until all are expended.
    :param a: array of integers
    :return: array of integers before cutting operation performed
    """
    r = []
    while len(arr) > 0:
        r.append(len(arr))
        arr[:] = [x - min(arr) for x in arr if x - min(arr) > 0]

    return r


if __name__ == '__main__':
    n = int(input('Enter the number of sticks:\n'))
    arr = list(map(int, input().rstrip().split()))
    print(cut_stick(arr))
