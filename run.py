# X for starship placement and hit
# ' ' for available space
# '-' for missed shot

from random import randint


# Create boards
HIDDEN_BOARD = [[' '] * 8 for x in range (8)]
GUESS_BOARD = [[' '] * 8 for x in range (8)]

# Convert letters to numbers for traditional battleships style
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# Print boards to terminal
def print_board(board):
    print('    A B C D E F G H')
    print('    ---------------')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1

# Create 5 starships in random locations
def create_starships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row] [ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row] [ship_column] = 'X'

# User inputs row and column
def get_starship_location():
    row = input('please enter ship row: ')
    while row not in '12345678':
        print('You must enter a valid row number 1-8')
        row = input('please enter ship row: ')
    column = input('please enter ship column: ')
    while column not in 'ABCDEFGH':
        print('You must enter a valid column letter A-H')
        column = input('please enter ship column: ')
    else:
        print('You must enter something')
    return int(row) - 1, letters_to_numbers[column]






def starship_hit_count():
    pass

create_starships()
turns = 10
while turns > 0:



