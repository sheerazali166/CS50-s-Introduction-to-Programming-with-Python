
# Program 34

print("~~~~~~~~~~~~~~~~~Program 34~~~~~~~~~~~~~~~~~")

# Taking this concept further, let’s pivot toward another program.
# In the text editor window, type code gryffindors.py and code as follows:

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

gryffindors = []

for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)

# Notice we have a conditional while we’re creating our list. If the student’s house is Gryffindor, we append the
# student to the list of names. Finally, we print all the names.

# Program 35

print("~~~~~~~~~~~~~~~~~Program 35~~~~~~~~~~~~~~~~~")

# More elegantly, we can simplify this code with a list comprehension as follows:

studentsTwo = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

gryffindorsTwo = [student["name"] for student in studentsTwo if student["house"] == "Gryffindor"]

for gryffindorTwo in sorted(gryffindorsTwo):
    print(gryffindorTwo)

# Notice how the list comprehension is on a single line!

# Program 36

print("~~~~~~~~~~~~~~~~~Program 36~~~~~~~~~~~~~~~~~")

# filter

# Using Python’s filter function allows us to return a subset of a sequence for which a certain condition is true.
# In the text editor window, code as follows:

studentsThree = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindorsThree = filter(is_gryffindor, studentsThree)

for gryffindorThree in sorted(gryffindorsThree, key=lambda s: s["name"]):
    print(gryffindorThree["name"])

# Program 37

print("~~~~~~~~~~~~~~~~~Program 37~~~~~~~~~~~~~~~~~")

# Notice how a function called is_gryffindor is created. This is our filtering function that will take a student s,
# and return True or False depending on whether the student’s house is Gryffindor. You can see the new filter function
# takes two arguments. First, it takes the function that will be applied to each element in a sequence—in this case,
# is_gryffindor. Second, it takes the sequence to which it will apply the filtering function—in this case, students.
# In gryffindors, we should see only those students who are in Gryffindor.

# filter can also use lambda functions as follows:

studentsFour = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

gryffindorsFour = filter(lambda sTwo: sTwo["house"] == "Gryffindor", studentsFour)

for gryffindorFour in sorted(gryffindorsFour, key=lambda sThree: sThree["name"]):
    print(gryffindorFour["name"])

# Notice how the same list of students is provided.
# You can learn more in Python’s documentation of filter.

# Program 38

print("~~~~~~~~~~~~~~~~~Program 38~~~~~~~~~~~~~~~~~")

# Dictionary Comprehensions

# We can apply the same idea behind list comprehensions to dictionaries. In the text editor window, code as follows:

studentsFive = ["Hermione", "Harry", "Ron"]

gryffindorsFive = []

for studentTwo in studentsFive:
    gryffindorsFive.append({"name": studentTwo, "house": "Gryffindor"})

print(gryffindorsFive)

# Notice how this code doesn’t (yet!) use any comprehensions. Instead, it follows the same paradigms we have seen
# before.

# Program 39

print("~~~~~~~~~~~~~~~~~Program 39~~~~~~~~~~~~~~~~~")

# We can now apply dictionary comprehensions by modifying our code as follows:
studentsSix = ["Hermione", "Harry", "Ron"]

gryffindorsSix = [{"name": studentsSix, "house": "Gryffindor"} for studentThree in studentsSix]
print(gryffindorsSix)

# Notice how all the prior code is simplified into a single line where the structure of the dictionary is provided for
# each student in students.

# Program 40

print("~~~~~~~~~~~~~~~~~Program 40~~~~~~~~~~~~~~~~~")

# We can even simplify further as follows:

studentsSeven = ["Hermione", "Harry", "Ron"]

gryffindorsSeven = { studentFour: "Gryffindor" for studentFour in studentsSeven }
print(gryffindorsSeven)

# Notice how the dictionary will be constructed with key-value pairs.

# Program 41

print("~~~~~~~~~~~~~~~~~Program 41~~~~~~~~~~~~~~~~~")

# enumerate

# We may wish to provide some ranking of each student. In the text editor window, code as follows:

studentsEight = ["Harry", "Hermione", "Ron"]

for i in range(len(studentsEight)):
    print(i + 1, studentsEight[i])

# Notice how each student is enumerated when running this code.

# Program 42

print("~~~~~~~~~~~~~~~~~Program 42~~~~~~~~~~~~~~~~~")

# Utilizing enumeration, we can do the same:

studentsNine = ["Harry", "Hermione", "Ron"]

for iTwo, studentFive in enumerate(studentsNine):
    print(iTwo + 1, studentFive)

# Notice how enumerate presents the index and the value of each student.
# You can learn more in Python’s documentation of enumerate.






