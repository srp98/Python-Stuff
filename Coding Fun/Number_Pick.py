"""
Given an array of integers, find and print the maximum number of integers you can select from an array such that the
absolute difference between any two of integers is less than or equal to 1.
"""


def pick_numbers(arr):
    """
    Function which picks the maximum length of the numbers given a array which satisfy the condition, any two numbers
    picked their absolute difference is less than or equal to 1
    :param arr: Array of numbers
    :return: Max length of numbers picked
    """

    maximum = 0
    for i in arr:
        c = arr.count(i)
        d = arr.count(i-1)
        c = c + d
        if c > maximum:
            maximum = c
    return maximum


if __name__ == '__main__':
    n = int(input('Enter the size of the array, followed by the array: '))
    a = list(map(int, input().rstrip().split()))
    print(pick_numbers(a))
