import sys

from dill import objects
from scipy.constants import gallon

# Program 11

print("~~~~~~~~~~~~~~~~~Program 11~~~~~~~~~~~~~~~~~")

# After installing mypy, execute mypy meows.py in the terminal window. mypy will provide some guidance about how to
# fix this error.

# You can annotate all your variables. In the text editor window, code as follows:

# def meow(n: int):
    # for _ in range(n):
        # print("meow")

# number: int = input("Number: ")
# meow(number)

# Notice how number is now provided a type hint.

# Program 12

print("~~~~~~~~~~~~~~~~~Program 12~~~~~~~~~~~~~~~~~")

# Again, executing mypy meows.py in the terminal window provides much more specific feedback to you, the programmer.
# We can fix our final error by coding as follows:

# def meowTwo(nTwo: int):
    # for _ in range(nTwo):
        # print("meow")

# numberTwo: int = int(input("numberTwo: "))
# meowTwo(numberTwo)

# Notice how running mypy how produces no errors because cast our input as an integer.

# Program 13

print("~~~~~~~~~~~~~~~~~Program 13~~~~~~~~~~~~~~~~~")

# Let’s introduce a new error by assuming that meow will return to us a string, or str. In the text editor window,
# code as follows:

# def meowThree(nThree: int):
    # for _ in range(nThree):
        # print("meow")

# numberThree: int = int(input("numberThree: "))
# meows = meowThree(numberThree)
# print(meows)

# Notice how the meow function has only a side effect. Because we only attempt to print “meow”, not return a value,
# an error is thrown when we try to store the return value of meow in meows

# Program 14

print("~~~~~~~~~~~~~~~~~Program 14~~~~~~~~~~~~~~~~~")

# We can further use type hints to check for errors, this time annotating the return values of functions. In the text
# editor window, code as follows:

# def meowFour(nFour: int) -> None:
    # for _ in range(nFour):
        # print("meow")

# numberFour: int = int(input("numberFour: "))
# meowsTwo: str = meowFour(numberFour)
# print(meowsTwo)

# Notice how the notation -> None tells mypy that there is no return value.


# Program 15

print("~~~~~~~~~~~~~~~~~Program 15~~~~~~~~~~~~~~~~~")

# We can modify our code to return a string if we wish:

# def meowFive(nFive: int) -> str:
    # return "meow\n" * nFive

# numberFive: int = int(input("Number: "))
# meowsThree: str = meowFive(numberFive)
# print(meowsThree, end="")

# Notice how we store in meows multiple strs. Running mypy produces no errors.
# You can learn more in Python’s documentation of Type Hints.
# You can learn more in Python’s documentation of Type Hints.


# Program 16

print("~~~~~~~~~~~~~~~~~Program 16~~~~~~~~~~~~~~~~~")

# Docstrings

# A standard way of commenting your function’s purpose is to use a docstring. In the text editor window, code
# as follows:

# def meowSix(nSix):
    # """Meow n times."""
    # return "meow\n" * nSix

# numberSix = int(input("Number: "))
# meowsFour = meowSix(numberSix)
# print(meowsFour, end="")

# Notice how the three double quotes designate what the function does.

# Program 17

print("~~~~~~~~~~~~~~~~~Program 17~~~~~~~~~~~~~~~~~")

# You can use docstrings to standardize how you document the features of a function. In the text editor window,
# code as follows: s

# def meowSeven(nSeven):
    # """
    # Meow n times.

    # :param n: Number of times to meow
    # :type n: int
    # :raise TypeError: If n is not an int
    # :return: A string of n meows, one per line
    # :rtype: str
    # """

    # return "meowSeven\n" * nSeven

# numberSeven = int(input("numberSeven: "))
# meowsFive = meowSeven(numberSeven)
# print(meowsFive, end="")

# Notice how multiple docstring arguments are included. For example, it describes the parameters taken by the function
# and what is returned by the function.

# Established tools, such as Sphinx, can be used to parse docstrings and automatically create documentation for us in
# the form of web pages and PDF files such that you can publish and share with others.
# You can learn more in Python’s documentation of docstrings.

# Program 18

print("~~~~~~~~~~~~~~~~~Program 18~~~~~~~~~~~~~~~~~")

# argparse
# Suppose we want to use command-line arguments in our program. In the text editor window, code as follows:

# import sys

# if len(sys.argv) == 1:
    # print("meow")
# elif len(sys.argv) == 3 and sys.argv[-1] == "-n":
    # nEight = int(sys.argv[2])

    # for _ in range(nEight):
        # print("meow")
# else:
    # print("usage: meows.py [-n NUMBER]")

# Notice how argparse is imported instead of sys. An object called parser is created from an ArgumentParser class.
# That class’s add_argument method is used to tell argparse what arguments we should expect from the user when they run
# our program. Finally, running the parser’s parse_args method ensures that all of the arguments have been included
# properly by the user.

# Program 19

print("~~~~~~~~~~~~~~~~~Program 19~~~~~~~~~~~~~~~~~")

# We can also program more cleanly, such that our user can get some information about the proper usage of our code when
# they fail to use the program correctly. In the text editor window, code as follows:

# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", help="number of times to meow")
# args = parser.parse_args()

# for _ in range(int(args.n)):
    # print("meow")

# Program 20

print("~~~~~~~~~~~~~~~~~Program 20~~~~~~~~~~~~~~~~~")

# Notice how the user is provided some documentation. Specifically, a help argument is provided. Now, if the user
# executes python meows.py --help or -h, the user will be presented with some clues about how to use this program.

# We can further improve this program. In the text editor window, code as follows:

# import argparse

