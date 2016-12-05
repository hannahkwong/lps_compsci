# put this line at the start of your program
import random 
myNum = random.randint(1, 1000)
print("I'm thinking of a number between 1 and 1000. Enter your guess!")
num = int(raw_input())

while num != myNum:
	if num > myNum:
		print("Nope, too high! Guess again.")
		num = int(raw_input())
	if num < myNum:
		print("Nope, too low! Guess again.")
		num = int(raw_input())
	if num == myNum:
		break
if num == myNum:
	print("Hooray, you won!") 
