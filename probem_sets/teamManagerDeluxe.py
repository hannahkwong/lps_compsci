class soccerTeam(object):

	def __init__(self, name, age, goals, jersey, position): 
		self.name = name 
		self.age =age 
		self.goals = goals 
		self.jersey = jersey 
		self.position = position 
    
	def getStats(self):
		summary = "Name: " + self.name + "\n" 
		summary = summary + "Age: " + self.age + "\n"
    		summary = summary + "Goals: " + self.goals + "\n" 
		summary = summary + "Jersey Number: " + self.jersey + "\n"
		summary = summary + "Position: " + self.position + "\n" 
    		return summary 
    
team = []

tom2 = True 

while tom2:
	print("Welcome to Team Manager Deluxe!")
	print("Do you want to start with a new team or open an existing team?")
	print("What would you like to do? Enter your choice: ")
	print("(1) Start with a new team")
	print("(2) Print all players")
	print("(3) Save your player list to a file")
	print("(0) Leave the program (save first to avoid losing your data!)") 
 
	choice = raw_input()
	
	if choice == "0":
		tom2 = False 
    
  	elif choice == "1":
    		print("Enter player name")
    		playerName = raw_input()
    		print("Enter age")
    		playerAge = raw_input()
    		print("Enter number of goals scored this season")
   		playerGoals = raw_input()
		print("Enter the jersey number")
		playerJersey = raw_input()
		print("Enter the position")
		playerPosition = raw_input()
    
	userPlayer = soccerTeam(playerName, playerAge, playerGoals, playerJersey, playerPosition)
    
	team.append(userPlayer)
     
  	if choice == "2":
    		for m in team:
      			print(m.getStats())

    
	elif choice == "3":
		print("Where do you like to save your players? Enter a file name, we'll add the '.txt' for you.") 
		user_file = raw_input()
		saveTeam(players, user_file) 


def saveTeam(playerList, filename):
	myFile = open(filename + ".txt", "w") 
	for p in playersList:
		myFile.write(playerName + " " 
			+ str(playerAge) + " " 
			+ str(playerGoals) + " " 
			+ str(playerJersey) + " " 
			+ playerPosition + "\n" 

	myFile.close()
	
		
def loadTeam(filename):
	myList = [] 
	the_file = open((filename), "r")
	line = the_file.readline() 
	while line:
		player = line.split()
		myList.append(Player(player[0],player[1],player[2],player[3],player[4]))
		line = the_file.readline()


	the_file.close() 

	print(the_list)
	return myList
