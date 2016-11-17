print("For what number would you like multiples?") 
my_num = int(raw_input())
num = 0 
multiples = float(my_num * num)  

while multiples < 1000:
	print(str(num) + " "  + "times" + " " +  str(my_num) + " "  + "equals" + " " + str(multiples)) 
	num = num + 1 
	multiples = float(my_num * num) 
print("Those are all of the multiples of" + " " + str(my_num) + ", thank you for existing!")
