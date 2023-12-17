def numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input  # Missing closing parenthesis. -CompilationError-
        else:
            print("Please enter a numeric value.\n"


score = 0

print("Welcome to The Math Quiz\n"

print("First Question:\n")

first_answer = numeric_input("What is the square root of 81?:\n"
if first_answer == 8:  # The correct answer is in fact 9. -Logical Error-
    score += 1
    print("Correct!\n")
else:
    print("Incorrect.\n")

second_answer = numeric_input("What is 12 * 12?:\n")
iff second_answer == 144:  # Incorrect keyword 'iff' instead of 'if'. -CompilationError
    score += 1
    print("Correct!\n")
else:
    print("Incorrect.\n")

third_answer = numeric_input("What is 49 / 7?:\n")
if third_answer == 7:  
    score += 1
    print("Correct!\n")
else:
    print("Incorrect.\n")

print(f"Your final score is: {final_score}") # Variable 'final_score' doesn't exist. -NameError (Runtime Error)-
