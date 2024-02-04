# X for starship placement and hit
# ' ' for available space
# '-' for missed shot

from random import randint


LENGTH_OF_STARSHIPS = [5, 4, 3, 3, 2]
PLAYER_BOARD = [[' '] * 8 for x in range (8)]
COMPUTER_BOARD = [[' '] * 8 for x in range (8)]
PLAYER_GUESS_BOARD = [[' '] * 8 for x in range (8)]
COMPUTER_GUESS_BOARD = [[' '] * 8 for x in range (8)]

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
    print('  A B C D E F G H')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print('  ----------------')



def place_ships(board):
    pass

def check_ship_fit():
    pass

def ship_overlap():
    pass

def user_input():
    pass

def turn(board):
    pass

#while True:




# Create 5 starships in random locations
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row] [ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'

# User inputs row and column
def get_star_location():
    row = input('please enter ship row: ')
    while row not in '12345678':
        print('You must enter a valid row number 1-8')
        row = input('please enter ship row: ')
    column = input('please enter ship column: ').upper()
    while column not in 'ABCDEFGH':
        print('You must enter a valid column letter A-H')
        column = input('please enter ship column: ').upper()
    return int(row) - 1, letters_to_numbers[column]

#Check if all starships are hit
def ship_hit_count(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships()
print_board()
turns = 10
while turns > 0:
    print('Welcome to Star Trek Battleships')
    print_board(GUESS_BOARD)
    row, column = get_starship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You have already fired at this location')
    elif HIDDEN_BOARD[row] [column] == 'X':
        print('Direct hit!')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('We have missed the enemy, Captain')
        GUESS_BOARD[row] [column] = '-'
        turns -= 1
    if starship_hit_count(GUESS_BOARD) == 5:
        print('Congratulations Captain, we have destroyed all enemy ships')
        break
    print('you have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('You ran out of turns, game over')







