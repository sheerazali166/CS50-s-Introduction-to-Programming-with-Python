
# Program 14

print("~~~~~~~~~~~~~~~Program 14~~~~~~~~~~~~~~~")

# More About Lists

# Consider the world of Hogwarts from the famed Harry Potter universe.
# In the terminal, type code hogwarts.py.
# In the text editor, code as follows:

students = ["Hermione", "Harry", 'Ron']

print(students[0])
print(students[1])
print(students[2])

# Notice how we have a list of students with their names as above. We then print the student who is at the 0th
# location, “Hermoine”. Each of the other students is printed as well.


# Program 15

print("~~~~~~~~~~~~~~~Program 15~~~~~~~~~~~~~~~")

# Just as we illustrated previously, we can use a loop to iterate over the list. You can improve your code as follows:

studentsTwo = ["Hermione", "Harry", "Ron"]

for student in studentsTwo:
    print(student)

# Notice that for each student in the students list, it will print the student as intended. You might wonder why we did
# not use the _ designation as discussed prior. We choose not to do this because student is explicitly used in our code.

# You can learn more in Python’s documentation of lists.

# Program 16

print("~~~~~~~~~~~~~~~Program 16~~~~~~~~~~~~~~~")

# Length

# We can utilize len as a way of checking the length of the list called students.

# Imagine that you don’t simply want to print the name of the student but also their position in the list. To
# accomplish this, you can edit your code as follows:

studentsThree = ["Hermione", "Harry", "Ron"]

for i in range(len(studentsThree)):
    print(i + 1, studentsThree[i])

# Notice how executing this code results in not only getting the position of each student plus one using i + 1, but
# also prints the name of each student. len allows you to dynamically see how long the list of the students is
# regardless of how much it grows.

# You can learn more in Python’s documentation of len.


# Program 17

print("~~~~~~~~~~~~~~~Program 17~~~~~~~~~~~~~~~")


# Dictionaries

# dicts or dictionaries is a data structure that allows you to associate keys with values.
# Where a list is a list of multiple values, a dict associates a key with a value.
# Considering the houses of Hogwarts, we might assign specific students to specific houses.

# We could use lists alone to accomplish this:

studentsFour = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# Notice that we can promise that we will always keep these lists in order. The individual at the first position of
# students is associated with the house at the first position of the houses list, and so on. However, this can become
# quite cumbersome as our lists grow!


# Program 18

print("~~~~~~~~~~~~~~~Program 18~~~~~~~~~~~~~~~")


# We can better our code using a dict as follows:

studentsFive = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(studentsFive["Hermione"])
print(studentsFive["Harry"])
print(studentsFive["Ron"])
print(studentsFive["Draco"])

# Notice how we use {} curly braces to create a dictionary. Where lists use numbers to iterate through the list,
# dicts allow us to use words.

# Run your code and make sure your output is as follows:

# $ python hogwarts.py
# Gryffindor
# Gryffindor
# Gryffindor
# Slytherin


# Program 19

print("~~~~~~~~~~~~~~~Program 19~~~~~~~~~~~~~~~")


# We can improve our code as follows:

studentsSix = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for studentTwo in studentsSix:
    print(studentTwo)

# Notice how, executing this code, the for loop will only iterate through all the keys, resulting in a list of the
# names of the students. How could we print out both values and keys?


# Program 20

print("~~~~~~~~~~~~~~~Program 20~~~~~~~~~~~~~~~")


# We can clean up the print function by improving our code as follows:

studentsSeven = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for studentThree in studentsSeven:
    print(studentThree, studentsSeven[studentThree])

# Notice how students[student] will go to each student’s key and find the value of their house. Execute your code, and
# you’ll notice how the output is a bit messy.


# Program 21

print("~~~~~~~~~~~~~~~Program 21~~~~~~~~~~~~~~~")

# We can clean up the print function by improving our code as follows:

studentsEight = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for studentFour in studentsEight:
    print(studentFour, studentsEight[studentFour], sep=", ")

# Notice how this creates a clean separation of a , between each item printed.

# If you execute python hogwarts.py, you should see the following:

