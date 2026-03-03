import random

# Inputs
sHomeTeam = input("Enter the name of your home team: ")
iNumGames = int(input("Enter the number of games that " + sHomeTeam + " will play: "))
print()
# Record keeping
iWins = 0
iLosses = 0
dResults = {
    "Won Against": [],
    "Lost Against": []
}
# Play games
for iGameNum in range(1, iNumGames + 1):
    sAwayTeam = input("Enter the name of the away team for game " + str(iGameNum) + ": ")

    iHomeScore = random.randint(0, 3)
    iAwayScore = random.randint(0, 3)
    # No ties allowed
    while iHomeScore == iAwayScore:
        iHomeScore = random.randint(0, 3)
        iAwayScore = random.randint(0, 3)
    # Win / loss tracking
    if iHomeScore > iAwayScore:
        iWins = iWins + 1
        dResults["Won Against"].append(sAwayTeam)
    else:
        iLosses = iLosses + 1
        dResults["Lost Against"].append(sAwayTeam)
    # Score output
    print(sHomeTeam + "'s score: " + str(iHomeScore) + " - " + sAwayTeam + "'s score: " + str(iAwayScore))
    print()
# Teams won against
print("Teams won against:")
for sTeam in dResults["Won Against"]:
    print("  " + sTeam)
print()
# Teams lost against
print("Teams lost against:")
for sTeam in dResults["Lost Against"]:
    print("  " + sTeam)
print()
# Final record
print("Final season record: " + str(iWins) + " - " + str(iLosses))
# Final message
fWinPct = iWins / iNumGames

if fWinPct >= 0.75:
    print("Qualified for the NCAA Soccer Tournament!")
elif fWinPct >= 0.50:
    print("You had a good season.")
else:
    print("Your team needs to practice!")
