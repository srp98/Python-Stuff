"""
Function Norm to be filled
"""
import string


def designer_pdf(arr, word):
    """
    Function takes an array of integers representing the heights of each letter and a word
    :param arr: An array of letter heights
    :param word: The word string to be calculated
    :return: The max area that can be constructed with the given word lengths
    """
    alp = list(string.ascii_lowercase)
    word_ind = [alp.index(str(t)) for t in word]
    word_h = [arr[i] for i in word_ind]
    area = max(word_h)*len(word)
    return area


if __name__ == '__main__':
    h = list(map(int, input('Enter 26 space separated heights of the letters').rstrip().split()))
    w = str(input('Enter a word string'))
    print(designer_pdf(h, w))
