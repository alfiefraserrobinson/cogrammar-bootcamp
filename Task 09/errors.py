# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


# The parentheses after the function 'print' were missing and not containing the string. -SyntaxError-
print("Welcome to the error program")

# Again, the parentheses after the function 'print' were missing and not containing the string. -SyntaxError-
# Also, there is an indentation before the 'print' function creating an inconsistency from the previous statement. -IndentationError-
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result

# Unexpected indentation before both variables as well as 'print' function. -IndentationError-
# 'age_Str' is not defined as a variable due to a comparison operator being used ('==') instead of an assignment operator ('='). -NameError-
age_Str = "24"

# The assigned value to 'age_Str' is not compatible with the 'int' function due to there being letters as well as numbers. Thus the conversion to an integer fails. -ValueError-
age = int(age_Str)

# The error within the 'print' function is due to the attempt to concatenate a string with an integer and not first converting the integer to a string. -ValueError-
# Added a space after '"I'm"' for readability purposes.
print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age

# Unexpected indentation before both variables. -IndentationError-
# Failure to use 'float' function to convert string to a floating number. -ValueError-
years_from_now = float("3.5")
# Unsupported operand type '+' due to the 'years_from_now' variable not being converted to an integer. -TypeError-
total_years = age + years_from_now

# Missing parentheses after the 'print' function and failing to contain the string. -SyntaxError-
# 'answer_years is an undefined variable due to a typo. -NameError-
# The 'answer_years' variable is inside quotation marks within the print function's string. Thus it not being defined as a variable but instead as characters within a string.
# 'answer_years' variable is missing the 'str' function for the conversion to a string. -TypeError-
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result

# 'total' is not a defined variable. -NameError-
total_months = total_years * 12

# Not necessarily an error, but I addded the conversion of 'total_months' from a floating number to an integer, just to remove the '0' from the answer.
total_months = int(total_months)

# Missing parentheses after the 'print' function and failing to contain the string. -SyntaxError-
# 'total_months' variable is missing the 'str' function for the conversion to a string. -TypeError-
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

# HINT, 330 months is the correct answer
