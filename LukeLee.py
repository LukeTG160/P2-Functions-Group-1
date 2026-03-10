#Function: Final Record [Luke Lee]
    #Display the final record for a team.
    #Receive the home team data and display information.

def display_record(sHomeTeam, iWins, iLosses):

    print()
    print("Season Record")
    print("----------------------")
    print("Team:", sHomeTeam)

    # Calculate total games played
    iTotalGames = iWins + iLosses

    print("Games Played:", iTotalGames)
    print("Wins:", iWins)
    print("Losses:", iLosses)

    # Calculate win percentage
    if iTotalGames > 0:
        fWinPercent = iWins / iTotalGames
        print("Win Percentage:", round(fWinPercent, 2))

    print("----------------------")
    print()