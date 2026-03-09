# Women's Soccer Season Simulaton
# Team Members:
# Bryce Flindt Function 1 and 2
# Luke Lee Function 5
# Jordan Function 3
# Luke G Function 4


# Function: introduction
# This function explains the rules of the game,
# asks the player for their name, and returns it to the main program.
def introduction():
    print("Welcome to the Women's Soccer Season Simulator!")
    print()
    print("Rules of the Game:")
    print("- You will choose a home team.")
    print("- You will play several games against opponents.")
    print("- Scores will be randomly generated.")
    print("- Ties are not allowed.")
    print()
# Ask the player for their name
    sPlayerName = input("Enter your name: ")
# Welcome message
    print()
    print("Welcome, " + sPlayerName + "! Let's play soccer.")
    print()
# Return the name so main() can use it
    return sPlayerName
def display_menu():

    print("Main Menu")
    print("1 - Play Season")
    print("2 - Display Record")
    print("3 - Quit")
    print()

    # Get the user's choice
    sChoice = input("Enter your choice (1-3): ")

    # Return the choice to the main program
    return sChoice
# My Test For the functions
# sPlayerName = introduction()
# sChoice = display_menu()
# print("Player name is:", sPlayerName)
# print("Menu choice is:", sChoice)