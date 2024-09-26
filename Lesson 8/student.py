from pandas.core.indexes.accessors import Properties

# Program 1

print("~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~")

# Object-Oriented Programming

# There are different paradigms of programming. As you learn other languages, you will start recognizing patterns
# like these.

# Up until this point, you have worked procedurally step-by-step.
# Object-oriented programming (OOP) is a compelling solution to programming-related problems.
# To begin, type code student.py in the terminal window and code as follows:

# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")

# Notice that this program follows a procedural, step-by-step paradigm: Much like you have seen in prior parts of
# this course.

# Program 2

print("~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~")

# Drawing on our work from previous weeks, we can create functions to abstract away parts of this program.

# def main():
     # nameTwo = get_name()
     # houseTwo = get_house()

     # print(f"{nameTwo} from {houseTwo}")

# def get_name():
    # return input("Name: ")

# def get_house():
    # return input("House: ")

# if __name__ == '__main__':
    # main()

# Notice how get_name and get_house abstract away some of the needs of our main function. Further, notice how the
# final lines of the code above tell the compiler to run the main function.

# Program 3

print("~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~")

# We can further simplify our program by storing the student as a tuple. A tuple is a sequences of values. Unlike a
# list, a tuple can’t be modified. In spirit, we are returning two values.

# def mainTwo():
    # nameFour, houseFour = get_student()
    # print(f"{nameFour} from {houseFour}")

# def get_student():
    # nameThree = input("nameThree: ")
    # houseThree = input("houseThree: ")
    # return nameThree, houseThree

# mainTwo()

# Notice how get_student returns name, house

# Program 4

print("~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~")

# Packing that tuple, such that we are able to return both items to a variable called student, we can modify our code
# as follows.

# def mainThree():
    # student = get_student_two()
    # print(f"{student[0]} from {student[1]}")

# def get_student_two():
    # nameFive = input("nameFive: ")
    # houseFive = input("houseFive: ")
    # return (nameFive, houseFive)

# mainThree()

# Notice that (name, house) explicitly tells anyone reading our code that we are returning two values within one.
# Further, notice how we can index into tuples using student[0] or student[1]

# Program 5

print("~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~")

# tuples are immutable, meaning we cannot change those values. Immutability is a way by which we can program
# defensively.

# def mainFour():
    # studentTwo = get_student_three()
    # if studentTwo[0] == "Padma":
        # studentTwo[1] = "Ravenclaw"
    # print(f"{studentTwo[0]} from {studentTwo[1]}")

# def get_student_three():
    # nameSix = input("nameSix: ")
    # houseSix = input("houseSix: ")
    # return nameSix, houseSix

# mainFour()

# Notice that this code produces an error. Since tuples are immutable, we’re not able to reassign the value of
# student[1]

# Program 6

print("~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~")

# If we wanted to provide our fellow programmers flexibility, we could utilize a list as follows.

# def mainFive():
    # studentThree = get_student_four()
    # if studentThree[0] == "Padma":
        # studentThree[1] = "Revenclaw"
    # print(f"{studentThree[0]} from {studentThree[1]}")

# def get_student_four():
    # nameSix = input("nameSix: ")
    # houseSix = input("houseSix: ")
    # return [nameSix, houseSix]

# mainFive()

# Note the lists are mutable. That is, the order of house and name can be switched by a programmer. You might decide
# to utilize this in some cases where you want to provide more flexibility at the cost of the security of your code.
# After all, if the order of those values is changeable, programmers that work with you could make mistakes down
# the road.

# Program 7

print("~~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~~")

# A dictionary could also be utilized in this implementation. Recall that dictionaries provide a key-value pair.

# def mainSix():
    # studentFive = get_student_five()
    # print(f"{studentFive['nameSeven']} from {studentFive['houseSeven']}")

# def get_student_five():
    # studentFour = {}
    # studentFour["nameSeven"] = input("nameSeven: ")
    # studentFour["houseSeven"] = input("houseSeven: ")
    # return studentFour

# mainSix()

# Notice in this case, two key-value pairs are returned. An advantage of this approach is that we can index into this
# dictionary using the keys.

# Program 8

print("~~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~~")

# Still, our code can be further improved. Notice that there is an unneeded variable. We can remove student = {}
# because we don’t need to create an empty dictionary.

# def mainSeven():
    # studentSix = get_student_six()
    # print(f"{studentSix['nameEight']} from {studentSix['houseEight']}")

# def get_student_six():
    # nameEight = input("nameEight: ")
    # houseEight = input("houseEight: ")
    # return {"nameEight": nameEight, "houseEight": houseEight}

# mainSeven()

# Notice we can utilize {} braces in the return statement to create the dictionary and return it all in the same line.

