# X for starship placement and hit
# ' ' for available space
# '-' for missed shot

import random

# Constants
LENGTH_OF_SHIPS = [5, 4, 3, 3, 2]
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


# Place all ships of different lengths and make sure they don't overlap
def place_ships(board):
    #Loop through each ship length  
    for ship_length in LENGTH_OF_SHIPS:
        #Loop until ship is placed without overlapping
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if check_ship_fit(ship_length, row, column, orientation):
                    # Check is ship is placed without overlapping
                    if ship_overlap(board, row, column, orientation, ship_length) == False:
                        # Place ship on board
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True
                print('place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    if ship_overlap(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        print_board(PLAYER_BOARD)
                        break



def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True
    

def ship_overlap(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False
    

def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter orientation horizontal or Vertical (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except ValueError:
                print("Please enter H or V")
        while True:
            try:
                row = int(input("Enter row number (1-8): ")) - 1
                if row >= 0 and row <= 7:
                    row = int(row)
                    break
            except ValueError:
                print("Please enter a row number between 1-8")
        while True:
            try:
                column = input("Enter column letter (A-H): ").upper()
                if column in "ABCDEFGH":
                    column = letters_to_numbers[column]
                    break
            except ValueError:
                print("Please enter a column letter between A-H")
        return row, column, orientation
    else:
        while True:
            try:
                row = int(input("Enter row number (1-8): ")) - 1
                if row >= 0 and row <= 7:
                    row = int(row)
                    break
            except ValueError:
                print("Please enter a row number between 1-8")
        while True:
            try:
                column = input("Enter column letter (A-H): ").upper()
                if column in "ABCDEFGH":
                    column = letters_to_numbers[column]
                    break
            except ValueError:
                print("Please enter a column letter between A-H")
        return row, column
    

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


place_ships(COMPUTER_BOARD)
print_board(COMPUTER_BOARD) #comment this back in for testing purposes.
print_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)

while True:
    #player turn
    while True:
        print('Captain, the enemy has knocked out our sensors, we are blind! Where should we fire?')
        print_board(PLAYER_GUESS_BOARD)
        turn(PLAYER_GUESS_BOARD)
        break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print("Congratulations Captain! all enemy ships have been destroyed")
        break
    #Computer turn
    while True:
        turn(COMPUTER_GUESS_BOARD)
        break
    print_board(COMPUTER_GUESS_BOARD)
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print("Captain, we have been defeated!")
        break









