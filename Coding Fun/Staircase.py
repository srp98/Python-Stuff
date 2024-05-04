# Staircase Function
def staircase(n):
    """
    Function prints a staircase of '#' given the size n where the first step and height of the staircase is n

    :param n: Size of the staircase
    :return: Staircase of size 'n' with #
    """
    for i in range(n+1):
        print(('#'*i).rjust(n, ' '))


if __name__ == '__main__':
    print("Enter the Size of the stair case")
    n = int(input())

    staircase(n)
