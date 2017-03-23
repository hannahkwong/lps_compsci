phonebook = {}

tom = True
while tom == True:
        print("Welcome to Contacts!")
        print("What would you like to do?")
        print("(1) Add a phone number")
        print("(2) Print the full list of contacts")
        print("(3) Enter a name to retrieve that contact's phone number")
        print("(0) Exit Contacts app")

        response = raw_input()


        if response == "0":
                tom = False

        if response == "1":
                print("What's the name of your contact?")
                name = raw_input()
                print("What's the phone number of your contact?")
                number = raw_input()
                phonebook[name] = number

        if response == "2":
                print phonebook

        if response == "3":
                print("Who's number would you like?")
                contactName = raw_input()
                print("Okay, here's the number:")
                phonebook[name] = number
		print number 
