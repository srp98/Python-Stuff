# Function returning the blown out candles of max height given 'n' candles and their heights
def blow_candles(x, y):
    """
    Function returns the number of candles blown out on condition that only max height candles can be blown out
    :param x: Number of candles
    :param y: Height of the candles
    :return: Number of candles blown out
    """
    assert x == len(y)
    return y.count(max(y))


if __name__ == '__main__':
    print('Give the No. of Candles on Cake: ')
    c = int(input())
    print('Give the height of each candles with space between each candle height: ')
    h = str(input())
    c_h = h.split(sep=' ')

    # Execute the Function
    print(f'No. of candles blown out are: {blow_candles(c, c_h)}')
