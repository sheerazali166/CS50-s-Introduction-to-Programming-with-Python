from numpy.core.defchararray import upper

# Program 29

print("~~~~~~~~~~~~~~~~~Program 29~~~~~~~~~~~~~~~~~")

# map

# Early on, we began with procedural programming.
# We later revealed Python is an object oriented programming language.
# We saw hints of functional programming, where functions have side effects without a return value. We can illustrate
# this in the text editor window, type code yell.py and code as follows:

def main():
    yell("This is CS50")

def yell(word):
    print(word.upper())

if __name__ == '__main__':
    main()

# Program 30

print("~~~~~~~~~~~~~~~~~Program 30~~~~~~~~~~~~~~~~~")

# Notice how the yell function is simply yelled.
# Wouldn’t it be nice to yell a list of unlimited words? Modify your code as follows:

def mainTwo():
    yellTwo(["This", "is", "CS50"])

def yellTwo(words):
    uppercased = []
    for wordTwo in words:
        uppercased.append(wordTwo.upper())
    print(*uppercased)

mainTwo()

# Notice we accumulate the uppercase words, iterating over each of the words and uppercasing them. The uppercase list
# is printed utilizing the * to unpack it.

# Program 31

print("~~~~~~~~~~~~~~~~~Program 31~~~~~~~~~~~~~~~~~")

# Removing the brackets, we can pass the words in as arguments. In the text editor window, code as follows:

def mainThree():
    yellThree("This", "is", "CS50")

def yellThree(*wordsTwo):
    uppercasedTwo = []
    for wordThree in wordsTwo:
        uppercasedTwo.append(wordThree.upper())
    print(*uppercasedTwo)

mainThree()

# Notice how *words allows for many arguments to be taken by the function.

# Program 32

print("~~~~~~~~~~~~~~~~~Program 32~~~~~~~~~~~~~~~~~")

# map allows you to map a function to a sequence of values. In practice, we can code as follows:

def mainFour():
    yellFour("This", "is", "CS50")

def yellFour(*wordsThree):
    uppercasedThree = map(str.upper, wordsThree)
    print(uppercasedThree)

mainFour()

# Notice how map takes two arguments. First, it takes a function we want applied to every element of a list. Second,
# it takes that list itself, to which we’ll apply the aforementioned function. Hence, all words in words will be
# handed to the str.upper function and returned to uppercased.

# You can learn more in Python’s documentation of map.

# Program 33

print("~~~~~~~~~~~~~~~~~Program 33~~~~~~~~~~~~~~~~~")

# List Comprehensions
# List comprehensions allow you to create a list on the fly in one elegant one-liner.
# We can implement this in our code as follows:

def mainFive():
    yellFive("This", "is", "CS50")

def yellFive(*wordsFour):
    uppercasedFour = [arg.upper() for arg in wordsFour]
    print(*uppercasedFour)

mainFive()

# Notice how instead of using map, we write a Python expression within square brackets. For each argument, .upper is
# applied to it.


