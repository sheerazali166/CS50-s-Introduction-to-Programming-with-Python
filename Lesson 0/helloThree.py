
# import helloTwo

# Program 27

print("~~~~~~~~~~~~~~~Program 27~~~~~~~~~~~~~~~")

################ 27 ################
# We can better our code to create our own special function that says “hello” for us!
# Erasing all our code in our text editor, let’s start from scratch:
# name = input("What's your name? ")
# helloTwo()
# print(name)

# TypeError: 'module' object is not callable

# Program 28

print("~~~~~~~~~~~~~~~Program 28~~~~~~~~~~~~~~~")

# Attempting to run this code, your compiler will throw an error. After all, there is no defined function for hello.
# We can create our own function called hello as follows:

################ 28 ################
# def hello():
    # print("hello")

# name = input("What's your name? ")
# hello()
# print(name)

# Program 29

print("~~~~~~~~~~~~~~~Program 29~~~~~~~~~~~~~~~")

# Notice that everything under def hello() is indented. Python is an indented language. It uses indentation to
# understand what is part of the above function. Therefore, everything in the hello function must be indented.
# When something is not indented, it treats it as if it is not inside the hello function. Running python hello.py
# in the terminal window, you’ll see that your output is not exactly as you may want.

# We can further improve our code:

# create our own function
# def helloTwo(to):
    # print("hello,", to)

# output using our own function
# nameTwo = input("What's your name? ")
# helloTwo(nameTwo)

# Program 30

print("~~~~~~~~~~~~~~~Program 30~~~~~~~~~~~~~~~")

# Here, in the first lines, you are creating your hello function. This time, however, you are telling the compiler
# that this function takes a single parameter: a variable called to. Therefore, when you call hello(name) the computer
# passes name into the hello function as to. This is how we pass values into functions. Very useful! Running python
# hello.py in the terminal window, you’ll see that the output is much closer to our ideal presented earlier
# in this lecture.

# We can change our code to add a default value to hello:

################ 30 ################
# create our own function
# def helloThree(to="world"):
    # print("hello,", to)

# output using our own function
# nameThree = input("What's your name? ")
# helloThree(nameThree)

# output without passing the expected arguments
# helloThree()

# Program 31

print("~~~~~~~~~~~~~~~Program 31~~~~~~~~~~~~~~~")

# Test out your code yourself. Notice how the first hello will behave as you might expect, and the second hello,
# which is not passed a value, will, by default, output hello, world.

# We don’t have to have our function at the start of our program. We can move it down, but we need to tell the compiler
# that we have a main function and a separate hello function.

################ 31 ################
# def main():

    # output using our own function
    # nameFour = input("What's your name? ")
    # helloFour(nameFour)

    # output without passing the expected arguments
    # helloFour()

# create our own function
# def helloFour(to="world"):
    # print("hello,", to)

# Program 32

print("~~~~~~~~~~~~~~~Program 32~~~~~~~~~~~~~~~")

# This alone, however, will create an error of sorts. If we run python hello.py, nothing happens! The reason for this
# is that nothing in this code is actually calling the main function and bringing our program to life.

# The following very small modification will call the main function and restore our program to working order:

def mainTwo():

    # output using our function
    nameFive = input("What's your name? ")
    helloFive(nameFive)

    # output without passing the expected arguments
    helloFive()

# create our own function
def helloFive(to="world"):
    print("hello,", to)

mainTwo()


