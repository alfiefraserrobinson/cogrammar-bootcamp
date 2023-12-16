# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# 'Lion is wrote as an undefined variable when it should be wrote as a string. -NameError-
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Missing 'f' to make this an f string.
# 'number_of_teeth' variable and 'animal_type' variable are misplaced within the string.
full_spec = (
    f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
)

# Missing parentheses after 'print' function and not containing the variable
print(full_spec)