# $ python hogwarts.py
# Hermoine, Gryffindor
# Harry, Gryffindor
# Ron, Gryffindor
# Draco, Slytherin


# Program 22

print("~~~~~~~~~~~~~~~Program 22~~~~~~~~~~~~~~~")

# What if we have more information about our students? How could we associate more data with each of the students?
# You can imagine wanting to have lots of data associated with multiple keys. Enhance your code as follows:

studentsNine = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

# Notice how this code creates a list of dicts. The list called students has four dicts within it: One for each student.
# Also, notice that Python has a special None designation where there is no value associated with a key.


# Program 23

print("~~~~~~~~~~~~~~~Program 23~~~~~~~~~~~~~~~")

# Now, you have access to a whole host of interesting data about these students. Now, further modify your code as
# follows:

studentsTen = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for studentFive in studentsTen:
    print(studentFive["name"], studentFive["house"], studentFive["patronus"], sep=", ")

# Notice how the for loop will iterate through each of the dicts inside the list called students.
# You can learn more in Python’s Documentation of dicts.

# Program 24

print("~~~~~~~~~~~~~~~Program 24~~~~~~~~~~~~~~~")

# Mario

# Remember that the classic game Mario has a hero jumping over bricks. Let’s create a textual representation of this
# game.

# Begin coding as follows:

print("#")
print("#")
print("#")

# Notice how we are copying and pasting the same code over and over again.

# Program 25

print("~~~~~~~~~~~~~~~Program 25~~~~~~~~~~~~~~~")

# Consider how we could better the code as follows:

for _ in range(3):
    print("#")

# Notice how this accomplishes essentially what we want to create.

# Program 26

print("~~~~~~~~~~~~~~~Program 26~~~~~~~~~~~~~~~")

# Consider: Could we further abstract for solving more sophisticated problems later with this code? Modify your code as
# follows:

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

# Notice how our column can grow as much as we want without any hard coding.


# Program 27

print("~~~~~~~~~~~~~~~Program 27~~~~~~~~~~~~~~~")

# Now, let’s try to print a row horizontally. Modify your code as follows:

def mainTwo():
    print_row(4)

def print_row(width):
    print("?" * width)

mainTwo()

# Notice how we now have code that can create left-to-right blocks.


# Program 28

print("~~~~~~~~~~~~~~~Program 28~~~~~~~~~~~~~~~")

# Consider: How could we implement both rows and columns within our code? Modify your code as follows:

def mainThree():
    print_square(3)

def print_square(size):

    # for each row in square
    for i in range(size):

        # for each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        # Print blank line
        print()

mainThree()

# Notice that we have an outer loop that addresses each row in the square. Then, we have an inner loop that prints a
# brick in each row. Finally, we have a print statement that prints a blank line.


# Program 29

print("~~~~~~~~~~~~~~~Program 29~~~~~~~~~~~~~~~")

# We can further abstract away our code:

def mainFour():
    print_square_two(3)


def print_square_two(sizeTwo):
    for iTwo in range(sizeTwo):
        print_row_two(sizeTwo)


def print_row_two(widthTwo):
    print("#" * widthTwo)

mainFour()

# Program 30

print("~~~~~~~~~~~~~~~Program 30~~~~~~~~~~~~~~~")

# We can further abstract away our code:

def mainFive():
    print_square_three(4)


def print_square_three(sizeThree):
    for iThree in range(sizeThree):
        print_row_three(iThree)


def print_row_three(widthThree):
    print("#" * widthThree)

mainFive()


# Program 31

print("~~~~~~~~~~~~~~~Program 31~~~~~~~~~~~~~~~")

# We can further abstract away our code:

def mainSix():
    print_square_four(5)


def print_square_four(sizeFour):
    for iFour in range(sizeFour):
        print_row_four(iFour)


def print_row_four(widthFour):
    print("#" * widthFour)

mainSix()


# Program 30 And Program 31 ??

# Summing Up

# You now have another power in your growing list of your Python abilities. In this lecture, we addressed…

# 1. Loops
# 2. while
# 3. for
# 4. len
# 5. list
# 6. dict
