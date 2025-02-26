# Rachel Pinkney
# Function which allows the user to choose a team name from a list

teamNamesList = ["BYU", "Boise State", "Arizona State", "Texas Tech", "TCU", "Baylor", "Kansas", "Kansas State"]

def chooseTeam(nameList = None):
    if len(nameList) is 0:
        print("There are no teams available to be chosen from at this moment. Please try again. ")

    #gives a default list of names if none is provided
    if nameList is None:
        nameList = ["BYU", "Boise State", "Arizona State", "Texas Tech", "TCU", "Baylor", "Kansas", "Kansas State"]

    #iterates through list and prints each team name
    print("Teams List: ")
    for count in range(0, len(nameList)):
        print(str(count) + " " + teamNamesList[count])
    
    #recieves input from user on which team they choose
    menuNum = int(input("Give the number of the team you pick: "))
    selectedTeam = nameList[menuNum]

    #removes selected team from list
    nameList.pop(menuNum)
    
    return selectedTeam

