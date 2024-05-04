# Plus Minus Function
def plus_minus(arr):
    """
    Given an array calculate the fractions of its elements that are positive, negative and zeros.
    :param arr: An array of size ranging from [0, 100] and elements of it ranging from [-100, 100]
    :return: fractions on separate lines rounded to six decimals
    """
    pos, neg, zeros = 0, 0, 0
    length = len(arr)
    for x in range(length):
        if arr[x] > 0:
            pos += 1
        elif arr[x] < 0:
            neg += 1
        else:
            zeros += 1

    return f"{pos/length: .6f} \n {neg/length: .6f} \n {zeros/length: .6f}"


if __name__ == '__main__':
    print("Enter the Size of the Array, ranging from [0, 100]: ")
    n = int(input())
    print("Enter the array elements in range [-100, 100]: ")
    a = list(map(int, input().split()))
    print(f'The result of the Plus_Minus Function is: {plus_minus(a)}')
