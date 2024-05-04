# Time Conversion Function
def time_conversion(t):
    """
    Given a time in 12-hour AM/PM format, convert to 24-hour time.
    :param t: Input time string in 12-hour format (hh:mm:ss AM/PM) where 01<=hh<=12 and 00<=mm,ss<=60
    :return: Output 24-hour conversion of time 't' string (hh) 00<=hh<=23
    """
    h, m, s = map(int, t[:-2].split(':'))
    p = t[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    conv = f'{h:02d}:{m:02d}:{s:02d}'
    print(conv)


if __name__ == '__main__':
    # Give the Time
    print("Enter the time you wish to convert from 12-hour format to 12-hour format in (hh:mm:ss AM/PM) "
          "where 01<=hh<=12 and 00<=mm,ss<=6")
    x = str(input())
    time_conversion(x)
