"""
Given an integer 'k' and two strings 's', 't' we have to determine if we can convert 's' to 't' by performing exactly
'k' of the operations on 's'. The operations include:

1.) Append a lowercase English alphabetic letter to the end of the string
2.) Delete the last character in the string. Performing this operation on an empty string results in an empty string

Eg: s=[a, b, c] and t=[d, e, f] moves,k=6

    To convert 's' to 't' we first delete all of the characters in 3 moves, next we add each of the characters of 't' in
    order. On the 6th move we will have matching string. if there had been more moves available, they could be
    eliminated by performing multiple deletions on an empty string. If there were fewer than 6 mores, we would not have
    succeeded in creating the new string.
"""


def append_delete(st1, st2):
    same_char = min(len(st1), len(st2))
    for i in range(len(st2)):
        if s[:i] != t[:i]:
            same_char = i-1
            break

    diff = len(st1) - same_char + len(st2) - same_char
    return 'YES' if (diff <= k and diff % 2 == k % 2) or len(st1) + len(st2) < k else 'NO'


def append_delete_2(s, t, k):
    s_length = len(s)
    t_length = len(t)

    if s_length + t_length < k:
        return 'Yes'

    same = 0
    for s_l, t_l in zip(s, t):
        if s_l == t_l:
            same += 1
        else:
            break

    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t

    if difference <= k and difference % 2 == k % 2:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    print('Enter the first string:\n')
    s = input()
    print('Enter the second string:\n')
    t = input()
    print('Enter the number of operations limit:\n')
    k = int(input())
    print('The output of the First Test Function:\n', append_delete(s, t))
    print('The output of the Second Test Function:\n', append_delete_2(s, t, k))
