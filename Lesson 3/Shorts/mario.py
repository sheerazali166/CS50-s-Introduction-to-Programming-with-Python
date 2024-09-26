
# Program 1

print("~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~")

def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * i)

if __name__ == "__main__":
    main()


# Program 2

print("~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~")

def mainTwo():
    heightTwo = int(input("heightTwo: "))
    pyramidTwo(heightTwo)


def pyramidTwo(nTwo):
    for iTwo in range(nTwo):
        print(iTwo, end=" ")
        print("#" * iTwo)

mainTwo()

# Program 3

print("~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~")

def mainThree():
    heightThree = int(input("heightThree: "))
    pyramidThree(heightThree)


def pyramidThree(nThree):
    for iThree in range(nThree):
        print("#" * (iThree + 1))

mainThree()


# Program 4

# Debugging

print("~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~")

def mainFour():
    heightFour = int(input("heightFour: "))
    pyramidFour(heightFour)


def pyramidFour(nFour):
    for iFour in range(nFour):
        print("#" * iFour)

# Apply breakpoint at mainFour()
mainFour()

# Program 5

print("~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~")

def mainFive():
    heightFive = int(input("heightFive: "))
    pyramidFive(heightFive)


def pyramidFive(nFive):
    for iFive in range(nFive):
        print("#" * (iFive + 1))

mainFive()