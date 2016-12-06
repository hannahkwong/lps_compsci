print("Welcome to PumaPix!")
print("Enter your 5 favorite TV shows.")
shows = 0 
all_shows = []

while shows < 5:
	print("Enter a show name:")
	show = raw_input()
	all_shows.append(show)
	shows = shows + 1 

print("Here is what you have entered:")
print(all_shows)
print("We've added a couple of important ones.")
all_shows.append("Breaking Bad")
all_shows.append("The Wire")

num = 0
for shows in all_shows:
        num = num + 1
        all_shows.sort()
        print(str(num) + ". " +  shows)
