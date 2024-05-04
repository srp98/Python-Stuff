# Function to print each number out of the given number in a new line adding up to the number
def number_line(a):
    """
    Prints each character of a given number in a new line shown below:
    Given 429,
    Outputs: 9
    29
    429
    :param a: A Number in string format
    :return: Numbers of the given number in new lines until the full number printed
    """
    st = ''
    for i in range(1, len(a)+1):
        st = a[-i] + st
        print(st)


if __name__ == '__main__':
    print("Enter a number: ")
    n = str(input())
    number_line(n)
