# Decrypt a Matrix of characters to readable format converting special characters to white space.
# Import Required Lib's
import re
import os
import sys
import random
import math


# Main Functionality of the Program
if __name__ == '__main__':
    print("Give rows and column numbers separated by space where rows > 0 and columns < 100")
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    matrix = []
    for _ in range(n):
        print("Input the Matrix Row followed by 'Enter': ")
        matrix_item = input()
        matrix.append(matrix_item)
    print(matrix)
