# This is welcoming the user and asking the user to input their first line of their haiku
print("Welcome to the haiku generator!" + "\n")
print("Provide the first line of your haiku: ") 
firstLine = raw_input()

#This is asking the user for the second line and the user types it in 
print("Provide the second line of your haiku: ") 
secondLine = raw_input()

# This is asking the user for the final line and the user types it in 
print("Provide the third line of your haiku: ") 
thirdLine = raw_input() 

#This is asking the user they want to name the file that their haiku will be saved in 
print("What file would you like to write your haiku to? Add the .txt to the end of the name. ") 
myFile = raw_input()  

#This opens the file the user created and writes it out 
createdHaiku = open((myFile), "w")

#This is printing the user's haiku on 3 different lines 
createdHaiku.write(firstLine + "\n" + secondLine + "\n" + thirdLine + "\n") 

print("Done! To view your haiku, type 'cat' and the name of your file to the command line. ")
#This closes the file so it doesn't run forever 
createdHaiku.close()
