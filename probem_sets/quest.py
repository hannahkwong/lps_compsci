#Introducing the game and the user 
print("Welcome to your quest!")
print("What is your character's name?")
name = raw_input()

#Letting the user choose how much strength they want between the numbers 1-10
print("Enter strength" + "(1-10)") 
strength = int(raw_input())

#Same as strengrh, but with health instead 
print("Enter health" + "(1-10)")
health = int(raw_input())

#Just asking for their luck 
print("Enter luck" + "(1-10)")
luck = int(raw_input())

#Adding up their strength, health and luck together 
points = int(strength + health + luck) 

#After adding up their points, they have to have the total be 15 or below 
if points <= 15:
	print(str(name) + " " +  "strength =" + str(strength) + " " +  "health =" + str(health) + " " + "luck =" + str(luck))
elif points > 15:
	print("You have given your character too many points! Default values have been assigned," + str(name) + "strength = 5 health = 5 luck = 5")

#They come across a fork in the road and have to choose whether to go left or right 
print( str(name) + ", you've come to a fork in the road. Do you want to go left or right")
print("Enter 'right' or 'left'") 
fork = raw_input()

#This is what happens when they go right, they either die and lose or win the game 
if fork == 'right' and health <= 6:
	print("You have come across a unicorn, but your health wasn't high enough so you get stabbed in the heart and die. You lost the game.")  
elif fork == 'right' and health > 6:
	print("Congratulations! You have won the game!") 

#This is what happens when they go left
if fork == 'left' and strength <= 6:
	print("You went on a date with a skeleton, however, you strength was too low so your heart couldn't take take it. You have died and lost the game.")
elif fork == 'left' and strength > 6:
	print("You went on a date with a skeleton, you and the skeleton really hit it off! It has spared you and you have won the game, congratulations!")
