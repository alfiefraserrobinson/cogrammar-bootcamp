#create variable to store/save the string#
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

data_type = ""

#use replace() function to modify the string within the variable - replacing "!" with a blank space (" ")#
new_sentence = (sentence.replace("!", " "))

#print the modified sentence#
print(new_sentence)

#reprint the same modified sentence but further modify it to make it all uppercase using the .upper method#
print(new_sentence.upper())