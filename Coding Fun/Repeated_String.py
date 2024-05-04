"""
Given a string of lowercase english letters repeated infinite times, given integer 'n' print the number of letter 'a' in
the first 'n' letters of the infinite string
"""


def repeated_letter(s, x):
    return s.count("a") * (x // len(s)) + s[:n % len(s)].count("a")


if __name__ == '__main__':
    string = input('Enter the String:\n').lower()
    n = int(input('Enter an integer:\n'))
    print(repeated_letter(string, n))
