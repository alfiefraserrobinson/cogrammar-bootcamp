# Used to open the file
with open("DOB.txt") as file:
    # Created lists to store names and birthdates
    names = []
    birthdates = []

    # For loop to iterate over the lines in the file
    for line in file:
        # Splits the line parts based on spaces
        line_parts = line.split()
        # Joins all parts except the last three, assuming these parts constitute the name
        name = " ".join(line_parts[:-3])
        birthdate = " ".join(line_parts[-3:])
        # Add processed lines to lists made earlier
        names.append(name)
        birthdates.append(birthdate)

# Print all iterated lines from 'names' list
print("**Name**")
for name in names:
    print(name)

# Print all iterated lines from 'birthdates' list
print("\n**Birthdate**")
for birthdate in birthdates:
    print(birthdate)
