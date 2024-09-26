
# Program 16

print("~~~~~~~~~~~~~~~Program 16~~~~~~~~~~~~~~~")

# Integers or int
# First, we can declare a few variables.
x = 1
y = 2

z = x + y
print(z)

# Program 17

print("~~~~~~~~~~~~~~~Program 17~~~~~~~~~~~~~~~")

# Naturally, when we run python calculator.py we get the result in the terminal window of 3. We can make this more
# interactive using the input function.

################ 17 ################
# xTwo = input("What is x? ")
# yTwo = input("What is y? ")

# zTwo = xTwo + yTwo
# print(zTwo)

print("~~~~~~~~~~~~~~~~~~~~~")

# 108 85 53
print(2024 - 108)
print(2024 - 85)
print(2024 - 53)

print("~~~~~~~~~~~~~~~~~~~~~")

print(1939-1916)
print(1971-1939)
print(1971-1916)

print("~~~~~~~~~~~~~~~~~~~~~")

print(2024 + 23)
print(2024 + 32)
print(2024 + 55)

# Program 18

print("~~~~~~~~~~~~~~~Program 18~~~~~~~~~~~~~~~")

# Running this program, we discover that the output is incorrect as 12. Why might this be?
# Prior, we have seen how the + sign concatenates two strings. Because your input from your keyboard on your computer
# comes into the compiler as text, it is treated as a string. We, therefore, need to convert this input from a string
# to an integer. We can do so as follows:

################ 18 ################
# xThree = input("What's x? ")
# yThree = input("What's y? ")

# zThree = int(xThree) + int(yThree)
# print(zThree)

# Program 19

print("~~~~~~~~~~~~~~~Program 19~~~~~~~~~~~~~~~")

# The result is now correct. The use of int(x) is called “casting,” where a value is temporarily changed from one type
# of variable (in this case, a string) to another (here, an integer).

# We can further improve our program as follows:

################ 19 ################
# xFour = int(input("What's x? "))
# yFour = int(input("What's y? "))

# print(xFour + yFour)

# Program 20

print("~~~~~~~~~~~~~~~Program 20~~~~~~~~~~~~~~~")

# Readability Wins

# When deciding on your approach to a coding task, remember that one could make a reasonable argument for many
# approaches to the same problem.

# Regardless of what approach you take to a programming task, remember that your code must be readable. You should use
# comments to give yourself and others clues about what your code is doing. Further, you should create code in a way
# that is readable.

# Float Basics
# A floating point value is a real number that has a decimal point in it, such as 0.52.
# You can change your code to support floats as follows:

################ 20 ################
# xFive = float(input("What's x? "))
# yFive = float(input("What's y? "))

# print(xFive + yFive)

# This change allows your user to enter 1.2 and 3.4 to present a total of 4.6.
# Let’s imagine, however, that you want to round the total to the nearest integer. Looking at the Python documentation
# for round, you’ll see that the available arguments are round(number[n, ndigits]). Those square brackets indicate that
# something optional can be specified by the programmer. Therefore, you could do round(n) to round a digit to its
# nearest integer. Alternatively, you could code as follows:

# Program 21

print("~~~~~~~~~~~~~~~Program 21~~~~~~~~~~~~~~~")

################ 21 ################
# get the user's input
# xSix = float(input("What's x? "))
# ySix = float(input("What's y? "))

# create a rounded result
# zSix = round(xSix + ySix)

# print the result
# print(zSix)


# Program 22

print("~~~~~~~~~~~~~~~Program 22~~~~~~~~~~~~~~~")

# The output will be rounded to the nearest integer.
# What if we wanted to format the output of long numbers? For example, rather than seeing 1000, you may wish to see
# 1,000. You could modify your code as follows:

################ 22 ################
# get the user's input
# xSeven = float(input("What's x? "))
# ySeven = float(input("What's y? "))

# create a rounded result
# zSeven = round(xSeven + ySeven)

# print the formatted result
# print(f"{zSeven:,}")

# Program 23

print("~~~~~~~~~~~~~~~Program 23~~~~~~~~~~~~~~~")

# More on Floats

# How can we round floating point values? First, modify your code as follows:

################ 23 ################
# get the user's input
# xEight = float(input("What's x? "))
# yEight = float(input("What's y? "))

# calculate the result
# zEight = xEight / yEight
# print(zEight)

# Program 24

print("~~~~~~~~~~~~~~~Program 24~~~~~~~~~~~~~~~")

# When inputting 2 as x and 3 as y, the result z is 0.6666666666, seemingly going on to infinite as we might expect.
# Let’s imagine that we want to round this down. We could modify our code as follows:

################ 24 ################
# get the user's input
# xNine = float(input("What's x? "))
# yNine = float(input("What's y? "))

# calculate the result and round
# zNine = round(xNine / yNine, 2)

# print the result
# print(zNine)

# Program 25

print("~~~~~~~~~~~~~~~Program 25~~~~~~~~~~~~~~~")

# As we might expect, this will round the result to the nearest two decimal points.
# We could also use fstring to format the output as follows:

################ 25 ################
# get the user's input
# xTen = float(input("What's x? "))
# yTen = float(input("What's y? "))

# calculate the result
# zTen = xTen / yTen

# print the result
# print(f"{zTen: .2f}")


# Program 33

print("~~~~~~~~~~~~~~~Program 33~~~~~~~~~~~~~~~")

# Returning Values

# You can imagine many scenarios where you don’t just want a function to perform an action but also to return a value
# back to the main function. For example, rather than simply printing the calculation of x + y, you may want a function
# to return the value of this calculation back to another part of your program. This “passing back” of a value we call
# a return value.

# Returning to our calculator.py code by typing code calculator.py. Erase all code there. Rework the code as follows:

def mainThree():
    xEleven = int(input("What's x? "))
    print("x squared is", square(xEleven))


def square(n):
    return n * n

mainThree()

print(2024 - 100)
print(100 - 26)
print(1924 - 74)

# Summing Up

# Through the work of this single lecture, you have learned abilities that you will use countless times in your own
# programs. You have learned about…

# 1. Creating your first programs in Python;
# 2. Functions;
# 3. Bugs;
# 4. Variables;
# 5. Comments;
# 6. Pseudocode;
# 7. Strings;
# 8. Parameters;
# 9. Formatted Strings;
# 10. Integers;
# 11. Principles of readability;
# 12. Floats;
# 13. Creating your own functions; and
# 14. Return values.



# Effectively, x is passed to square. Then, the calculation of x * x is returned back to the main function.
