# Imports
import random  # Used for computer moves

# Variable 'grid' that is a list of empty strings to create grid.
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
symbol = ["x", "o"]


def print_grid():
    """
    Prints the list from the grid variable. Sets position for each item
    within the list.
    """
    print(" Game Grid ")
    print(" " + grid[1] + " | " + grid[2] + " | " + grid[3] + "  ")
    print("---|---|---")
    print(" " + grid[4] + " | " + grid[5] + " | " + grid[6] + "  ")
    print("---|---|---")
    print(" " + grid[7] + " | " + grid[8] + " | " + grid[9] + "  ")
    print("\n")


def reset_grid():
    """
    Resets the grid and adds new items in order to let user start a new
    game.
    """
    grid.clear()
    grid.extend([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])


def main():
    """
    The main function that gets called once the script has started
    """
    print("Welcome to Tic Tac Toe!\n")
    print("Please select one of the following options.")
    print("1. Play the game.")
    print("2. How to play")
    # Loops through user inputs to go to next menu.
    while True:
        user_choice = input()
        if user_choice == "1":
            game_type()
        elif user_choice == "2":
            how_to_play()
        else:
            print("Wrong input. Please use the numbers '1' or '2'.")


def how_to_play():
    """
    Instructions on how to play the game.
    """
    print("1. The game is played on a grid that's "
          "3 squares by 3 squares.")
    print("2. You choose your symbol being either 'X' or 'O'. "
          "Your opponent will get the ones that's left.")
    print("3. Look at the reference grid to know which box "
          "is assigned to which number.")
    print("4. The first player to get 3 of her marks in a row "
          "(up, down, across, or diagonally) is the winner.")
    print("5. When all 9 squares are full, the game is over. If no "
          "player has 3 marks in a row, the game ends in a tie.\n")
    print("Enter '0' to return to main menu.")
    # Loops through user inputs and returns to main menu.
    while True:
        user_choice = input()
        if user_choice == "0":
            main()
        else:
            print("Wrong input, please use the number '0'.\n")


def game_type():
    """
    Let's user select which game he/she wants to play depending if it's
    against computer or 2nd player.
    """
    print("1. Play the game against computer.")
    print("2. Play the game against your friend.")
    while True:
        user_choice = input()
        global game_level
        if user_choice == "1":
            game_level = 1
            play_game()
        elif user_choice == "2":
            game_level = 2
            play_game()
        else:
            print("Wrong input. Please use the numbers '1' or '2'.")


def winner(grid, user):
    """
    Check if the player or computer has won the game by going through
    each possible combination for winning game. If it's a win then
    returns true otherwise returns false.
    """
    if (grid[1] == user and grid[2] == user and grid[3] == user) or \
       (grid[4] == user and grid[5] == user and grid[6] == user) or \
       (grid[7] == user and grid[8] == user and grid[9] == user) or \
       (grid[1] == user and grid[4] == user and grid[7] == user) or \
       (grid[2] == user and grid[5] == user and grid[8] == user) or \
       (grid[3] == user and grid[6] == user and grid[9] == user) or \
       (grid[1] == user and grid[5] == user and grid[9] == user) or \
       (grid[3] == user and grid[5] == user and grid[7] == user):
        return True
    else:
        return False


def draw(grid):
    """
    Checks if the grid has empty strings left. If there is more than 1
    empty string returns false, otherwise returns true and therefore
    the game has ended with a draw.
    """
    if grid.count(" ") > 1:
        return False
    else:
        return True


def computer_move(grid, opponent_symbol):
    """
    Loop for the computer to move to a random position within the grid.
    Checks if the grid is an empty string, if yes places correct symbol
    and breaks out of the loop.
    """
    while True:
        move = random.randint(1, 9)
        if grid[move] == " ":
            return move


def play_game():
    """
    The main game function that gets executed after all previous options
    gets put through.
    """
    # Let's user select the symbol he/she wants to play as. Either 'X'
    # or 'O'. Prints out to user message that wrong symbol has been
    # chosen, if so restarts the game.
    print(f"Do you want to play as a '{symbol[0]}' or an '{symbol[1]}?' \n")
    player_symbol = input().lower()
    if player_symbol == symbol[0]:
        opponent_symbol = symbol[1]
    elif player_symbol == symbol[1]:
        opponent_symbol = symbol[0]
    else:
        print("Wrong symbol, please use either 'X' or 'O'.\n")
        play_game()
    # The main game loop
    while True:
        print_grid()
        # The main player loop that loops through input.
        while True:
            # Loops through until correct input from user has been
            # given. Checks if the space is taken and prints out message
            # to user if the input or space is taken.
            try:
                choice = int(input(f"Please choose an empty space for for "
                                   f"your next move as '{player_symbol}'. \n"))
                if choice in range(1, 10):
                    if grid[choice] == " ":
                        grid[choice] = player_symbol
                        break
                    else:
                        print("Ups, that space is taken!")
                else:
                    print("Wrong number. Please use the numbers "
                          "between 1-9.\n")
            except ValueError:
                print("This is not a number. Please enter a valid number")

        # Checks if player has won the game. Two different print outputs
        # depending on the game that has been selected.
        if winner(grid, player_symbol):
            print_grid()
            if game_level == 1:
                print("You win! Congratulations")
                return_to_menu()
            elif game_level == 2:
                print("Player one wins! Congratulations")
                return_to_menu()
            else:
                return None

        print_grid()
        # Checks if the grid is full. If yes then prints out message and
        # calls function return_to_menu to let user choose if he wants
        # to quit the script or go back to menu.
        if draw(grid):
            print("It's a draw!")
            return_to_menu()

        # Check if the game level is vs computer. If yes then generates
        # a random computer move and sets that grid to computers symbol.
        if game_level == 1:
            choice = computer_move(grid, opponent_symbol)
            grid[choice] = opponent_symbol

            # Checks for computer win same as previously for player.
            if winner(grid, opponent_symbol):
                print_grid()
                print("Computer wins!")
                return_to_menu()

            # Checks for a draw as the player above.
            if draw(grid):
                print("It's a draw!")
                return_to_menu()

        # Checks if the game level is against another player.
        if game_level == 2:
            # Main 2nd player loop that asks for a grid input to place
            # correct symbol onto grid. Same function as the main player
            while True:
                try:
                    choice = int(input(f"Please choose an empty space for for "
                                       f"your next move as "
                                       f"'{opponent_symbol}'.\n"))
                    if choice in range(1, 10):
                        if grid[choice] == " ":
                            grid[choice] = opponent_symbol
                            break
                        else:
                            print("Ups, that space is taken!")
                    else:
                        print("Wrong number. Please use the numbers "
                              "between 1-9.\n")
                except ValueError:
                    print("This is not a number. Please enter a valid number")

            # Checks for 2nd player win.
            if winner(grid, opponent_symbol):
                print_grid()
                print(f"Player two '{opponent_symbol}' wins! Congratulations")
                return_to_menu()

            print_grid()

            # Checks for a draw.
            if draw(grid):
                print("It's a draw!")
                return_to_menu()


def return_to_menu():
    """
    An input user gets asked when the game has ended. Either go back to
    main menu or quit the script.
    """
    choice = input("Would you like to return to main menu? "
                   "Type '1' if yes or type '2' to quit.\n")
    if choice == "1":
        reset_grid()
        main()
    elif choice == "2":
        quit()
    else:
        print("Invalid input. Please enter a valid number")


main()
