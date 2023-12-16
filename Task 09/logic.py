print("This is the One Question Quiz\n")

# Loop to get the contestant's name
while True:
    contestant = input("Contestant - What is your name? ")

    # Check if the name consists only of letters
    if contestant.isalpha():
        name = contestant
        # Greet the contestant and break the loop
        print(f"Welcome {name.title()}!\n")
        break
    else:
        # Prompt the user again if the input contains non-letter characters
        print("Letters only please!")
        continue

print("Right... Now this is where it gets serious.")
print("Let's give you your question.\n")

# Loop to get the contestant's answer to the quiz question
while True:
    user_answer = input(
        "From which university was Cogrammer originally launched back in 2012?\n"
        "A. Harvard University\n"
        "B. Oxford University\n"
        "C. Princeton University\n"
        "D. Cambridge University\n"
    )

    # Check if the user's answer is Harvard University (incorrect)
    if user_answer.casefold() == "a" or user_answer.casefold() == "harvard university":
        print("Unfortunately, that is an incorrect answer. Better luck next time!")
        break

    # Check if the user's answer is Oxford University (incorrect)
    elif user_answer.casefold() == "b" or user_answer.casefold() == "oxford university":
        print("Unfortunately, that is an incorrect answer. Better luck next time!")
        break

    # Check if the user's answer is Princeton University (correct)
    elif (
        user_answer.casefold() == "c"
        or user_answer.casefold() == "princeton university"
    ):
        print(f"Congratulations {name.title()}! That is the correct answer.")
        print("Please receive your prize of $1,000,000")
        break

    # Check if the user's answer is Cambridge University (incorrect)
    elif (
        user_answer.casefold() == "d"
        or user_answer.casefold() == "cambridge university"
    ):
        print("Unfortunately, that is an incorrect answer. Better luck next time!")
        break

    # Prompt the user to choose one of the options if the input doesn't match any case
    else:
        print("Please choose one of the options.\n")

    # The logical error in this code is that the correct answer to the question is actually Cambridge University. #
