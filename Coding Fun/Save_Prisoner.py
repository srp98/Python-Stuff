"""
A Jailer wishes to distribute treats to prisoners who are seated sequentially in numbered chairs and a random number be
drawn to start distributing the treats in sequential order from the picked number. The last treat is a bad one and we
need to determine which prisoner gets it.

Eg:There are 4 prisoners and 6 pieces of candy. The prisoners arrange themselves in seats numbered 1 to 4. Let's suppose
two is drawn from the hat. Prisoners receive candy at positions 2, 3, 4, 1, 2, 3. The prisoner to be warned sits in
chair number 3.
"""


def save_prisoner(p, q, r):
    """
    Function takes 3 inputs representing number of prisoners, number of sweets and chair number to start passing
    out treats at and returns the number at which the last treat is given.
    :param p: Number of prisoners
    :param q: Number of sweets
    :param r: Chair number to start passing treats at
    :return: The number at which the last treat will be given
    """
    return ((q - 1 + r - 1) % p) + 1


if __name__ == '__main__':
    t = int(input('Enter the number of Test Cases: '))
    for _ in range(t):
        print('Enter number of prisoners(n), number of sweets(m) and chair number to start passing out treats at(s)')
        n, m, s = map(int, input().rstrip().split())
        print(save_prisoner(n, m, s))
