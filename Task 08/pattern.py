# number of rows in pattern
rows = 5

# outer loop to iterate over both increasing and decreasing parts of pattern
for i in range(1, 2 * rows):
    # asks if 'i' is less than or equal to rows(5)
    # if True this will be the first part of the pattern
    if i <= rows:
        # this will draw a number of stars based om the number of the row (first row = 1 star)
        num_stars = i

    else:
        # this is the second part of the pattern which is the decrease
        num_stars = 2 * rows - i

    # inner loop to iterate over number of stars in each row
    for j in range(num_stars):
        # print a star without a newline
        print("*", end="")

    # move to the next line after each row
    print()
