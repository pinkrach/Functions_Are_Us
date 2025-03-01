# Rachel Pinkney
# Function which allows the user to choose a team name from a list

import time

def chooseTeam(homeTeam = None):

    #list of team names to choose from
    nameList = ["BYU", "Boise State", "Arizona State", "Texas Tech", "TCU", "Baylor", "Kansas", "Kansas State"]
    
    #if home team is supplied it is removed from the list so it can not be chosen again
    if homeTeam is not None:
        nameList.remove(homeTeam)
    
    bCont = True # set up a variable that controls the loop

    while bCont == True :
        
        #iterates through list and prints each team name
        print("Teams List: ")
        for count in range(0, len(nameList)):
            print(str(count) + " " + nameList[count])

        try : # use a try-except to account for non-numeric inputs from the user
                #recieves input from user on which team they choose
                menuNum = int(input("Give the number of the team you pick: "))

                if menuNum in range(0,len(nameList)) : # If the user input is in the valid range, end the loop
                    bCont = False
                else: # if the number the user inputs isn't a menu option, print a message and run the loop again.
                    print("\nPlease input a number from the list!")
                    time.sleep(.5) # include a small delay between an invalid input and reprinting the menu

        except ValueError: # print an error message if the user input isn't a number
            print("\nPlease input number from the menu!")
            time.sleep(.5) # include a small delay between an invalid input and reprinting the menu

    selectedTeam = nameList[menuNum]
    
    return selectedTeam