# Program 9

print("~~~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~~~")

# We can provide our special case with Padma in our dictionary version of our code.

# def mainEight():
    # studentSeven = get_student_seven()
    # if studentSeven["nameNine"] == "Padma":
        # studentSeven["houseNine"] = "Ravenclaw"
    # print(f"{studentSeven['nameNine']} from {studentSeven['houseNine']}")


# def get_student_seven():
    # nameNine = input("nameNine: ")
    # houseNine = input("houseNine: ")

    # return {"nameNine": nameNine, "houseNine": houseNine}

# mainEight()

# Notice how, similar in spirit to our previous iterations of this code, we can utilize the key names to index into our
# student dictionary.

# Program 10

print("~~~~~~~~~~~~~~~~Program 10~~~~~~~~~~~~~~~~")

# Classes

# Classes are a way by which, in object-oriented programming, we can create our own type of data and give them names.
# A class is like a mold for a type of data – where we can invent our own data type and give them a name.
# We can modify our code as follows to implement our own class called Student:

# class Student:
    # ...

# def mainNine():
    # studentNine = get_student_eight()
    # print(f"{studentNine.nameTen}  from {studentNine.houseTen}")

# def get_student_eight():
    # studentEight = Student()
    # studentEight.nameTen = input("nameTen: ")
    # studentEight.houseTen = input("houseTen: ")
    # return studentEight


# mainNine()

# Notice by convention that Student is capitalized. Further, notice the ... simply means that we will later return to
# finish that portion of our code. Further, notice that in get_student, we can create a student of class Student using
# the syntax student = Student(). Further, notice that we utilize “dot notation” to access attributes of this
# variable student of class Student.

# Program 11

print("~~~~~~~~~~~~~~~~Program 11~~~~~~~~~~~~~~~~")

# Any time you create a class and you utilize that blueprint to create something, you create what is called an
# “object” or an “instance”. In the case of our code, student is an object.

# Further, we can lay some groundwork for the attributes that are expected inside an object whose class is Student.
# We can modify our code as follows:

# class StudentTwo:
    # def __init__(self, nameEleven, houseEleven):
        # self.nameEleven = nameEleven
        # self.houseEleven = houseEleven

# def get_student_nine():
    # nameTwelve = input("nameTwelve: ")
    # houseTwelve = input("houseTwelve: ")
    # studentTen = StudentTwo(nameTwelve, houseTwelve)
    # return studentTen

# def mainTen():
    # studentEleven = get_student_nine()
    # print(f"{studentEleven.nameEleven} from {studentEleven.houseEleven}")

# mainTen()

# Notice that within Student, we standardize the attributes of this class. We can create a function within class
# Student, called a “method”, that determines the behavior of an object of class Student. Within this function, it
# takes the name and house passed to it and assigns these variables to this object. Further, notice how the constructor
# student = Student(name, house) calls this function within the Student class and creates a student. self refers to
# the current object that was just created.


# Program 12

print("~~~~~~~~~~~~~~~~Program 12~~~~~~~~~~~~~~~~")

# We can simplify our code as follows:

# class StudentThree:
    # def __init__(self, nameThirteen, houseThirteen):
        # self.nameThirteen = nameThirteen
        # self.houseThirteen = houseThirteen

# def mainEleven():
    # studentTwelve = get_student_ten()
    # print(f"{studentTwelve.nameThirteen} from {studentTwelve.houseThirteen}")


# def get_student_ten():
    # nameFourteen = input("nameFourteen: ")
    # houseFourteen = input("houseFourteen: ")
    # return StudentThree(nameFourteen, houseFourteen)

# mainEleven()

# Notice how return Student(name, house) simplifies the previous iteration of our code where the constructor statement
# was run on its own line.

# You can learn more in Python’s documentation of classes.


# Program 13

print("~~~~~~~~~~~~~~~~Program 13~~~~~~~~~~~~~~~~")

# raise

# Object-oriented program encourages you to encapusulate all the functionality of a class within the class definition.
# What if something goes wrong? What if someone tries to type in something random? What if someone tries to create a
# student without a name? Modify your code as follows:

# class StudentFour:
    # def __init__(self, nameFifteen, houseFifteen):
        # if not nameFifteen:
            # raise ValueError("Missing nameFifteen")
        # if houseFifteen not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # raise ValueError("Invalid houseFifteen")
        # self.nameFifteen = nameFifteen
        # self.houseFifteen = houseFifteen

# def mainTwelve():
    # studentThirteen = get_student_eleven()
    # print(f"{studentThirteen.nameFifteen} from {studentThirteen.houseFifteen}")

