# Rachel Pinkney
# Program takes input on team names, randomly generate scores,
# reaturns the scores for each game, number of wins vs loses, 
# and a statment about the season

import random

#initializing counter variables to 0
numWin = 0
numLose = 0
gameDictionary = {}

#takes input on home team and number of games
teamName = input("Enter the name of your team(the home team): ")
numGames = int(input("\nEnter the number of games that " + teamName + " will play(1-10): "))
print("\n")

#create dictionary to store teams and scores
gameDictionary[teamName] = []

#saves information on other teams and their scores in a dictionary
for count in range(0, numGames):
    awayName = input("Enter the name of the away team for game " + str(count + 1) + ": ")
    
    homeScore = 0
    awayScore = 0
    
    while homeScore == awayScore:

        #randomly generate score for the teams
        homeScore = random.randint(0, 10)
        awayScore = random.randint(0, 10)

        #keeps track of games won and lost
        if homeScore > awayScore:
            numWin += 1
        elif homeScore < awayScore:
            numLose += 1

    gameDictionary[teamName].append([homeScore, awayName, awayScore])    

#prints the scores and teams for each game
print("\n")
for count in range(0, numGames):
    print("BYU's score: " + str(gameDictionary[teamName][count][0]) + " " + str(gameDictionary[teamName][count][1]) + "'s score: " + str(gameDictionary[teamName][count][2]))

#prints a phrase depending on percentage of games won by home team
print("\nFinal season record: " + teamName + " " + str(numWin) + " - " + str(numLose))
if numGames > 0:
    scorePercentage = numWin/(numGames)
    if scorePercentage >= 0.75:
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif scorePercentage >= 0.5:
        print("You had a good season ")
    else:
        print("Your team needs to practice!") 