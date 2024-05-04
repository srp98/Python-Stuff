"""
Function to determine whether we have enough money to buy 2 items from a electric shop, given price lists of 2 items
and the budget we have. We print the amount of money to spend to buy both items, if we can't buy both the items we
print -1.
"""


def get_money_spent(keyboards, drives, b):
    """
    Takes budget, prices of keyboards, drives as input and checks to see if we have budget to spend on both not
    exceeding the budget.
    :param keyboard: List of prices in integers of keyboards
    :param drives: List of prices in integers of USB drives
    :param b: Budget
    :return: Amount of money spent or '-1' if not enough money
    """
    return max([sum([x, y]) for x in keyboards for y in drives if sum([x, y]) <= b] + [-1])


if __name__ == '__main__':
    print('Enter budget, no. keyboard models and no. of USB drives separated by spaces')
    l = list(map(int, list(str(input()).split())))
    print('Enter the prices of keyboards with spaces')
    k = list(map(int, str(input()).split()))
    print('Enter the prices of USB drives with spaces')
    d = list(map(int, str(input()).split()))
    print(get_money_spent(k, d, l[0]))
