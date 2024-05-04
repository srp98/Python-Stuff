# Tiny Function to check if a given year is Leap Year or not according to Georgian Calendar
def leap(y):
    """
    Functions check if given year is Leap Year or not according to Georgian Calender i.e.,
    - Year can be divided by 4 but not divided by 100 unless it is divisible by 400.
    Eg: 2000, 2400 are leap years but 1800, 1900, 2100, 2200, 2300 and 2500 are not.
    :param y: Given Year range: [1900, 10^5]
    :return: True or False
    """
    return y % 4 == 0 and (y % 400 == 0 or y % 100 != 0)


if __name__ == '__main__':
    print("Enter the Year you wish to check for Leap within range: [1900, 10^5]")
    year = int(input())
    if year in range(1900, 10**5+1):
        print(leap(year))
    else:
        raise ValueError('Number out of bounds')
