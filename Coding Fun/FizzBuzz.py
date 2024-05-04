for i in range(1, 16):
    string = ""
    if i % 3 == 0:
        string += "Fizz"
    if i % 5 == 0:
        string += "Buzz"
    if i % 5 != 0 and i % 3 != 0:
        string += str(i)
    print(string)
