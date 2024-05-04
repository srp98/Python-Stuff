"""
Happiness Function where we define an array of 'n' elements, define 2 disjoint sets A and B of 'm' integers aswell
where if an element in A is present in array we add the happiness +1 and -1 if present in B.
Initially we start with 0 happiness.

Since A, B are sets no repetitions but array might contain repeated elements.
"""


def happiness(array, set_a, set_b):
    """
    Function to count happiness
    :param array: Array of elements we like
    :param set_a: Set A elements which we like if present
    :param set_b: Set B elements which we don't like
    :return: Happiness Value
    """
    hap = 0
    pos = len(set_a.intersection(array))
    neg = len(set_b.intersection(array))
    hap = pos - neg
    return hap


def happiness_short(array, set_a, set_b):
    """
    Function to count happiness
    :param array: Array of elements we like
    :param set_a: Set A elements which we like if present
    :param set_b: Set B elements which we don't like
    :return: Happiness Value
    """
    return sum([(i in set_a) - (i in set_b) for i in array])


if __name__ == '__main__':
    print('Enter the number of elements in array (n) and in sets (m):')
    n, m = list(map(int, input().split()))
    print(f'Enter the {n} integers with space between each integer: ')
    arr = list(map(int, input().split()))
    print(f'Enter the {m} elements of Sets A and B in 2 lines with spaces between the numbers')
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(f'Happiness Function Output :{happiness(arr, A, B)}')
    print(f'Happiness_Short Function Output :{happiness_short(arr, A, B)}')
