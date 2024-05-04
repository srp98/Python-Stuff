# Import Required Lib's
import random


# Simple Tic-Tac-Toe Game
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def simple_ttt():
    # Define the Board
    the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    # The Loop!
    turn = 'X'
    for i in range(9):
        print_board(the_board)
        print('Turn for ' + turn + '. Move on which space ?')
        move = input()
        the_board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        print_board(the_board)


if __name__ == '__main__':

    # Run Simple Tic-Tac-Toe
    simple_ttt()