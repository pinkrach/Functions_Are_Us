# Karlie Ward

# Introduction to the game getting user's name, welcoming them, and giving them direction
# to play the game. Returns user's name for future use

def introduction():
    print(f"\nWOMEN'S SOCCER SEASON\n")
    print()
    iUserName = input("What is your name? ")
    print()
    print(f"Welcome {iUserName}! Let's play!")
    print("How to begin:\nChoose from the menu to play the game, choose your teams, play again, or quit.")

    return iUserName
