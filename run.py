# X for starship placement and hit
# ' ' for available space
# '-' for missed shot

import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

# Constants
LENGTH_OF_SHIPS = [5, 4, 3, 3, 2]
PLAYER_BOARD = [[' '] * 8 for x in range(8)]
COMPUTER_BOARD = [[' '] * 8 for x in range(8)]
PLAYER_GUESS_BOARD = [[' '] * 8 for x in range(8)]
COMPUTER_GUESS_BOARD = [[' '] * 8 for x in range(8)]

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


def main_welcome():
    """Prints welcome message to terminal."""
    print(Fore.RED + "Welcome to Star Trek Battleships! \n")
    print("To start the game, you simply place your ships on the board \n")
    print("Then take turns firing at each other's ships. \n")
    print("The first to destroy all ships (17 hits) wins! \n")


# Prints given boards to terminal
def print_board(board):
    print(Fore.BLUE + '  A B C D E F G H')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print('  ----------------')
    print({Fore.RESET})


# Place all ships of different lengths and make sure they don't overlap
def place_ships(board):
    # Loop through each ship length
    for ship_length in LENGTH_OF_SHIPS:
        # Loop until ship is placed without overlapping
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = (
                    random.choice(["H", "V"]),
                    random.randint(0, 7),
                    random.randint(0, 7)
                )
                if check_ship_fit(ship_length, row, column, orientation):
                    # Check is ship is placed without overlapping
                    if not ship_overlap(board, row, column, orientation,
                                        ship_length):
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
                    if not ship_overlap(board, row, column, orientation,
                                        ship_length):
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
    if place_ship is True:
        while True:
            orientation = input(
                "Enter Horizontal or Vertical (H or V): "
            ).upper().strip()
            orientation = orientation.strip()
            if orientation in ["H", "V"]:
                break
            else:
                print(f"""
{Fore.YELLOW}You must enter H or V to place your ship{Fore.RESET}""")
                print('\033[39m')
        while True:
            try:
                row = int(input("Enter row number (1-8): ")) - 1
                if row >= 0 and row <= 7:
                    break
                else:
                    print(f"""
{Fore.YELLOW} Must enter a row number between 1-8! {Fore.RESET}

""")
            except ValueError:
                print(Fore.YELLOW + "Please enter a row number between 1-8")
                print('\033[39m')
        while True:
            try:
                column = input("Enter column letter (A-H): ").upper().strip()
                if column in "ABCDEFGH":
                    column = letters_to_numbers[column]
                    break
                else:
                    print(Fore.YELLOW + "Must enter a column between A-H!")
                    print('\033[39m')
            except KeyError:
                print(Fore.YELLOW + "Please enter a column letter between A-H")
                print('\033[39m')

        return row, column, orientation
    else:
        while True:
            try:
                row = int(input("Enter row number (1-8): ")) - 1
                if row >= 0 and row <= 7:
                    break
                else:
                    print(Fore.YELLOW + "Must enter a row number between 1-8!")
                    print('\033[39m')
            except ValueError:
                print(Fore.YELLOW + "Please enter a row number between 1-8")
                print('\033[39m')
        while True:
            try:
                column = input("Enter column letter (A-H): ").upper().strip()
                if column in "ABCDEFGH":
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print(Fore.YELLOW + "Please enter a column letter between A-H")
                print('\033[39m')
        return row, column


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def turn(board):
    while True:  # Start a loop that will continue until a valid move is made
        if board == PLAYER_GUESS_BOARD:
            row, column = user_input(PLAYER_GUESS_BOARD)
            # Check if the move is valid and if it hits or misses
            if board[row][column] == "-":
                continue  # If the move is valid but misses, continue the loop
            elif board[row][column] == "X":
                continue  # If the move is valid and hits, continue the loop
            elif COMPUTER_BOARD[row][column] == "X":
                board[row][column] = "X"
                break  # If the move hits, break the loop
            else:
                board[row][column] = "-"
                break  # If the move misses, break the loop
        else:
            row, column = random.randint(0, 7), random.randint(0, 7)
            if board[row][column] == "-":
                continue
            elif board[row][column] == "X":
                continue
            elif PLAYER_BOARD[row][column] == "X":
                board[row][column] = "X"
                break
            else:
                board[row][column] = "-"
                break


def main():
    main_welcome()
    place_ships(COMPUTER_BOARD)
    # Comment this back in for testing purposes.
    # print_board(COMPUTER_BOARD)
    print_board(PLAYER_BOARD)
    place_ships(PLAYER_BOARD)

    while True:
        # player turn
        while True:
            print(
                f"""Captain, they've knocked out our sensors,
                Where should we fire?
{print_board(PLAYER_GUESS_BOARD)}"""
            )
            turn(PLAYER_GUESS_BOARD)
            break
        if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
            print(
                f"""Congratulations Captain,
                we've destroyed all enemy ships!"""
            )
            break
        # Computer turn
        while True:
            turn(COMPUTER_GUESS_BOARD)
            break
        print_board(COMPUTER_GUESS_BOARD)
        if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
            print("Captain, we have been defeated!")
            break


if __name__ == "__main__":
    main()
