fave = 9

print("What do you think is my favorite number?") 
your_guess = int(raw_input())

if your_guess > fave:
	print("Sorry, you lose. :(")  
if your_guess <= fave:
	print("Hooray, you won! Good choice.")
