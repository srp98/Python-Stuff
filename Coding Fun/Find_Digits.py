"""
Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of
divisors occurring within the integer.
"""


def find_digits(x):
    """
    Takes in an integer as input and returns an integer representing the number of digits of 'd' that are divisors of
    'd'.
    :param x: An integer
    :return: Integer denoting the number of divisors of the given integer
    """
    return len([i for i in str(x) if (int(i) > 0) and (x % int(i) == 0)])


if __name__ == '__main__':
    t = int(input('Enter the number of test cases:\n'))
    for _ in range(t):
        n = int(input('Enter the integer:\n'))
        print(find_digits(n))
