"""
A Sequence of consecutive steps above sea-level starting with a step up from sea-level and ending with a step down to
sea level is a 'Mountain'

A Sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to
level is a 'Valley'

Given a sequence of up and down steps, we find the number of valleys encountered.

Eg: s = [D D U U U U D D], start with 2 valleys and 2 mountains after then climbs down to sea level.
"""
import re
import itertools


def count_valley(x, y):
    """
    Takes number of steps and steps sequence as input and prints the number of valleys
    :param x: number of steps
    :param y: sequence of steps (D, U)
    :return: number of valleys in the sequence
    """
    level, valley = 0, 0
    for step in y:
        if step == 'U':
            level += 1
        else:
            level -=1
        if step == 'U' and level == 0:
            valley += 1

    return valley


if __name__ == '__main__':
    n = int(input('Enter the number of steps taken'))
    print(f'Enter the {n} sequence of steps (U, D): ')
    s = str(input())
    print(f'The Number of valleys hiked: {count_valley(n, s)}')
