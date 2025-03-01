# Spencer Bigelow
# Display the final record for a team. 
# Receive the home team data and display information.

# Making the function that will print out the results and name of home team.
def displayResult(homeTeam, numWin, numLose) :
    print(f"{homeTeam} has {numWin} wins and {numLose}")
    return 

# Setting paramaters so i could test the funtion 
homeTeam = "BYU"
numWin = 20
numLose = 4

# Running function 
displayResult(homeTeam, numWin, numLose)