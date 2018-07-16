from collections import Counter


def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


word1 = input('Please input first word:')
word2 = input('Please input the second word:')

if is_anagram(word1, word2) == 1:
    print('The Two given words are Anagrams')
else:
    print('The Two given words are not Anagrams')
