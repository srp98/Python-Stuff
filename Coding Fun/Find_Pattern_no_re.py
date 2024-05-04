# A Simple Pattern Matching Program without Regular Expressions


# Phone Pattern Function
def is_pn(text):
    # Check for Size
    if len(text) != 12:
        return False

    # First 3 numbers check
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    # Check for '-' after 3 numbers
    if text[3] != '-':
        return False

    # Next 3 numbers
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    # Check for '-' for next 3 numbers
    if text[7] != '-':
        return False

    # Last 4 numbers!
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


# Find Phone Number
def find_pn(message):
    for i in range(len(message)):
        chunk = message[i:i+12]
        if is_pn(chunk):
            print(f'Phone Number Found! It\'s: {chunk}')
    print('Done!')


if __name__ == '__main__':
    # Take input from user and check if it's a Phone Number
    _text = input('Enter text for checking...')

    _message = input('Enter Message...')

    # Check if Phone Number!
    if is_pn(_text):
        print(f'Yes! {_text} is a Phone Number!!')
    else:
        print(f'No {_text} is not a Phone Number!')

    # Find Phone Number in message!
    find_pn(_message)
