

# Program 18

print("~~~~~~~~~~~~~~~~~~Program 18~~~~~~~~~~~~~~~~~~")

# Cleaning Up User Input

# You should never expect your users to always follow your hopes for clean input. Indeed, users will often violate your
# intentions as a programmer.

# There are ways to clean up your data.
# In the terminal window, type code format.py. Then, in the text-editor, code as follows:

# name = input("What's your name? ").strip()
# print(f"hello, {name}")

# Notice that we have created, essentially, a “hello world” program. Running this program and typing in David, it
# works well! However, typing in Malan, David notice how the program does not function as intended. How could we
# modify our program to clean up this input?

# Program 19

print("~~~~~~~~~~~~~~~~~~Program 19~~~~~~~~~~~~~~~~~~")

# Modify your code as follows.

# nameTwo = input("What's your name? ").strip()

# if "," in nameTwo:
    # last, first = nameTwo.split(", ")
    # nameTwo = f"{first} {last}"
# print(f"hello, {nameTwo}")

# Notice how last, first = name.split(", ") is run if there is a , in the name. Then, the name is standardized as first
# and last. Running our code, typing in Malan, David, you can see how this program does clean up at least one scenario
# where a user types in something unexpected.

# Program 20

print("~~~~~~~~~~~~~~~~~~Program 20~~~~~~~~~~~~~~~~~~")

# You might notice that typing in Malan,David with no space causes the compiler to throw an error. Since we now know
# some regular expression syntax, let’s apply that to our code:

# mport re

# nameThree = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", nameThree)

# if matches:
    # lastTwo, firstTwo = matches.group()
    # nameThree = firstTwo + " " + lastTwo
# print(f"hello, {nameThree}")

# Notice that re.search can return a set of matches that are extracted from the user’s input. If matches are returned
# by re.search. Running this program, typing in David Malan notice how the if condition is not run and the name is
# returned. If you run the program by typing Malan, David, the name is also returned properly.

# Program 21

print("~~~~~~~~~~~~~~~~~~Program 21~~~~~~~~~~~~~~~~~~")

# It just so happens that we can request specific groups back using matches.group. We can modify our code as follows:

import re

# nameFour = input("What's your name? ").strip()
# matchesTwo = re.search("^(.+), (.+)$", nameFour)

# if matchesTwo:
    # nameFour = matchesTwo.group(2) + " " + matchesTwo.group(1)
# print(f"hello, {nameFour}")

# Notice how, in this implementation, group is not plural (there is no s).

# Program 22

print("~~~~~~~~~~~~~~~~~~Program 21~~~~~~~~~~~~~~~~~~")

# Our code can be further tightened as follows:

# import re

# nameFive = input("What's your name? ").strip()
# matchesThree = re.search(r"^(.+), (.+)$", nameFive)

# if matchesThree:
    # nameFive = matchesThree.group(2) + " " + matchesThree.group(1)

# print(f"hello, {nameFive}")

# Notice how group(2) and group(1) are concatenated together with a space. The first group is that which is left of
# the comma. The second group is that which is right of the comma.

# Program 23

print("~~~~~~~~~~~~~~~~~~Program 23~~~~~~~~~~~~~~~~~~")

# Recognize still that typing in Malan,David with no space will still break our code. Therefore, we can make the
# following modification:

# import re

# nameSix = input("What's your name? ").strip()

# matchesFour = re.search(r"^(.+), *(.+)$", nameSix)

# if matchesFour:
    # nameSix = matchesFour.group(2) + " " + matchesFour.group(1)
# print(f"hello, {nameSix}")

# Notice the addition of the * in our validation statement. This code will now accept and properly process
# Malan,David. Further, it will properly handle ` David,Malan with many spaces in front of David`.

# Program 24

print("~~~~~~~~~~~~~~~~~~Program 24~~~~~~~~~~~~~~~~~~")

# It is very common to utilize re.search as we have in the previous examples, where matches is on a line of code after.
# However, we can combine these statements:

import re

nameSeven = input("What's your name? ").strip()

if matchesFive := re.search(r"^(.+), *(.+)$", nameSeven):
    nameSeven = matchesFive.group(2) + " " + matchesFive.group(1)
print(f"hello, {nameSeven}")

# Notice how we combine two lines of our code. The walrus := operator assigns a value from right to left and allows
# us to ask a boolean question at the same time. Turn your head sideways and you’ll see why this is called a walrus
# operator.

# You can learn more in Python’s documentation of re.