# parserTwo = argparse.ArgumentParser(description="Meow like a cat")
# parserTwo.add_argument("-n", default=1, help="number of times to meow", type=int)
# argsTwo = parserTwo.parse_args()

# for _ in range(argsTwo.n):
    # print("meow")

# Notice how not only is help documentation included, but you can provide a default value when no arguments are
# provided by the user.You can learn more in Python’s documentation of argparse

# Program 21

print("~~~~~~~~~~~~~~~~~Program 21~~~~~~~~~~~~~~~~~")

# Unpacking

# Would it not be nice to be able to split a single variable into two variables? In the text editor window,
# code as follows:

# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")

# Notice how this program tries to get a user’s first name by naively splitting on a single space.
# It turns out there are other ways to unpack variables. You can write more powerful and elegant code by understanding
# how to unpack variables in seemingly more advanced ways. In the text editor window, code as follows:

# def total(galleons, sickles, knuts):
    # return (galleons * 17 + sickles) * 29 + knuts

# print(total(100, 50, 25), "Knuts")

# Notice how this returns the total value of Knuts.
# What if we wanted to store our coins in a list? In the text editor window, code as follows:

# def totalTwo(galleonsTwo, sicklesTwo, knutsTwo):
    # return (galleonsTwo * 17 + sicklesTwo) * 29 + knutsTwo

# coins = [100, 50, 25]
# print(totalTwo(coins[0], coins[1], coins[2]), "Knuts")

# Notice how a list called coins is created. We can pass each value in by indexing using 0, 1, and so on.

# Program 22

print("~~~~~~~~~~~~~~~~~Program 22~~~~~~~~~~~~~~~~~")

# This is getting quite verbose. Wouldn’t it be nice if we could simply pass the list of coins to our function?
# To enable the possibility of passing the entire list, we can use unpacking. In the text editor window,
# code as follows:

# def totalThree(galleonsThree, sicklesThree, knutsThree):
    # return (galleonsThree * 17 + sicklesThree) * 29 + knutsThree

# coinsTwo = [100, 50, 25]
# print(totalThree(*coinsTwo), "Knuts")

# Notice how a * unpacks the sequence of the list of coins and passes in each of its individual elements to total.
# Suppose that we could pass in the names of the currency in any order? In the text editor window, code as follows:

# def totalFour(galleonsFour, sicklesFour, knutsFour):
    # return (galleonsFour * 17 + sicklesFour) * 29 + knutsFour

# print(totalFour(galleonsFour=100, sicklesFour=50, knutsFour=25), "Knuts")

# Notice how this still calculates correctly.

# Program 23

print("~~~~~~~~~~~~~~~~~Program 23~~~~~~~~~~~~~~~~~")

# When you start talking about “names” and “values,” dictionaries might start coming to mind! You can implement this as
# a dictionary. In the text editor window, code as follows:

# def totalFive(galleonsFive, sicklesFive, knutsFive):
    # return (galleonsFive * 17 + sicklesFive) * 29 + knutsFive

# print(totalFive(galleonsFive=100, sicklesFive=50, knutsFive=25), "Knuts")

# Notice how this still calculates correctly.

# Program 24

print("~~~~~~~~~~~~~~~~~Program 24~~~~~~~~~~~~~~~~~")

# When you start talking about “names” and “values,” dictionaries might start coming to mind! You can implement this
# as a dictionary. In the text editor window, code as follows:

# def totalSix(galleonsSix, sicklesSix, knutsSix):
    # return (galleonsSix * 17 + sicklesSix) * 29 + knutsSix

# coinsThree = {"galleonsSeven": 100, "sicklesSeven": 50, "knutsSeven": 25}
# print(totalSix(coinsThree["galleonsSeven"], coinsThree["sicklesSeven"], coinsThree["knutsSeven"]), "Knuts")

# Notice how a dictionary called coins is provided. We can index into it using keys, such as “galleons” or “sickles”.

# Program 25

print("~~~~~~~~~~~~~~~~~Program 25~~~~~~~~~~~~~~~~~")

# Since the total function expects three arguments, we cannot pass in a dictionary. We can use unpacking to help with
# this. In the text editor window, code as follows:

# def totalSeven(galleonsEight, sicklesEight, knutsEight):
    # return (galleonsEight * 17 + sicklesEight) * 29 + knutsEight

# coinsFour = {"galleonsEight": 100, "sicklesEight": 50, "knutsEight": 25}
# print(totalSeven(**coinsFour), "Knuts")

# Notice how ** allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.

# Program 26

print("~~~~~~~~~~~~~~~~~Program 26~~~~~~~~~~~~~~~~~")

# Notice how ** allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.

# args and kwargs
# Recall the print documentation we looked at earlier in this course:

print(*objects, sep =' ', end='\n', file=sys.stdout, flush=False)

# Program 27

print("~~~~~~~~~~~~~~~~~Program 27~~~~~~~~~~~~~~~~~")

# args are positional arguments, such as those we provide to print like print("Hello", "World")
# kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="").

# As we see in the prototype for the print function above, we can tell our function to expect a presently unknown
# number positional arguments. We can also tell it to expect a presently unknown number of keyword arguments. In the
# text editor window, code as follows:

def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)

# Program 28

print("~~~~~~~~~~~~~~~~~Program 28~~~~~~~~~~~~~~~~~")

# Notice how executing this code will be printed as positional arguments.
# We can even pass in named arguments. In the text editor window, code as follows:

def fTwo(*args, **kwargs):
    print("Named:", kwargs)

fTwo(galleonsNine = 100, sicklesNine=50, knutsNine = 20)

# Notice how the named values are provided in the form of a dictionary.
# Thinking about the print function above, you can see how *objects takes any number of positional arguments.
# Thinking about the print function above, you can see how *objects takes any number of positional arguments.



