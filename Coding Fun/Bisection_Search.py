# First Bi-Section Algorithm (not so efficient)
def b_s(lis, e):
    """
    Assuming List is sorted Bi-Section Search
    :param lis: Sorted list of numbers
    :param e: Element we are looking for
    :return: Boolean to see if element is found or not
    """

    # Check if list is empty
    if len(lis) == 0:
        return False

    # Check if list is single element
    elif len(lis) == 1:
        return lis[0] == e

    # left over Case
    else:

        # Find Mid point
        half = len(lis) // 2

        # Check if mid is element
        if lis[half] == e:
            return True

        # Check if element is bigger than middle element
        elif e > lis[half]:
            return b_s(lis[half:], e)

        else:
            return b_s(lis[:half], e)


# Second Bi-Section Algorithm (Efficient than first)
def b_s_best(lis, e):
    """
    Assuming List is sorted Bi-Section Search
    :param lis: Sorted list of numbers
    :param e: Element we are looking for
    :return: Boolean to see if element is found or not
    """

    def b_s_helper(lis, e, low, high):
        """
        Helper Function for Bisection Search
        :param lis: Sorted List of numbers
        :param e: Element we are looking for
        :param low: low end of the list to start looking from
        :param high: high end of the list to stop looking for
        :return: Boolean if element found
        """
        if low == high:
            return lis[low] == e

        mid = (low + high) // 2
        if lis[mid] == e:
            return True

        elif e > lis[mid]:
            return b_s_helper(lis, e, mid + 1, high)

        else:
            return b_s_helper(lis, e, low, high - 1)

    if len(lis) == 0:
        return False
    else:
        return b_s_helper(lis, e, 0, len(lis) - 1)
