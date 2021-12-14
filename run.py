# Variable 'grid' that is a list of empty strings to create grid.
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


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


main()
