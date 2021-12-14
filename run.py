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
        user_choice = int(input())
        if user_choice == 1:
            game_type()
        elif user_choice == 2:
            print_grid()
        else:
            print("Wrong input. Please use the numbers '1' or '2'.")


def game_type():
    """
    Let's user select which game he/she wants to play depending if it's
    against computer or 2nd player.
    """
    print("1. Play the game against computer.")
    print("2. Play the game against your friend.")
    while True:
        user_choice = int(input())
        if user_choice == 1:
            game_level = 1
            play_game()
        elif user_choice == 2:
            game_level = 2
            play_game()
        else:
            print("Wrong input. Please use the numbers '1' or '2'.")


def play_game():
    """
    The main game function that gets executed after all previous options
    gets put through.
    """
    # Let's user select the symbol he/she wants to play as. Either 'X'
    # or 'O'. Prints out to user message that wrong symbol has been
    # chosen, if so restarts the game.
    print(f"Do you want to play as a '{symbol[0]}' or an '{symbol[1]}?' \n")
    player_symbol = str(input())
    if player_symbol == symbol[0]:
        print('you have chosen x')
    elif player_symbol == symbol[1]:
        print('you have chosen o')
    else:
        print("Wrong symbol, please use either 'X' or 'O'.\n")
        play_game()
    # The main game loop
    while True:
        print_grid()
        # The main player loop that loops through input.
        while True:
            choice = int(input(f"Please choose an empty space for for "
                               f"your next move as '{player_symbol}'."))
            if choice in range(1, 10):
                if grid[choice] == " ":
                    grid[choice] = player_symbol
                else:
                    print("Ups, that space is taken!")
            else:
                print("Wrong input. Please use the numbers "
                      "between 1-9.\n")
            print_grid()


main()
