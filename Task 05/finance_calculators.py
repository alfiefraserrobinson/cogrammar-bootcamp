import math
import sys


# function to ensure numeric input
def numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a (whole) number.")


# function to calculate simple interest
def simple_interest_calc(deposit, rate, time):
    # convert rate to decimal
    r = rate / 100
    return deposit * (1 + r * time)


# function to calculate compound interest
def compound_interest_calc(deposit, rate, time):
    r = rate / 100
    return deposit * math.pow((1 + r), time)


# function to calculate monthly bond repayment
def bond_repayment_calc(house_value, rate, time):
    monthly_interest_rate = (rate / 100) / 12
    total_payments = time

    return (monthly_interest_rate * house_value) / (
        1 - math.pow(1 + monthly_interest_rate, -total_payments)
    )


# main function that executes the program
def main():
    while True:
        print(
            "investment - to calculate the amount of interest you'll earn on your investment."
        )
        print(
            "bond       - to calculate the amount you'll have to pay on a home loan.\n"
        )

        # get the user's option of 'investment or 'bond
        option = input("Enter either 'investment' or 'bond'. ").casefold()

        # if user chooses 'investment' - get details from the user
        if option == "investment":
            deposit = numeric_input("How much money are you depositing? ")
            rate = numeric_input("How much is the interest rate? ")
            time = numeric_input("How many years do you plan on investing? ")

            while True:
                type_of_interest = input(
                    "Which type of interest would you prefer = 'simple' or 'compound'? "
                ).casefold()
                if type_of_interest == "simple":
                    interest = simple_interest_calc(deposit, rate, time)
                    print(
                        f"\nYour {type_of_interest} interest after {time} years will be: {interest:.2f}"  # used format method '.2f'to format the floating-point number to 2 decimal places
                    )
                    sys.exit()  # exits the program
                elif type_of_interest == "compound":
                    interest = compound_interest_calc(deposit, rate, time)
                    print(
                        f"\nYour {type_of_interest} interest after {time} years will be: {interest:.2f}"
                    )
                    sys.exit()
                else:
                    print("Incorrect type. Please try again.\n")
                    continue

        # if user chooses 'bond' - get details from the user
        elif option == "bond":
            house_value = numeric_input("What is the current value of the house? ")
            rate = numeric_input("How much is the interest rate? e.g., 7: ")
            time = numeric_input(
                "How many months do you plan to take to repay the bond? "
            )
            # calculate and print the monthly bond repayment

            bond_repayment = bond_repayment_calc(house_value, rate, time)
            print(f"\nYour monthly bond repayment will be: {bond_repayment:.2f}")
            sys.exit()

        else:
            print("\nInvalid option. Please try again.\n")


# ensures the main program is being run
if __name__ == "__main__":
    main()
