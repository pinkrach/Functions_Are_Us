# Sabrina Wong
# Main Function to run the game

from intro import introduction
from chooseTeam import *
from Menu import *
from masonsfunction import *

def main():
    # Start the game by calling the introduction function
    name = introduction() 
    
    # to keep track of the team's win/loss record
    record = []
    
    numWins = 0
    numLosses = 0
    gamesCount = 0
    homeTeam = None
    oppTeam = None
    bCont = True

    while bCont is True:
        # Display the menu and get the user's choice
        menuChoice = menu()

        # Start the game by choosing home team
        if menuChoice == 1: 
            print(f"Choose your home team from the list ")
            homeTeam = chooseTeam(homeTeam=None)
            print(f"{homeTeam} is {name}'s home team.")
            
        # Choose the opposing Team and play the game
        if menuChoice == 2:  
            if homeTeam:
                print(f"Choose the opposing team from the list ")
                oppTeam = chooseTeam(homeTeam=homeTeam) 
                print(f"{oppTeam} is the opposing team.")

                # Play the game and record results
                result = playGame(homeTeam, oppTeam)
                if result == "W":
                    print(f"{homeTeam} wins!")
                    numWins += 1
                else:
                    print(f"{homeTeam} loses.")
                    numLosses += 1

                record.append(f"{homeTeam} vs {oppTeam}: {result}")
                print(record[0])

                gamesCount = gamesCount + 1 
            
            else:
                print("You need to choose your home team first.")

        
        elif menuChoice == 3: # Print current record
            print(f"Current Record for {name}: {numWins} Wins - {numLosses} Losses")
            
        # Print history of games played
        elif menuChoice == 4:
            for count in range(0, gamesCount):
                print(record[count])

        # Quit the game
        elif menuChoice == 5:  
            print("Thanks for playing! Goodbye.")
            
            # Display the final record
            print(f"Final Record for {name}: {numWins} Wins - {numLosses} Losses")
            
            #prints a statement based on the team performance
            if (numWins + numLosses) > 0:
                scorePercentage = numWins/(numWins + numLosses)
                if scorePercentage >= 0.75:
                    print("You qualified for the NCAA Women's Soccer Tournament")
                elif scorePercentage >= 0.5:
                    print("You had a good season ")
                else:
                    print("Your team needs to practice!") 

            #exist menu
            bCont = False

