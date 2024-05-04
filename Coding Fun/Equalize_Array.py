"""
Given an array of integers, determine the minimum number of elements to delete to reduce the array until all remaining
elements are equal.

Eg. arr = [1, 2, 2, 3], we can delete 2 elements: 1 and 3; we get arr = [2, 2]. Another approach would be deleting both
2's and either 1 or 3 but would take 3 deletions. So, first choice is chosen.
"""
from collections import Counter


def equal_array(a, b):
    """
    Takes an array of integers and deletes some elements of it to equalize the array with minimum amount of deletions.
    :param a: An array of integers
    :param b: Length of the array 'a'
    :return: An integer denoting the number of deletions done
    """
    return b - Counter(a).most_common()[0][1]


if __name__ == '__main__':
    n = int(input('Enter the number of elements:\n'))
    arr = list(map(int, input(f'Enter the array of {n} elements:\n')))
    print(equal_array(arr, n))
