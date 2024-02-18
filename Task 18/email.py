# Define the Email class that will represent each email in our simulator.
class Email:
    # Constructor for the Email class, initializes each new Email object with specific attributes.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address  # The sender's email address.
        self.subject_line = subject_line  # The subject line of the email.
        self.email_content = email_content  # The body content of the email.
        self.has_been_read = (
            False  # Tracks whether the email has been read, starts off as unread.
        )

    # Method to mark an email as read, changing 'has_been_read' from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# List to store all email objects, acting as the inbox for our email simulator.
inbox = []


# Function to populate the inbox with a few starter emails.
def populate_inbox():
    # Add three predefined emails to the inbox to start with.
    inbox.append(
        Email("email1@example.com", "Welcome to HyperionDev!", "Content of email 1.")
    )
    inbox.append(
        Email(
            "email2@example.com", "Great work on the bootcamp!", "Content of email 2."
        )
    )
    inbox.append(
        Email("email3@example.com", "Your excellent marks!", "Content of email 3.")
    )


# Function to list all the emails in the inbox, showing their index and subject line.
def list_emails():
    for index, email in enumerate(inbox):
        # Print out each email's index and subject line for easy viewing.
        print(f"{index} {email.subject_line}")


# Function to read an email from the inbox based on its index.
def read_email(index):
    # Check if the provided index is within the range of the inbox list.
    if 0 <= index < len(inbox):
        # Access the email at the provided index.
        email = inbox[index]
        # Mark the email as read.
        email.mark_as_read()
        # Display the email's details: sender, subject, and content.
        print(
            f"\nEmail from {email.email_address}:\nSubject: {email.subject_line}\nContent: {email.email_content}\n"
        )
        print(f"Email from {email.email_address} marked as read.\n")
    else:
        # If the index is invalid (out of range), inform the user.
        print("Invalid email index.")


# Main part of the program.
populate_inbox()  # Start by populating the inbox with some initial emails.

# Loop to keep the program running.
while True:
    # Present the user with a menu of options to interact with the email simulator.
    user_choice = input(
        """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
    )

    # Check if the user's input is a digit and convert it to an integer.
    if user_choice.isdigit():
        user_choice = int(user_choice)
    else:
        # If the input isn't a number, prompt the user to enter a valid choice.
        print("Please enter a valid number.")
        continue

    if user_choice == 1:
        # Option to read a specific email from the inbox.
        list_emails()  # First, show all emails with their indices.
        try:
            # Ask the user to choose an email to read by entering its index.
            selected_email = int(
                input("Enter the number of the email you want to read: ")
            )
            # Call the function to display the chosen email.
            read_email(selected_email)
        except ValueError:
            # Handle cases where the user doesn't enter a number.
            print("Please enter a valid number.")

    elif user_choice == 2:
        # Option to view all unread emails in the inbox.
        print("\nUnread Emails:")
        for index, email in enumerate(inbox):
            # Only display emails that haven't been marked as read.
            if not email.has_been_read:
                print(f"{index} {email.subject_line}")

    elif user_choice == 3:
        # Option to quit the email simulator program.
        print("Quitting the application. Goodbye!")
        break  # Exit the loop, ending the program.

    else:
        # Handle cases where the user enters an option not on the menu.
        print("Oops - incorrect input.")
