def smash_candies(total_candies, friend_count=3):
    """
    Function for Candy-sharing friends Alice, Bob and Carol. They have some candies which they plan to split evenly
    among themselves. For the sake of their friendship, any candies left over would be smashed. For example, if they
    collectively bring home 91 candies, they'll take 30 each and smash 1.

    Also will calculate the number of candies to smash for *any* number of total candies. Modifying it so that it
    optionally takes a second argument representing the number of friends the candies are being split between. If no
    second argument is provided, it should assume 3 friends, as before.

    -End of Doc String for the function-
    """
    return total_candies % friend_count


candies = 67
print(smash_candies(candies))
print(help(smash_candies))


def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
    return total_candies % 3


to_smash(91)
to_smash(1)
