print("What is the amount of purchase, in dollars?") 
purchase = int(raw_input())

discount = int(purchase * .10)
final_purchase =int(purchase - discount) 

if int(purchase) > 10.00:
	print("You spent over $10! Your final price is" + "$" + str(final_purchase))
if int(purchase) <= 10.00:
	print("You did not spend over $10, your final price is still" + "$" + str(purchase))
