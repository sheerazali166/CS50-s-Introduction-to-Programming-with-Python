
# Program 1

print("~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~")

# Exceptions

# Exceptions are things that go wrong within our coding.

# In our text editor, type code hello.py to create a new file. Type as follows (with the intentional errors included):

# print("hello, world)

# Notice that we intentionally left out a quotation mark.

# Running python hello.py in our terminal window, an error is outputted. The compiler states that it is a
# “syntax error.”” Syntax errors are those that require you to double-check that you typed in your code correction.

# You can learn more in Python’s documentation of Errors and Exceptions.


# Program 2

print("~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~")

# Runtime Errors

# Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for
# a user to input a number, but they input a character instead. Your program may throw an error because of this
# unexpected input from the user.

# In your terminal window, run code number.py. Code as follows in your text editor:

# x = int(input("What's x? "))
# print(f"x is {x}")

# Notice that by including the f, we tell Python to interpolate what is in the curly braces as the value of x. Further,
# testing out your code, you can imagine how one could easily type in a string or a character instead of a number. Even
# still, a user could type nothing at all – simply hitting the enter key.

# As programmers, we should be defensive to ensure that our users are entering what we expected. We might consider
# “corner cases” such as -1, 0, or cat

# If we run this program and type in “cat”, we’ll suddenly see ValueError: invalid literal for int() with base 10:
# 'cat' Essentially, the Python interpreter does not like that we passed “cat” to the print function.

# An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as
# we intend. You can learn more in Python’s documentation of Errors and Exceptions.


# Program 3

print("~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~")

# try

# In Python try and except are ways of testing out user input before something goes wrong. Modify your code
# as follows:

# try:
    # xTwo = int(input("What's xTwo?")) # x is x the end
    # print(f"xTwo? is {xTwo}")
# except ValueError:
    # print("xTwo is not an integer")

# Program 4

print("~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~")

# Notice how, running this code, inputting 50 will be accepted. However, typing in cat will produce an error visible to
# the user, instructing them why their input was not accepted.

# This is still not the best way to implement this code. Notice that we are trying to do two lines of code. For best
# practice, we should only try the fewest lines of code possible that we are concerned could fail. Adjust your code
# as follows:

# try:
    # xThree = int(input("What's xThree? "))
# except ValueError:
    # print("xThree is not an integer")

# print(f"xThree is {xThree}")

# Notice that while this accomplishes our goal of trying as few lines as possible, we now face a new error! We face a
# NameError where x is not defined. Look at this code and consider: Why is x not defined in some cases?

# Indeed, if you examine the order of operations in x = int(input("What's x?")), working right to left, it could take
# an incorrectly inputted character and attempt to assign it as an integer. If this fails, the assignment of the value
# of x never occurs. Therefore, there is no x to print on our final line of code.

# Program 5

print("~~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~~")

# else

# It turns out that there is another way to implement try that could catch errors of this nature.

# Adjust your code as follows:

# try:
    # xFour = int(input("What's xFour?"))
# except ValueError:
    # print("xFour  is not an integer")
# else:
    # print(f"xFour is {xFour}")


# Program 6

print("~~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~~")

# Considering improving our code, notice that we are being a bit rude to our user. If our user does not cooperate, we
# currently simply end our program. Consider how we can use a loop to prompt the user for x and if they don’t prompt
# again! Improve your code as follows:

# while True:
    # try:
        # xFive = int(input("What's xFive?"))
    # except ValueError:
        # print("xFive is not an integer")
    # else:
        # break

# print(f"xFive is {xFive}")

# Notice that while True will loop forever. If the user succeeds in supplying the correct input, we can break from the
# loop and then print the output. Now, a user that inputs something incorrectly will be asked for input again.


# Program 7

print("~~~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~~~")

# Creating a Function to Get an Integer

# Surely, there are many times that we would want to get an integer from our user. Modify your code as follows:

# def main():
    # xSeven = get_int()
    # print(f"xSeven  is {xSeven}")


# def get_int():
    # while True:
        # try:
            # xSix = int(input("What's xSix?"))
        # except ValueError:
            # print("xSix is not an integer")
        # else:
            # break
    # return xSix

# main()


# Program 8

print("~~~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~~~")

# Notice that we are manifesting many great properties. First, we have abstracted away the ability to get an integer.
# Now, this whole program boils down to the first three lines of the program.

# Even still, we can improve this program. Consider what else you could do to improve this program. Modify your code
# as follows:

# def main_two():
    # xNine = get_int_two()
    # print(f"xNine is {xNine}")


# def get_int_two():
    # while True:
        # try:
            # xEight = int(input("What's xEight? "))
        # except ValueError:
            # print("xEight is not an integer")
        # else:
            # return xEight


# main_two()

# Notice that return will not only break you out of a loop, but it will also return a value.


# Program 9

print("~~~~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~~~~")

# Some people may argue you could do the following:

# def main_three():
    # xEleven = get_int_three()
    # print(f"xEleven is {xEleven}")


# def get_int_three():
    # while True:
        # try:
            # return int(input("What's xTen?"))
        # except ValueError:
            # print("xTen is not an integer")

# main_three()

# Notice this does the same thing as the previous iteration of our code, simply with fewer lines.

# Program 10

print("~~~~~~~~~~~~~~~~~Program 10~~~~~~~~~~~~~~~~~")

# pass

# We can make it such that our code does not warn our user, but simply re-asks them our prompting question by modifying
# our code as follows:

# def main_four():
    # xThirteen = get_int_four()
    # print(f"xThirteen is {xThirteen}")


# def get_int_four():
    # while True:
        # try:
            # return int(input("What's xTwelve?"))
        # except ValueError:
            # pass

# main_four()

# Notice that our code will still function but will not repeatedly inform the user of their error. In some cases,
# you’ll want to be very clear to the user what error is being produced. Other times, you might decide that you simply
# want to ask them for input again.

# Program 11

print("~~~~~~~~~~~~~~~~~Program 11~~~~~~~~~~~~~~~~~")

# One final refinement that could improve the implementation of this get_int function. Right now, notice that we are
# relying currently upon the honor system that the x is in both the main and get_int functions. We probably want to
# pass in a prompt that the user sees when asked for input. Modify your code as follows.

def main_five():
    xFourteen = get_int_five("What's xFourteen? ")
    print(f"xFourteen is {xFourteen}")

def get_int_five(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main_five()

# You can learn more in Python’s documentation of pass.

# Summing Up

# Errors are inevitable in your code. However, you have the opportunity to use what was learned today to help prevent
# these errors. In this lecture, you learned about…

# 1. Exceptions
# 2. Value Errors
# 3. Runtime Errors
# 4. try
# 5. else
# 6. pass