# def get_student_eleven():
    # nameSixteen = input("nameSixteen: ")
    # houseSixteen = input("houseSixteen: ")
    # return StudentFour(nameSixteen, houseSixteen)

# mainTwelve()

# Notice how we check now that a name is provided and a proper house is designated. It turns out we can create our
# own exceptions that alerts the programmer to a potential error created by the user called raise. In the case above,
# we raise ValueError with a specific error message.

# Program 14

print("~~~~~~~~~~~~~~~~Program 14~~~~~~~~~~~~~~~~")

# It just so happens that Python allows you to create a specific function by which you can print the attributes of an
# object. Modify your code as follows:

# class StudentFive:
    # def __init__(self, nameSevenTeen, houseSeventeen, patronus):

        # if not nameSevenTeen:
            # raise ValueError("Missing nameSevenTeen")

        # if houseSeventeen not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # raise ValueError("Invalid houseSeventeen")

        # self.nameSeventeen = nameSevenTeen
        # self.houseSeventeen = houseSeventeen
        # self.patronus = patronus

    # def __str__(self):
        # return f"{self.nameSeventeen} from {self.houseSeventeen}"

# def mainThirteen():
    # studentFourteen = get_student_twelve()
    # print(studentFourteen)

# def get_student_twelve():
    # nameEighteen = input("nameEighteen: ")
    # houseEighteen = input("houseEighteen: ")
    # patronusTwo = input("patronusTwo: ")
    # return StudentFive(nameEighteen, houseEighteen, patronusTwo)

# mainThirteen()

# Notice how def __str__(self) provides a means by which a student is returned when called. Therefore, you can now, as
# the programmer, print an object, its attributes, or almost anything you desire related to that object.


# Program 15

print("~~~~~~~~~~~~~~~~Program 15~~~~~~~~~~~~~~~~")

# __str__ is a built-in method that comes with Python classes. It just so happens that we can create our own methods
# for a class as well! Modify your code as follows:

# class StudentSix:
    # def __init__(self, nameNineteen, houseNineteen, patronusTwo = None):
        # if not nameNineteen:
            # raise ValueError("Missing nameNineteen")
        # if houseNineteen not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # raise ValueError("Invalid houseNineteen")
        # if patronusTwo and patronusTwo not in ["Stag", "Otter", "Jack Russell terrier"]:
            # raise ValueError("Invalid patronusTwo")

        # self.nameNineteen = nameNineteen
        # self.houseNineteen = houseNineteen
        # self.patronusTwo = patronusTwo


    # def __str__(self):
        # return f"{self.nameNinteen} from {self.houseNinteen}"

    # def charm(self):
        # match self.patronusTwo:
            # case "Stag":
                # return "🐴"
            # case "Otter":
                # return "🦦"
            # case "Russell Jack terrier":
                # return "🐶"
            # case _:
                # return "🪄"

# def mainFourteen():
    # studentFifteen = get_student_thirteen()
    # print("Expecto Patronum!")
    # print(studentFifteen.charm())


# ef get_student_thirteen():
    # nameTwenty = input("nameTwenty: ")
    # houseTwenty = input("houseTwenty: ")
    # patronusThree = input("patronusThree: ") or None
    # return StudentSix(nameTwenty, houseTwenty, patronusThree)

# mainFourteen()

# Notice how we define our own method charm. Unlike dictionaries, classes can have built-in functions called methods.
# In this case, we define our charm method where specific cases have specific results. Further, notice that Python has
# the ability to utilize emojis directly in our code.

# Program 16

print("~~~~~~~~~~~~~~~~Program 16~~~~~~~~~~~~~~~~")

# Before moving forward, let us remove our patronus code. Modify your code as follows:

# class StudentSeven:
    # def __init__(self, nameTwentyOne, houseTwentyOne):
        # if not nameTwentyOne:
            # raise ValueError("Invalid nameTwentyOne")
        # if houseTwentyOne not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # raise ValueError("Invalid houseTwentyOne")

        # self.nameTwentyOne = nameTwentyOne
        # self.houseTwentyOne = houseTwentyOne

    # def __str__(self):
        # return f"{self.nameTwentyOne} from {self.houseTwentyOne}"

# def mainFifteen():
    # i also love this student
    # studentSixteen = get_student_fourteen()
    # studentSixteen.houseTwentyOne = "Number Four, Private Drive"
    # print(studentSixteen)

# def get_student_fourteen():
    # nameTwentyTwo = input("nameTwentyTwo: ")
    # houseTwentyTwo = input("houseTwentyTwo: ")
    # return StudentSeven(nameTwentyTwo, houseTwentyTwo)

# mainFifteen()

# Notice how we have only two methods: __init__ and __str__.


