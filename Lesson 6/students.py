
# Program 12

print("~~~~~~~~~~~~~~~~Program 12~~~~~~~~~~~~~~~~")


# Let’s create a new program by typing code students.py and code as follows:

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# Notice that rstrip removes the end of each line in our CSV file. split tells the compiler where to find the end of
# each of our values in our CSV file. row[0] is the first element in each line of our CSV file. row[1] is the second
# element in each line in our CSV file.


# Program 13

print("~~~~~~~~~~~~~~~~Program 13~~~~~~~~~~~~~~~~")

# The above code is effective at dividing each line or “record” of our CSV file. However, it’s a bit cryptic to look at
# if you are unfamiliar with this type of syntax. Python has built-in ability that could further simplify this code.
# Modify your code as follows:

with open("students.csv") as file:
    for lineTwo in file:
        name, house = lineTwo.rstrip().split(",")
        print(f"{name} is in {house}")

# Imagine that we would again like to provide this list as sorted output? You can modify your code as follows:


# Program 14

print("~~~~~~~~~~~~~~~~Program 14~~~~~~~~~~~~~~~~")

students = []

with open("students.csv") as file:
    for lineThree in file:
        nameTwo, houseTwo = lineThree.rstrip().split(",")
        students.append(f"{nameTwo} is in {houseTwo}")


for student in sorted(students):
    print(student)

# Notice that we create a list called students. We append each string to this list. Then, we output a sorted version of
# our list.

# Program 15

print("~~~~~~~~~~~~~~~~Program 15~~~~~~~~~~~~~~~~")

# Recall that Python allows for dictionaries where a key can be associated with a value. This code could be further
# improved

studentsTwo = []

with open("students.csv") as file:
    for lineFour in file:
        nameThree, houseThree = lineFour.rstrip().split(",")
        studentTwo = {}
        studentTwo["name"] = nameThree
        studentTwo["house"] = houseThree
        studentsTwo.append(studentTwo)

for studentThree in studentsTwo:
    print(f"{studentThree['name']} is in {studentThree['house']}")

# Notice that we create an empty dictionary called student. We add the values for each student, including their name
# and house into the student dictionary. Then, we append that student to the list called students.


# Program 16

print("~~~~~~~~~~~~~~~~Program 16~~~~~~~~~~~~~~~~")

# We can improve our code to illustrate this as follows:

studentsThree = []

with open("students.csv") as file:
    for lineFive in file:
        nameFour, houseFour = lineFive.rstrip().split(",")
        studentFour = {"nameFour": nameFour, "houseFour": houseFour}
        studentsThree.append(studentFour)

for studentFive in studentsThree:
    print(f"{studentFive['nameFour']} is in {studentFive['houseFour']}")

# Notice that this produces the desired outcome, minus the sorting of students.


# Program 17

print("~~~~~~~~~~~~~~~~Program 17~~~~~~~~~~~~~~~~")

# Unfortunately, we cannot sort the students as we had prior because each student is now a dictionary inside of a list.
# It would be helpful if Python could sort the students list of student dictionaries that sorts this list of
# dictionaries by the student’s name.

# To implement this in our code, make the following changes:

studentsFour = []

with open("students.csv") as file:
    for lineSix in file:
        nameFive, houseFive = lineSix.rstrip().split(",")
        studentsFour.append({"nameFive": nameFive, "houseFive": houseFive})

def get_name(studentSix):
    return studentSix["nameFive"]

for studentSeven in sorted(studentsFour, key=get_name):
    print(f"{studentSeven['nameFive']} is in {studentSeven['houseFive']}")


# Notice that sorted needs to know how to get the key of each student. Python allows for a parameter called key where
# we can define on what “key” the list of students will be sorted. Therefore, the get_name function simply returns
# the key of student["name"]. Running this program, you will now see that the list is now sorted by name

# Program 18

print("~~~~~~~~~~~~~~~~Program 18~~~~~~~~~~~~~~~~")

# Still, our code can be further improved upon. It just so happens that if you are only going to use a function like
# get_name once, you can simplify your code in the manner presented below. Modify your code as follows:

studentsFive = []

with open("students.csv") as file:
    for lineSeven in file:
        nameSix, houseSix = lineSeven.rstrip().split(",")
        studentsFive.append({"nameSix": nameSix, "houseSix": houseSix})

for studentEight in sorted(studentsFive, key=lambda studentNine: studentNine["nameSix"]):
    print(f"{studentEight['nameSix']} is in {studentEight['houseSix']}")

