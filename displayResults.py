# Spencer Bigelow
# Display the final record for a team. 
# Receive the home team data and display information.

# Making the function that will print out the results and name of home team.
def displayResult(homeTeam, numWin, numLose) :

    print(f"{homeTeam}'s Final Record: wins - {numWin} losses - {numLose}")

    #prints a statement based on the team performance
    if (numWin + numLose) > 0:
        scorePercentage = numWin/(numWin + numLose)
        if scorePercentage >= 0.75:
            print("You qualified for the NCAA Women's Soccer Tournament")
        elif scorePercentage >= 0.5:
            print("You had a good season ")
        else:
            print("Your team needs to practice!") 


    return 

