# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print(
    "Welcome to the error program"
)  # SYNTAX ERROR - Missing parentheses. Added parentheses to correct error.
print(
    "\n"
)  ## SYNTAX ERROR ## - Missing parentheses. Added parentheses to correct error. ## SYNTAX ERROR ## Unecessary indentation causing inconsistency.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"  ## RUNTIME ERROR ## - 'age_Str' is not defined as a variable due to a comparison operator being used ('==') instead of an assignment operator ('='). ## SYNTAX ERROR ## Unecessary indentation causing inconsistency.
age = int(
    age_Str
)  ## RUNTIME ERROR ## - The assigned value to 'age_Str' is not compatible with the 'int' function due to there being letters as well as numbers. Thus the conversion to an integer fails. ## SYNTAX ERROR ## Unecessary indentation causing inconsistency.
print(
    "I'm " + str(age) + " " + "years old."
)  ## RUNTIME ERROR# - The error within the 'print' function is due to the attempt to concatenate a string with an integer and not first converting the integer to a string. Added a space after '"I'm"' for readability purposes. ## SYNTAX ERROR ## Unecessary indentation causing inconsistency.

# Variables declaring additional years and printing the total years of age
years_from_now = float(
    "3.5"
)  ## RUNTIME ERROR ## - Failure to use 'float' function to convert string to a floating number. ## SYNTAX ERROR ## Unecessary indentation causing inconsistency.
total_years = (
    age + years_from_now
)  # RUNTIME ERROR ## - Unsupported operand type '+' due to the 'years_from_now' variable not being converted to an integer. ## SYNTAX ERROR ## Unecessary indentation causing inconsistency.

print(
    "The total number of years: " + str(total_years)
)  ## SYNTAX ERROR ## - Missing parentheses after the 'print' function and failing to contain the string. ## RUNTTIME ERROR ## - 'answer_years is an undefined variable due to a typo. ## LOGICAL ERROR ##  The 'answer_years' variable is inside quotation marks within the print function's string. Thus it not being defined as a variable but instead as characters within a string. ## RUNTIME ERROR ## 'answer_years' variable is missing the 'str' function for the conversion to a string.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (
    total_years * 12
)  ## RUNTIME ERROR ## - 'total' is not a defined variable.
total_months = int(
    total_months
)  # Not necessarily an error, but I addded the conversion of 'total_months' from a floating number to an integer, just to remove the '0' from the answer.

print(
    "In 3 years and 6 months, I'll be " + str(total_months) + " months old"
)  ## SYNTAX ERROR ## - Missing parentheses after the 'print' function and failing to contain the string. ## RUNTIME ERROR ## -  'total_months' variable is missing the 'str' function for the conversion to a string.

# HINT, 330 months is the correct answer
