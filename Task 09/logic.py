print("This is the One Question Quiz\n")

while True:
    contestant = input("Contestant - What is your name? ")

    if contestant.isalpha():
        name = contestant
        print(f"Welcome {name.title()}!\n")
        break
    else:
        print("Letters only please!")
        continue

print("Right... Now this is where it gets serious.")
print("Let's give you your question.\n")

while True:
    user_answer = input(
        "From which university was Cogrammer originally launched back in 2012?\n"
        "A. Harvard University\n"
        "B. Oxford University\n"
        "C. Princeton University\n"
        "D. Cambridge University\n"
    )

    if user_answer.casefold() == "a" or user_answer.casefold() == "harvard university":
        print("Unfortunately, that is an incorrect answer. Better luck next time!")
        break

    elif user_answer.casefold() == "b" or user_answer.casefold() == "oxford university":
        print("Unfortunately, that is an incorrect answer. Better luck next time!")
        break

    elif (
        user_answer.casefold() == "c"
        or user_answer.casefold() == "princeton university"
    ):
        print(f"Congratulations {name.title()}! That is the correct answer.")
        print("Please receive your prize of $1,000,000")
        break

    elif (
        user_answer.casefold() == "d"
        or user_answer.casefold() == "cambridge university"
    ):
        print("Unfortunately, that is an incorrect answer. Better luck next time!")
        break

    else:
        print("Please choose one of the options.\n")
