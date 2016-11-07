print("What is the hour?") 
NewYorkHours = raw_input()

print("What are the minutes?") 
NewYorkMinutes = raw_input()

CaliforniaTime = int(NewYorkHours) + int(9)

print("If the time in New York is" + str(NewYorkHours) + ":" + str(NewYorkMinutes) + ",then the time in California is" + str(CaliforniaTime) + ":" +str(NewYorkMinutes))
