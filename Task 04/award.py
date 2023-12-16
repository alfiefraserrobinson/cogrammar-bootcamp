name = input("What is your name?" + ' ')

while True:
    swimming_input = input("What is your swimming time (in minutes)?:" + ' ')
    if swimming_input.isdigit():
        swimming_time = int(swimming_input)  #created a loop requesting swimming time in minutes until returned as True#
        break                                #once the minutes were input by the user, i created a new variable to store the recently converted integer#
                                             #if user input was anything other than a numeric value it would return as false and request the input again#
    else:
        print("Please enter a numeric value.")

while True:
    cycling_input = input("What is your cycling time (in minutes)?:" + ' ')
    if cycling_input.isdigit():
        cycling_time = int(cycling_input) #same as above#
        break
    else:
        print("Please enter a numeric value.")

while True:
    running_input = input("What is your running time (in minutes)?:" + ' ')
    if running_input.isdigit():
        running_time = int(running_input) #same as above#
        break
    else:
        print("Please enter a numeric value.")

total_time = swimming_time + cycling_time + running_time #created a variable from the result of adding all of the user's input's together to get the total amount of minutes#
if total_time in range(0, 100):  #checks if total_time variable falls within this range and if so - gives the relative reward#
    print(f"Congratulations {name}! You qualified and have been awarded Provincial Colours!")
elif total_time in range(101, 105):
    print(f"Congratulations {name}! You qualified and have been awarded Provincial Half Colours!")
elif total_time in range(106, 110):
    print(f"Congratulations {name}! You qualified and have been awarded Provincial Scroll!")
else:
    print("Unfortunately, you didn't qualify. Better luck next time!") #if total_time doesn't fall within any of those ranges then this print() is returned#