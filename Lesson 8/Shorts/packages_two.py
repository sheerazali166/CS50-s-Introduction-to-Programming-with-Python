
# Program 1

print("~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~")

class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight


def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]

    for package in packages:
        print(package.number)

main()

# Program 2

print("~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~")

class PackageTwo:
    def __init__(self, numberTwo, senderTwo, recipientTwo, weightTwo):
        self.numberTwo = numberTwo
        self.senderTwo = senderTwo
        self.recipientTwo = recipientTwo
        self.weightTwo = weightTwo


def mainTwo():
    packagesTwo = [
        PackageTwo(numberTwo=1, senderTwo="Alice", recipientTwo="Bob", weightTwo=10),
        PackageTwo(numberTwo=3, senderTwo="Bob", recipientTwo="Charlie", weightTwo=5)
    ]

    for packageTwo in packagesTwo:
        print(packageTwo.numberTwo)

mainTwo()

# Program 3

print("~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~")

class PackageThree:
    def __init__(self, numberThree, senderThree, recipientThree, weightThree):
        self.numberThree = numberThree
        self.senderThree = senderThree
        self.recipientThree = recipientThree
        self.weightThree = weightThree


def mainThree():
    packagesThree = [
        PackageThree(numberThree=1, senderThree="Alice", recipientThree="Bob", weightThree=10),
        PackageThree(numberThree=3, senderThree="Bob", recipientThree="Charlie", weightThree=5)
    ]

    for packageThree in packagesThree:
        print(f"Package {packageThree.numberThree}")

mainThree()

# Program 4

print("~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~")

class PackageFour:
    def __init__(self, numberFour, senderFour, recipientFour, weightFour):
        self.numberFour = numberFour
        self.senderFour = senderFour
        self.recipientFour = recipientFour
        self.weightFour = weightFour


def mainFour():
    packagesFour = [
        PackageFour(numberFour=1, senderFour="Alice", recipientFour="Bob", weightFour=10),
        PackageFour(numberFour=3, senderFour="Bob", recipientFour="Charlie", weightFour=5)
    ]

    for packageFour in packagesFour:
        print(f"Package {packageFour.numberFour}: {packageFour.senderFour} to {packageFour.recipientFour}")

mainFour()

# Program 4

print("~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~")

class PackageFour:
    def __init__(self, numberFour, senderFour, recipientFour, weightFour):
        self.numberFour = numberFour
        self.senderFour = senderFour
        self.recipientFour = recipientFour
        self.weightFour = weightFour


def mainFour():
    packagesFour = [
        PackageFour(numberFour=1, senderFour="Alice", recipientFour="Bob", weightFour=10),
        PackageFour(numberFour=3, senderFour="Bob", recipientFour="Charlie", weightFour=5)
    ]

    for packageFour in packagesFour:
        print(f"Package {packageFour.numberFour}: {packageFour.senderFour} to {packageFour.recipientFour}")

mainFour()

# Program 5

print("~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~")

class PackageFive:
    def __init__(self, numberFive, senderFive, recipientFive, weightFive):
        self.numberFive = numberFive
        self.senderFive = senderFive
        self.recipientFive = recipientFive
        self.weightFive = weightFive


def mainFive():
    packagesFive = [
        PackageFive(numberFive=1, senderFive="Alice", recipientFive="Bob", weightFive=10),
        PackageFive(numberFive=3, senderFive="Bob", recipientFive="Charlie", weightFive=5)
    ]

    for packageFive in packagesFive:
        print(f"Package {packageFive.numberFive}: {packageFive.senderFive} to {packageFive.recipientFive}, {packageFive.weightFive}kg")

mainFive()
