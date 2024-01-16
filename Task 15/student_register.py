# 'input' to ask for number of students registering. Then converting that string to an integer.
student_numbers = int(input("How many students are registering?\n"))

# 'for' loop created to iterate 'student_numbers'.
for student in range(student_numbers):
    # Each iteration asks for the student id.
    student_id = input("What is the student I.D?\n")
    # Creates a new file called 'reg_form.txt in append mode, allowing data to be added to the file without previsou data being overwritten.
    with open("reg_form.txt", "a") as file:
        # Writes the 'student_id' string to the file
        file.write(student_id)
        # Writes a string to the file containing several dots, for the use of signatures.#
        file.write("\n............\n")

# To inform the user that all students have been registered.
print("All students have been registered.")
