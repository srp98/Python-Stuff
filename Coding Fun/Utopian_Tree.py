"""
The Program calculates the height of the tree given the 'n' number of growth cycles where the amount of growth is
defined for each season.
"""


def tree_height(c):
    """
    An Utopian tree goes through two cycles of growth every year, Each spring it doubles in height and in summer it
    increases by 1 meter. Based on this info the function calculates the tree height after the given number of cycles,
    if the height start from 1 meter.

    :param c: Number of growth cycles
    :return: The height of the plant growth after the given number of growth cycles
    """
    h = 1
    for i in range(c):
        if i % 2 == 0:
            h += h
        if i % 2 != 0:
            h += 1
    return h


if __name__ == '__main__':
    t = int(input('Enter the number of test cases:\n'))
    n = [input() for _ in range(t)]
    print(tree_height(n))
