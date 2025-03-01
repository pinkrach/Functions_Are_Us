'''Mason Zarges
    Program takes input on team names, randomly generate scores,
    reaturns the scores for each game, the shows the whether is was a win or loss,'''
import random
# 4 Play the game receiving both team names. Generate random scores without ties. Return W or L.

def playGame(homeName, awayName):
    homeScore = 0
    awayScore = 0
    
    while homeScore == awayScore:
        homeScore = random.randint(0, 10)
        awayScore = random.randint(0, 10)
        
    if homeScore > awayScore:
        return "W"
    else:
        return "L"
    
    

