# Import functions from Soccer.py
from Soccer import introduction, display_menu

def main():

    # Call introduction function (Bryce)
    sPlayerName = introduction()

    # Call menu function (Bryce)
    sChoice = display_menu()

    # Basic menu logic
    if sChoice == "1":
        print("Starting the season...")

    elif sChoice == "2":
        print("Displaying record...")

    elif sChoice == "3":
        print("Goodbye " + sPlayerName)


# Run the program
main()