# Program 17

print("~~~~~~~~~~~~~~~~Program 17~~~~~~~~~~~~~~~~")

# Decorators

# Properties can be utilized to harden our code. In Python, we define properties using function “decorators”, which
# begin with @. Modify your code as follows:

# class StudentEight:
    # def __init__(self, nameTwentyThree, houseTwentyThree):
        # if not nameTwentyThree:
            # raise ValueError("Invalid nameTwentyThree")

        # self.nameTwentyThree = nameTwentyThree
        # self.houseTwentyThree = houseTwentyThree

    # def __str__(self):
        # return f"{self.nameTwentyThree} from {self.houseTwentyThree}"

    # Getter for house
    # @property
    # def house(self):
        # return self._house

    # Setter for house
    # @house.setter
    # def house(self, houseTwentyFour):
        # if houseTwentyFour not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # raise ValueError("houseTwentyFour")
        # self._house = houseTwentyFour

# def mainSixteen():
    # studentSeventeen = get_student_fifteen()
    # print(studentSeventeen)


# def get_student_fifteen():
    # nameTwentyFour = input("nameTwentyFour: ")
    # houseTwentyFive = input("houseTwentyFour: ")

    # return StudentEight(nameTwentyFour, houseTwentyFive)

# mainSixteen()

# Notice how we’ve written @property above a function called house. Doing so defines house as a property of our class.
# With house as a property, we gain the ability to define how some attribute of our class, _house, should be set and
# retrieved. Indeed, we can now define a function called a “setter”, via @house.setter, which will be called whenever
# the house property is set—for example, with student.house = "Gryffindor". Here, we’ve made our setter validate values
# of house for us. Notice how we raise a ValueError if the value of house is not any of the Harry Potter houses,
# otherwise, we’ll use house to update the value of _house. Why _house and not house? house is a property of our class,
# with functions via which a user attempts to set our class attribute. _house is that class attribute itself. The
# leading underscore, _, indicates to users they need not (and indeed, shouldn’t!) modify this value directly. _house
# should only be set through the house setter. Notice how the house property simply returns that value of _house, our
# class attribute that has presumably been validated using our house setter. When a user calls student.house, they’re
# getting the value of _house through our house “getter”.

# Program 18

print("~~~~~~~~~~~~~~~~Program 18~~~~~~~~~~~~~~~~")

# In addition to the name of the house, we can protect the name of our student as well. Modify your code as follows:

# class StudentNine:
    # def __init__(self, nameTwentyFive, houseTwentySix):
        # self.nameTwentyFive = nameTwentyFive
        # self.houseTwentySix = houseTwentySix

    # def __str__(self):
        # return f"{self.nameTwentyFive} from {self.houseTwentySix}"

    # Getter for name
    # @property
    # def name(self):
        # return self._name

    # Setter for name
    # @name.setter
    # def name(self, nameTwentySix):
        # if not nameTwentySix:
            # raise ValueError("nameTwentySix")
        # self._name = nameTwentySix

    # @property
    # def houseTwo(self):
        # return self._houseTwo

    # @houseTwo.setter
    # def houseTwo(self, houseTwentySeven):
        # if houseTwentySeven not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            # raise ValueError("Invalid houseTwentySeven")
        # self._houseTwo = houseTwentySeven

# def mainSeventeen():
    # studentEighteen = get_student_sixteen()
    # print(studentEighteen)


# def get_student_sixteen():
    # nameTwentySeven = input("nameTwentySeven: ")
    # houseTwentyEight = input("houseTwentyEight: ")
    # return StudentNine(nameTwentySeven, houseTwentyEight)

# mainSeventeen()

# Notice how, much like the previous code, we provide a getter and setter for the name.
# You can learn more in Python’s documentation of methods.


# Returning back to students.py we can modify our code as follows, addressing some missed opportunities related
# to @classmethods:

# Program 26

print("~~~~~~~~~~~~~~~~Program 26~~~~~~~~~~~~~~~~")

class StudentTen:
    def __init__(self, nameTwentyEight, houseTwentyNine):
        self.nameTwentyEight = nameTwentyEight
        self.houseTwentyNine = houseTwentyNine

    def __str__(self):
        return f"{self.nameTwentyEight} from {self.houseTwentyNine}"

    @classmethod
    def get(cls):
        nameTwentyNine = input("nameTwentyNine: ")
        houseThirty = input("houseThirty: ")
        return cls(nameTwentyNine, houseThirty)


def mainEighteen():
    studentNinteen = StudentTen.get()
    print(studentNinteen)

mainEighteen()

# Notice that get_student is removed and a @classmethod called get is created. This method can now be called without
# having to create a student first.


