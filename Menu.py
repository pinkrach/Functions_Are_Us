# Gavin Smith
# Display of menu and return choice. Store in variable and use this value to determine which function to call next.

# what needs to go in the menu?
'''
Choose your team
Choose the opponent's team
Play again
Quit
'''

import time

def menu() :
    # bring up an option menu of things you can do in the game
    
    bContMenu = True # set up a variable that controls the loop

    while bContMenu == True :
        print( "\nOptions:" # print this menu every time there's an invalid input, so include it in the loop
            "\n1. Play the game"
            "\n2. Choose your team"
            "\n3. Choose the opposing team"
            "\n4. Play again with current teams"
            "\n5. Quit"
        )

        try : # use a try-except to account for non-numeric inputs from the user
            menuChoice = int(input("\nWhat would you like to do? "))

            if menuChoice in range(1,6) : # If the user input is in the valid range, end the loop
                bContMenu = False
            else: # if the number the user inputs isn't a menu option, print a message and run the loop again.
                print("\nPlease input number from the menu!")
                time.sleep(.5) # include a small delay between an invalid input and reprinting the menu

        except ValueError: # print an error message if the user input isn't a number
            print("\nPlease input number from the menu!")
            time.sleep(.5) # include a small delay between an invalid input and reprinting the menu

    return menuChoice # return the user's choice as a number and use that number to determine what function is called next

menuChoice = menu()
print(menuChoice) # remove this line in the final code. I put it in as a way to verify that the function is working