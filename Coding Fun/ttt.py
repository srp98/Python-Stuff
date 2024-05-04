# Import Random Library
import random
import copy


def draw_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def input_player_letter():

    letter = ''
    while not (letter == 'X' or letter == '0'):
        print('Do you want to be X or 0 ?')
        letter = input().upper()

    if letter == 'X':
        return ['X', '0']
    else:
        return ['0', 'X']


def who_goes_first():

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():

    print('Do you want to play again ? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def get_board_copy(board):

    dupe_board = copy.copy(board)
    return dupe_board


def is_space_free(board, move):

    return board[move] == ' '


def get_player_move(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move ? (1-9)')
        move = input()
    return int(move)