# Notice how we use a lambda function, an anonymous function, that says “Hey Python, here is a function that has no
# name: Given a student, access their name and return that to the key.


# Program 19

print("~~~~~~~~~~~~~~~~Program 19~~~~~~~~~~~~~~~~")

# Notice how running our program how will produce a number of errors.
# Now that we’re dealing with homes instead of houses, modify your code as follows:

# studentsSix = []

# with open("studentsTwo.csv") as file:
    # for lineEight in file:
        # nameSeven, home = lineEight.rstrip().split(",")
        # studentsSix.append({"nameSeven": nameSeven, "home": home})

# ali amin gandapur
# for studentTen in sorted(key=lambda studentEleven: studentEleven["nameSeven"]):
    # print(f"{studentTen['nameSeven']} is in {studentTen['home']}")

# Notice that running our program still does not work properly. Can you guess why?

# The ValueError: too many values to unpack error produced by the compiler is a result of the fact that we previously
# created this program expecting the CSV file is split using a , (comma). We could spend more time addressing this,
# but indeed someone else has already developed a way to “parse” (that is, to read) CSV files!

# Program 20

print("~~~~~~~~~~~~~~~~Program 20~~~~~~~~~~~~~~~~")

# Python’s built-in csv library comes with an object called a reader. As the name suggests, we can use a reader to
# read our CSV file despite the extra comma in “Number Four, Privet Drive”. A reader works in a for loop, where each
# iteration the reader gives us another row from our CSV file. This row itself is a list, where each value in the list
# corresponds to an element in that row. row[0], for example, is the first element of the given row, while row[1] is
# the second element.

import csv

studentsSeven = []

with open("studentsTwo.csv") as file:
    reader = csv.reader(file)
    for rowTwo in reader:
        studentsSeven.append({"nameEight": rowTwo[0], "homeTwo": rowTwo[1]})

for studentTwelve in sorted(studentsSeven, key=lambda studentThirteen: studentThirteen["nameEight"]):
    print(f"{studentTwelve['nameEight']} is from {studentTwelve['homeTwo']}")

# Bravo

# Notice that our program now works as expected.

# Up until this point, we have been relying upon our program to specifically decide what parts of our CSV file are
# the names and what parts are the homes. It’s better design, though, to bake this directly into our CSV file by
# editing it as follows:

# name,home
# Harry,"Number Four, Privet Drive"
# Ron,The Burrow
# Draco,Malfoy Manor

# Notice how we are explicitly saying in our CSV file that anything reading it should expect there to be a name
# value and a home value in each line.


# Program 21

print("~~~~~~~~~~~~~~~~Program 21~~~~~~~~~~~~~~~~")

# We can modify our code to use a part of the csv library called a DictReader to treat our CSV file with even
# more flexibilty:

# import csv
#
# studentsEight = []
#
# with open("studentsTwo.csv") as file:
#     readerTwo = csv.DictReader(file)
#     for rowThree in readerTwo:
#         studentsEight.append({"nameNine":rowThree["nameNine"],"homeThree":rowThree["homeThree"]})
#
# for studentFourteen in sorted(studentsEight, key=lambda studentFifteen: studentFifteen["nameNine"]):
#     print(f"{studentFourteen['nameNine']} is in {studentFourteen['homeThree']}")

# Notice that we have replaced reader with DictReader, which returns one dictionary at a time. Also, notice that the
# compiler will directly access the row dictionary, getting the name and home of each student. This is an example of
# coding defensively. As long as the person designing the CSV file has inputted the correct header information on the
# first line, we can access that information using our program.

# Up until this point, we have been reading CSV files. What if we want to write to a CSV file?
# To begin, let’s clean up our files a bit. First, delete the students.csv file by typing rm students.csv in the
# terminal window. This command will only work if you’re in the same folder as your students.csv file.

# Program 22

print("~~~~~~~~~~~~~~~~Program 22~~~~~~~~~~~~~~~~")

# Then, in students.py, modify your code as follows:

import csv

nameEight = input("What's your nameEight? ")
homeTwo = input("Where is your homeTwo?")

with open("studentsThree.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["nameTen", "homeFour"])
    writer.writerow({"nameTen": nameEight, "homeFour": homeTwo})


# Notice how we are leveraging the built-in functionality of DictWriter, which takes two parameters: the file being
# written to and the fieldnames to write. Further, notice how the writerow function takes a dictionary as its
# parameter. Quite literally, we are telling the compiler to write a row with two fields called name and home.

# Note that there are many types of files that you can read from and write to.
# You can learn more in Python’s documentation of CSV.


