# Sabrina Wong
# Main Function to run the game

def main():
    # Start the game by calling the introduction function
    name = introduction() 
    # to keep track of the team's win/loss record
    record= {}

    numWins = 0
    numLosses = 0
    homeTeam = None
    oppTeam = None

    while True:
        # Display the menu and get the user's choice
        menuChoice = menu()

        if menuChoice == 1:  # Play the game
            if homeTeam and oppTeam:
                result = play_game(homeTeam, oppTeam)
                if result == "W":
                    print(f"{homeTeam} wins!")
                    numWins += 1
                else:
                    print(f"{homeTeam} loses.")
                    numLosses += 1

        # Choose your team
        elif menuChoice == 2: 
            homeTeam = chooseTeam(homeTeam=None)
            print(f"{homeTeam} is your home team.")

        # Choose the opposing team
        elif menuChoice == 3:  
            if homeTeam:
                oppTeam = chooseTeam(homeTeam=homeTeam) 
                print(f"{oppTeam} is the opposing team.")
            else:
                print("You need to choose your home team first.")

        # Play again with current teams
        elif menuChoice == 4:  
            if homeTeam and oppTeam:
                result = play_game(homeTeam, oppTeam)
                if result == "W":
                    print(f"{homeTeam} wins!")
                    numWins += 1
                else:
                    print(f"{homeTeam} loses.")
                    numLosses += 1
            else:
                print("You need to choose both your home team and an opponent first.")

        # Quit the game
        elif menuChoice == 5:  
            print("Thanks for playing! Goodbye.")
            # Display the final record
            print(f"Final Record for {name}: {numWins} Wins - {numLosses} Losses")
            
