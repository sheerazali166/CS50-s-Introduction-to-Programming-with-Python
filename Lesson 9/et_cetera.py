
# Program 1

print("~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~")

# Et Cetera

# Over the many past lessons, we have covered so much related to Python!
# In this lesson, we will be focusing upon many of the “et cetera” items not previously discussed. “Et cetera”
# literally means “and the rest”!
# Indeed, if you look at the Python documentation, you will find quite “the rest” of other features.

# set

# In math, a set would be considered a set of numbers without any duplicates.
# In the text editor window, code as follows:

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Padma", "house": "Ravenclaw"}
]

houses = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

# Notice how we have a list of dictionaries, each being a student. An empty list called houses is created. We iterate
# through each student in students. If a student’s house is not in houses, we append to our list of houses.

# Program 2

print("~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~")

# It turns out we can use the built-in set features to eliminate duplicates.
# In the text editor window, code as follows:

studentsTwo = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

housesTwo = set()

for studentTwo in studentsTwo:
    housesTwo.add(studentTwo["house"])


for houseTwo in sorted(housesTwo):
    print(houseTwo)

# Notice how no checking needs to be included to ensure there are no duplicates. The set object takes care of this
# for us automatically.

# You can learn more in Python’s documentation of set.

# Program 3

print("~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~")

# Global Variables

# In other programming languages, there is the notion of global variables that are accessible to any function.
# We can leverage this ability within Python. In the text editor window, code as follows:

balance = 0

def main():
    print("Balance:", balance)

if __name__ == "__main__":
    main()

# Notice how we create a global variable called balance, outside of any function.

# Program 4

print("~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~")

# Since no errors are presented by executing the code above, you’d think all is well. However, it is not! In the text
# editor window, code as follows:

balanceTwo = 0

def mainTwo():
    print("balanceTwo:", balanceTwo)
    # deposit(100)
    # withdraw(50)
    print("balanceTwo:", balanceTwo)

# def deposit(n):
    # balanceTwo += n

# def withdraw(n):
    # balanceTwo -= n

mainTwo()

# Notice how we now add the functionality to add and withdraw funds to and from balance. However, executing this code,
# we are presented with an error! We see an error called UnboundLocalError. You might be able to guess that, at least
# in the way we’ve currently coded balance and our deposit and withdraw functions, we can’t reassign it a value value
# inside a function.

# Program 5

print("~~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~~")

# To interact with a global variable inside a function, the solution is to use the global keyword. In the text editor
# window, code as follows:

balanceThree = 0

def mainThree():
    print("balanceThree:", balanceThree)
    depositTwo(100)
    withdrawTwo(50)
    print("balanceThree:", balanceThree)

    # aisa mat kiya karo 100 daal kar 50 nikal rahi ho

def depositTwo(n):
    global balanceThree
    balanceThree += n

def withdrawTwo(n):
    global balanceThree
    balanceThree -= n

mainThree()

# Notice how the global keyword tells each function that balance does not refer to a local variable: instead, it
# refers to the global variable we originally placed at the top of our code. Now, our code functions!

# Program 6

print("~~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~~")

# Utilizing our powers from our experience with object-oriented programming, we can modify our code to use a class
# instead of a global variable. In the text editor window, code as follows:

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def mainFour():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

mainFour()

# Notice how we use account = Account() to create an account. Classes allow us to solve this issue of needing a
# global variable more cleanly because these instance variables are accessible to all the methods of this class
# utilizing self.

# Generally speaking, global variables should be used quite sparingly, if at all!

# Program 7

print("~~~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~~~")

# Constants

# Some languages allow you to create variables that are unchangeable, called “constants”. Constants allow one to
# program defensively and reduce the opportunities for important values to be altered.

# In the text editor window, code as follows:

MEOWS = 3

for _ in range(MEOWS):
    print("meow")

# Notice MEOWS is our constant in this case. Constants are typically denoted by capital variable names and are placed
# at the top of our code. Though this looks like a constant, in reality, Python actually has no mechanism to prevent
# us from changing that value within our code! Instead, you’re on the honor system: if a variable name is written in
# all caps, just don’t change it!

# Program 8

print("~~~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~~~")

# One can create a class “constant”, now in quotes because we know Python doesn’t quite support “constants”. In the
# text editor window, code as follows:

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()

# Because MEOWS is defined outside of any particular class method, all of them have access to that value via Cat.MEOWS.

# Program 9

print("~~~~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~~~~")

# Type Hints

# In other programming languages, one expresses explicitly what variable type you want to use.
# As we saw earlier in the course, Python does not require the explicit declaration of types.
# Nevertheless, it’s good practice need to ensure all of your variables are of the right type.
# mypy is a program that can help you test to make sure all your variables are of the right type.
# You can install mypy by executing in your terminal window: pip install mypy.

# In the text editor window, code as follows:

# def meow(n):
    # for _ in range(n):
        # print("meow")

# number = input("Number: ")
# meow(number)

# You may already see that number = input("Number: )" returns a string, not an int. But meow will likely want an int!

# Program 10

print("~~~~~~~~~~~~~~~~~Program 10~~~~~~~~~~~~~~~~~")

# A type hint can be added to give Python a hint of what type of variable meow should expect. In the text editor
# window, code as follows:

# def meowTwo(nTwo: int):
    # for _ in range(nTwo):
        # print("meow")

# numberTwo = input("numberTwo: ")
# meowTwo(numberTwo)

# Notice, though, that our program still throws an error.












