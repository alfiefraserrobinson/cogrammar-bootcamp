while True: #this is to create an indefinite loop until the conditions are met#
    age_input = input("How old are you?" + ' ') #use input function to store user's input into a variable#
    if age_input.isdigit(): #use 'is.digit' method to ensure user's input only contains digits#
        age = int(age_input) #if the result of 'is.digit' returns 'True' then use 'int' function to convert number into an integer and store in new variable#
        if age >= 100: #check if user's input is equal to or greater than 100#
            print("Sorry, you're dead.") #if true then return this print#
        elif age >= 65: #check if user's input is equal to or greater than 65#
            print("Enjoy your retirement.") #if true then return this print#
        elif age >= 40: #check if user's input is equal to or greater than 40#
            print("You're over the hill.") #if true then return this print#
        elif age == 21: #check if user's input is equal to 21#
            print("Congrats on your 21st.") #if true then return this print#
        elif age <= 13: #check if user's input is equal to or less than 13#
            print("You qualify for the kiddy discount") #if True then return this print#
        else:
            print("Age is but a number.") #if user's input doesn't fall under any of the previous syntax - print this#

        break #this breaks the loops once the conditions are met#

    else:
        print("Invalid input. Please enter a numeric value.") #if the user's input is anything but a numeric value - print this#
