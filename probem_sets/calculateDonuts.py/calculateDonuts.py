print("How many people will you have at the party?") 
people = raw_input()

print("How many donuts will you have at the party?") 
donuts = raw_input()

print("Out party has" + str(people) + "people and" + str(donuts) + "donuts.") 
total = (int(donuts) / int(people)) 

print("Each person at the party gets" + str(total) + "donuts.") 
