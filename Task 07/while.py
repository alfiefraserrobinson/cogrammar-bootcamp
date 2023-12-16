# define main function
def main():
    # create a empty list to store the input numbers
    numbers = []
    # create a loop
    while True:
        user_input = input("Enter a number (or -1 to stop): ")
        # close the loop if user enters "-1"
        if user_input == "-1":
            break
        # use 'try' to convert the input numbers to integers and add to the list
        try:
            number = int(user_input)
            numbers.append(number)
        # use 'except' if conversion fails to raise a 'ValueError'
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # use 'if' to see if there are any numbers added to the list
    if numbers:
        # if True then create a variable to store the average
        # use 'sum()' function to add together all the numbers in list
        # use 'len()' function to count how many individual numbers are stored in the list
        # use sum(numbers) / len(numbers) equation to find out average
        average = sum(numbers) / len(numbers)
        print(f"The average of the entered numbers (excluding -1) is: {average}")
    else:
        # if numbers is False (no numbers were entered) - print this to the user
        print("No numbers were entered.")


# ensures the main program is being run
if __name__ == "__main__":
    main()
