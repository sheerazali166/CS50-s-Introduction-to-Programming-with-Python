from tkinter.font import names

# print("Kinza Sheikh Chocolaty")



# Program 1

print("~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~")

# Improving Your First Python Program

########### 1 #############
# input("What's your name?")
# print("Hello, World")

# Program 2

print("~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~")

# Variables

# A variable is just a container for a value within your own program.
# In your program, you can introduce your own variable in your program by editing it to read

########### 2 #############
# name = input("What's your name? ")
# print("hello, world")

# Program 3

print("~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~")

########### 3 #############
# If you edit your code as follows, you will notice an error
# nameTwo = input("What's your name? ")
# print("hello, nameTwo")

# Program 4

print("~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~")

########### 4 #############
# name = input("What's your name? ")
# print("hello,")
# print(name)

# Program 5

print("~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~")

########### 5 #############
# Comments
# Ask the user for their name
# name = input("What's your name? ")
# print("hello,")
# print(name)


# Program 6

print("~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~")

# Pseudocode

# Pseudocode is an important type of comment that becomes a special type of to-do list, especially when
# you don’t understand how to accomplish a coding task. For example, in your code, you might edit your code to say:

########### 6 #############
# Ask the user for their name
# name = input("What's your name? ")

# print hello
# print("hello,")

# print the name inputted
# print(name)

# Program 7

print("~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~")

# Further Improving Your First Python Program
# We can further edit our code as follows

########### 7 #############
# Ask the user for their name
# name = input("What's for your name? ")

# print hello and the inputted name
# print("hello," + name)

# Program 8

print("~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~")

# It turns out that some functions take many arguments.
# We can use a comma , to pass in multiple arguments by editing our code as follows:

########### 8 #############
# Ask the user for their name
# name = input("What's your name? ")

# print hello and the inputted name
# print("hello,", name)

# Program 9

print("~~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~~")

# Strings and Paremeters

# A string, known as a str in Python, is a sequence of text.
# Rewinding a bit in our code back to the following, there was a visual side effect of having the result
# appear on multiple lines:

########### 9 #############
# Ask the user for their name
# name = input("What's your name? ")
# print("hello,")
# print(name)

# Program 10

print("~~~~~~~~~~~~~~~Program 10~~~~~~~~~~~~~~~")

########### 10 #############
# We can modify our code as follows:
# ask the user for their name
# name = input("What's your name? ")
# print("hello,", end="")
# print(name)

# Program 11

print("~~~~~~~~~~~~~~~Program 11~~~~~~~~~~~~~~~")

# Formatting Strings
# Probably the most elegant way to use strings would be as follows:

########### 11 #############
# Ask the user for their name
# name = input("What's your name? ")
# print(f"hello, {name}")

# Program 12

print("~~~~~~~~~~~~~~~Program 12~~~~~~~~~~~~~~~")

########### 12 #############
# More on Strings

# Ask the user for
# name = input("What's your name? ")

# remove white space from the str
# name = name.strip()

# Print the output
# print(f"hello, {name}")


# Program 13

print("~~~~~~~~~~~~~~~Program 13~~~~~~~~~~~~~~~")

# Rerunning this program, regardless of how many spaces you type before or after the name,
# it will strip off all the whitespace.
# Using the title method, it would title case the user’s name:

########### 13 #############
# Ask the user for their name
# name = input("What's your name? ")

# remove white spaces from the str
# name = name.strip()

# Capitalize the first letter of each word
# name = name.title()

# Print the output
# print(f"hello, {name}")

# Program 14

print("~~~~~~~~~~~~~~~Program 14~~~~~~~~~~~~~~~")

# By this point, you might be very tired of typing python repeatedly in the terminal window. You cause use the
# up arrow of your keyboard to recall the most recent terminal commands you have made

# Notice that you can modify your code to be more efficient:

########### 14 #############
# Ask the user for their name
# name = input("What's your name? ")

# remove white space from the str and capitalize the first letter of each word
# name = name.strip().title()

# print the output
# print(f"hello, {name}")

# Program 15

print("~~~~~~~~~~~~~~~Program 15~~~~~~~~~~~~~~~")

# This creates the same result as your previous code.
# We could even go further!

# Ask the user for their name, remove white spaces from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# print the output
print(f"hello, {name}")
