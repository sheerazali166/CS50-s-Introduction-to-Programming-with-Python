from anyio import sleep

# Program 43

print("~~~~~~~~~~~~~~~~~Program 43~~~~~~~~~~~~~~~~~")

# Generators and Iterators

# In Python, there is a way to protect against your system running out of resources the problems they are addressing
# become too large.

# In the United States, it’s customary to “count sheep” in one’s mind when one is having a hard time falling asleep.
# In the text editor window, type code sleep.py and code as follows:

n = int(input("What's n? "))

for i in range(n):
    print("🐑" * i)

# Notice how this program will count the number of sheep you ask of it.

# Program 44

print("~~~~~~~~~~~~~~~~~Program 44~~~~~~~~~~~~~~~~~")

# We can make our program more sophisticated by adding a main function by coding as follows:

def main():
    nTwo = int(input("What's n? "))
    for iTwo in range(nTwo):
        print("🐑", iTwo)

main()

# Program 45

print("~~~~~~~~~~~~~~~~~Program 45~~~~~~~~~~~~~~~~~")

# We have been getting into the habit of abstracting away parts of our code.
# We can call a sheep function by modifying our code as follows:

def mainTwo():
    nFour = int(input("What's nFour? "))
    for iThree in range(nFour):
        print(sheep(iThree))

def sheep(nThree):
    return "🐑" * nThree

mainTwo()

# Notice how the main function does the iteration

# Program 46

print("~~~~~~~~~~~~~~~~~Program 46~~~~~~~~~~~~~~~~~")

# We can provide the sheep function more abilities. In the text editor window, code as follows:

def mainThree():
    nSix = int(input("What's nSix? "))
    for s in sheep(nSix):
        print(s)


def sheepTwo(nFive):
    flock = []
    for iFour in range(nFive):
        flock.append("🐑" * iFour)
    return flock

mainThree()

# Notice how we create a flock of sheep and return the flock.

# Executing our code, you might try different numbers of sheep such as 10, 1000, and 10000. What if you asked for
# 1000000 sheep, your program might completely hang or crash. Because you have attempted to generate a massive list
# of sheep, your computer may be struggling to complete the computation.

# The yield generator can solve this problem by returning a small bit of the results at a time. In the text editor
# window, code as follows:

# Program 47

print("~~~~~~~~~~~~~~~~~Program 47~~~~~~~~~~~~~~~~~")

# The yield generator can solve this problem by returning a small bit of the results at a time. In the text editor
# window, code as follows:

def mainFour():
    nEight = int(input("What's nEight? "))
    for sTwo in sheepTwo(nEight):
        print(sTwo)

def sheepThree(nSeven):
    for iFive in range(nSeven):
        yield "🐑" * iFive

mainFour()

# Notice how yield provides only one value at a time while the for loop keeps working.
# You can learn more in Python’s documentation of generators.
# You can learn more in Python’s documentation of iterators.

# Congratulations!

# As you exit from this course, you have more of a mental model and toolbox to address programming-related problems.
# First, you learned about functions and variables.
# Second, you learned about conditionals.
# Third, you learned about loops.
# Fourth, you learned about exceptions.
# Fifth, you learned about libraries.
# Sixth, you learned about unit tests.
# Seventh, you learned about file I/O.
# Eighth, you learned about regular expressions.
# Most recently, you learned about object-oriented programming.
# Today, you learned about many other tools you can use.



