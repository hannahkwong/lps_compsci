fave = 9

print("What do you think is my favorite number?")

your_guess = int(raw_input())

if your_guess < fave:
	print("Sorry, you lose. :(")
	print("Try again: next time try a higher guess.")
	print("what is 3 squared?") 
if your_guess > fave:
	print("Sorry, you lose. :(")
	print("Try again: next time, try a lower guess.")
	print("What is the square root of 81?")
if your_guess == fave:
	print("Wow, you guessed it! You must be a genius.") 
