# Variable 'grid' that is a list of empty strings to create grid.
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Print grid
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


print_grid()
