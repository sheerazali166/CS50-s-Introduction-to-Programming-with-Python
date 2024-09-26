
# Program 11

print("~~~~~~~~~~~~~~~~~~Program 11~~~~~~~~~~~~~~~~~~")

# Modulo

# In mathematics, parity refers to whether a number is either even or odd.
# The modulo % operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.

# For example, 4 % 2 would result in zero, because it evenly divides. However, 3 % 2 does not divide evenly and would
# result in a number other than zero!

# In the terminal window, create a new program by typing code parity.py. In the text editor window, type your
# code as follows:

############### Program 11 ###############
# x = int(input("What's x? "))

# if x % 2 == 0:
    # print("Even")
# else:
    # print("Odd")

# Notice how our users can type in any number 1 or greater to see if it is even or odd.


# Program 12

print("~~~~~~~~~~~~~~~~~~Program 12~~~~~~~~~~~~~~~~~~")


# Creating Our Own Parity Function

# As discussed in Lecture 0, you will find it useful to create a function of your own!
# We can create our own function to check whether a number is even or odd. Adjust your code as follows:

############### Program 12 ###############
# def main():
    # x = int(input("What's x? "))
    # if is_even(x):
        # print("Even")
    # else:
        # print("Odd")


# def is_even(n):
    # if n % 2 == 0:
        # return True
    # else:
        # return False

# main()

# Notice that our if statement is_even(x) works even though there is no operator there. This is because our function
# returns a bool (or boolean), true or false, back to the main function. The if statement simply evaluates whether or
# not is_even of x is true or false.


# Program 13

print("~~~~~~~~~~~~~~~~~~Program 13~~~~~~~~~~~~~~~~~~")

# Pythonic

# In the programming world, there are types of programming that are called “Pythonic” in nature. That is, there are
# ways to program that are sometimes only seen in Python programming. Consider the following revision to our program:

############### Program 13 ###############
# def main_two():
    # xTwo = int(input("What's xTwo? "))
    # if is_even_two(xTwo):
        # print("Even")
    # else:
        # print("Odd")


# def is_even_two(nTwo):
    # return True if nTwo % 2 == 0 else False

# main_two()

# Notice that this return statement in our code is almost like a sentence in English. This is a unique way of coding
# only seen in Python.

# Program 14

print("~~~~~~~~~~~~~~~~~~Program 14~~~~~~~~~~~~~~~~~~")

# We can further revise our code and make it more and more readable:

############### Program 14 ###############
# def main_three():
    # xThree = int(input("What's xThree? "))
    # if is_even_three(xThree):
        # print("Even")
    # else:
        # print("Odd")


# def is_even_three(nThree):
    # return nThree % 2 == 0

# main_three()

# Notice that the program will evaluate what is happening within the n % 2 == 0 as either true or false and simply
# return that to the main function.


# Program 15

print("~~~~~~~~~~~~~~~~~~Program 15~~~~~~~~~~~~~~~~~~")

# match

# Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain
# values.

# Consider the following program:

############### Program 15 ###############
# name = input("What's your name? ")

# if name == "Harry":
    # print("gryffindor")
# elif name == "Hermione":
    # print("Gryffindor")
# elif name == "Ron":
    # print("Gryffindor")
# elif name == "Draco":
    # print("Slytherin")
# else:
    # print("Who?")

# Notice the first three conditional statements print the same response.


# Program 16

print("~~~~~~~~~~~~~~~~~~Program 16~~~~~~~~~~~~~~~~~~")

# We can improve this code slightly with the use of the or keyword:

############### Program 16 ###############
# nameTwo = input("What's your nameTwo? ")

# if nameTwo == "Harry" or nameTwo == "Hermione" or nameTwo == "Ron":
    # print("Gryffindor")
# elif nameTwo == "Draco":
    # print("Slytherin")
# else:
    # print("Who?")

# Notice the number of elif statements has decreased, improving the readability of our code.


# Program 17

print("~~~~~~~~~~~~~~~~~~Program 17~~~~~~~~~~~~~~~~~~")

# Alternatively, we can use match statements to map names to houses. Consider the following code:

############### Program 17 ###############
# nameThree = input("What's your nameThree? ")

# match nameThree:
    # case "Harry":
        # print("Gryffindor")
    # case "Hermione":
        # print("Gryffindor")
    # case "Ron":
        # print("Gryffindor")
    # case "Draco":
        # print("Slytherin")
    # case _:
        # print("Who?")

# Notice the use of the _ symbol in the last case. This will match with any input, resulting in similar behavior as
# an else statement.


# Program 18

print("~~~~~~~~~~~~~~~~~~Program 18~~~~~~~~~~~~~~~~~~")

# A match statement compares the value following the match keyword with each of the values following the case keywords.
# In the event a match is found, the respective indented code section is executed, and the program stops the matching.

# We can improve the code:

nameFour = input("What's nameFour? ")

match nameFour:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


# Notice, the use of the single vertical bar |. Much like the or keyword, this allows us to check for multiple values
# in the same case statement.

# Summing Up

# You now have the power within Python to use conditional statements to ask questions and have your program take action
# accordingly. In this lecture, we discussed…

# 1. Conditionals;
# 2. if Statements;
# 3. Control flow, elif, and else;
# 4. or;
# 5. and;
# 6. Modulo;
# 7. Creating your own function;
# 8. Pythonic coding;
# 9. and match.