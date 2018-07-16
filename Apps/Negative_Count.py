a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

holder = [a, b, c, d]
# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [len(a), len(b), len(c), len(d)]
print(lengths)

lengths2 = map(lambda x: len(x), holder)
print(lengths2)

lengths3 = [len(x) for x in holder]
print(lengths3)

# Fashionably Late
"""A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, 
they must not be the very last guest (that's taking it too far)."""
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']


def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


print(fashionably_late(party_attendees, 5))


# Negative numbers
def count_negatives(nums):
    """Return the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    nums.append(0)
    # We could also have used the list.sort() method, which modifies a list, putting it in sorted order.
    nums = sorted(nums)
    return nums.index(0)


def count_negatives2(nums):
    # Equivalent to "if len(nums) == 0". An empty list is 'falsey'.
    if not nums:
        return 0
    else:
        # Implicitly converting a boolean to an int! See question 6 of the day
        # 3 exercises.
        return (nums[0] < 0) + count_negatives2(nums[1:])
