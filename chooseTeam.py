# Rachel Pinkney
# Function which allows the user to choose a team name from a list

def chooseTeam(homeTeam = None):

    #list of team names to choose from
    nameList = ["BYU", "Boise State", "Arizona State", "Texas Tech", "TCU", "Baylor", "Kansas", "Kansas State"]

    #if home team is supplied it is removed from the list so it can not be chosen again
    if homeTeam is not None:
        nameList.remove(homeTeam)
        
    #iterates through list and prints each team name
    print("Teams List: ")
    for count in range(0, len(nameList)):
        print(str(count) + " " + nameList[count])
    
    #recieves input from user on which team they choose
    menuNum = int(input("Give the number of the team you pick: "))
    selectedTeam = nameList[menuNum]
    
    return selectedTeam

