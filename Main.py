# Import functions from Soccer.py
from Soccer import introduction, display_menu, display_record
import random

def play_game(sHomeTeam, sOpponentTeam):
    iHomeScore = random.randint(0, 5)
    iOpponentScore = random.randint(0, 5)
    
    while iHomeScore == iOpponentScore:
        iOpponentScore = random.randint(0, 5)
    
    print()
    print(f"{sHomeTeam} vs {sOpponentTeam}")
    print(f"Final Score: {sHomeTeam} {iHomeScore} - {iOpponentScore} {sOpponentTeam}")
    
    if iHomeScore > iOpponentScore:
        print(f"{sHomeTeam} wins!")
        return "W"
    else:
        print(f"{sOpponentTeam} wins!")
        return "L"

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
