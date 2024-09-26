
# Program 8

print("~~~~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~~~~")

# AND

# Similar to or, and can be used within conditional statements.
# Execute in the terminal window code grade.py. Start your new program as follows:

############### Program 8 ###############
# score = int(input("Score: "))

# if score >= 90 and score <= 100:
    # print("Grade: A")
# elif score >= 80 and score < 90:
    # print("Grade: B")
# elif score >= 70 and score < 80:
    # print("Grade: C")
# elif score >= 60 and score < 70:
    # print("Grade: D")
# else:
    # print("Grade: F")


# Program 9

print("~~~~~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~~~~~")

# Notice that by executing python grade.py, you will be able to input a score and get a grade. However, notice how
# there is potential for bugs.

# Typically, we do not want to ever trust our users to input the correct information. We could improve our code
# as follows:

############### Program 9 ###############
# scoreTwo = int(input("scoreTwo: "))

# if 90 <= scoreTwo <= 100:
    # print("Grade: A")
# elif 80 <= scoreTwo < 90:
    # print("Grade: B")
# elif 70 <= scoreTwo < 80:
    # print("Grade: C")
# elif 60 <= scoreTwo < 70:
    # print("Grade: D")
# else:
    # print("Grade: F")


# Program 10

print("~~~~~~~~~~~~~~~~~~Program 10~~~~~~~~~~~~~~~~~~")

# Notice how Python allows you to chain together the operators and conditions in a way quite uncommon to other
# programming languages.

# Still, we can further improve our program:

scoreThree = int(input("scoreThree: "))

if scoreThree >= 90:
    print("Grade: A")
elif scoreThree >= 80:
    print("Grade: B")
elif scoreThree >= 70:
    print("Grade: C")
elif scoreThree >= 60:
    print("Grade: D")
else:
    print("Grade: F")

