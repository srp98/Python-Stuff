"""
Given a Function and 'K' lists, We have to pick a element from each list so that the value from the equation below is
maximized
S = (f(x1) + f(x2) + ... + f(xk)) % M

1 <= K <= 7
1 <= M <= 1000
1 <= Ni <= 7
1 < Magnitude of elements in list < 10^9
"""


def maxim(l, m, k):
    """
    Calculates the square of the maximum value from given set of lists by choosing the max value from each list, summing
     it and then dividing the value by given m, shown in following formula:
     S = (f(x1) + f(x2) + ... + f(xk)) % M
    :param l: set of lists
    :param m: modulo value
    :param k: number of lists
    :return: Maximum Value calculated from the given formula
    """
    return sum(map(lambda x: x**2, [max(l[i][:]) for i in range(k)])) % m


if __name__ == '__main__':
    print("Enter the number of lists (K) and modulo value (M) with space separating each other, within the range:"
          "1 <= K <= 7, 1 <= M <= 1000")
    prim = str(input()).split()
    K, M = int(prim[0]), int(prim[1])
    print("Enter the numbers in lists separated by spaces and 'Enter' to move to next list with range:"
          "1 <= Ni <= 7, 1 < Magnitude of elements in list < 10^9")
    N = []
    for _ in range(K):
        N.append(list(map(int, input().split()[1:])))
    print(maxim(N, M, K))
