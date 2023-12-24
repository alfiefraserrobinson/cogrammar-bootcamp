# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Alternating Character Case #

# Create an empty string to store each alternating character
result_characters = ""

# Iterate over each character from input_string using their index
for i in range(len(input_string)):
    # If the index is even, convert the character to upper case and add it to 'result_characters'
    if i % 2 == 0:
        result_characters += input_string[i].upper()
    # If the index is odd, convert the character to lower case and add it to 'result_characters'
    else:
        result_characters += input_string[i].lower()

# Alternating word case #

# Split the input string into a list of words
words = input_string.split()

# Create an empty string to store the result of alternating word
result_words = ""

# Iterate over the list of words using their index
for i in range(len(words)):
    # If the index is even, convert the word to lower case and append it to 'result_words'
    if i % 2 == 0:
        result_words += words[i].lower()
    # If the index is odd, convert the word to upper case and append it to 'result_words'
    else:
        result_words += words[i].upper()
    # Append a space after each word, except the last word, to keep words separated
    if i < len(words) - 1:
        result_words += " "

# Print the results for both alternating characters and words
print("Alternate characters:", result_characters)
print("Alternate words:", result_words)
