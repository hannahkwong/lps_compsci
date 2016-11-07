print("How many miles away do you live from Richmond State?")
miles = int(raw_input())

print("What is your GPA?")
gpa = float(raw_input())

print("What is your ACT score?")
act = int(raw_input())

if miles <= 30 and gpa >= 2.0:
	print("Congratulations, you have been accepted! :D")
elif miles > 30 and gpa >= 2.5 and act >= 18:
	print("Congratulations, you have been accepted! :D")
elif act > 32:
	print("You are a liar, the highest score on the ACT is 32.")
else:
	print("Sorry, you have not been accepted :(")

