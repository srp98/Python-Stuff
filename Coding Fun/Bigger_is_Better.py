"""
A word is said to be greater than other word if it comes later in a lexicographically sorted list.

So, given a word we create a new word by swapping some or all of it's characters to meet two conditions:
- It must be greater than the original word
- It must be the smallest word that meets the first condition
"""


def bib(s):
    """
    Given a string 's' return the lexicographically greater word by swapping some or all characters of the word meeting
    two conditions:
    - It must be greater than the original word
    - It must be the smallest word that meets the first condition

    :param s: a string
    :return: lexicographically greater string
    """
    n = len(s)
    pass


if __name__ == '__main__':
    t = int(input("Enter the number of Test Cases: "))
    print('Enter the words followed by an new line: ')
    for _ in range(t):
        w = input()
        print(bib(w))
