
# Program 1

print("~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~")

class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

def main():

   packages = [
        Package(number = 1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]

main()

# Program 2

print("~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~")

class PackageTwo:
    def __init__(self, numberTwo, senderTwo, recipientTwo, weightTwo):
        self.numberTwo = numberTwo
        self.senderTwo = senderTwo
        self.recipientTwo = recipientTwo
        self.weightTwo = weightTwo

def mainTwo():

   packagesTwo = [
        PackageTwo(numberTwo = 1, senderTwo="Alice", recipientTwo="Bob", weightTwo=10),
        PackageTwo(numberTwo=2, senderTwo="Bob", recipientTwo="Charlie", weightTwo=5)
    ]
   for package in packagesTwo:
       print(f"Package {package.numberTwo}: {package.senderTwo} to {package.recipientTwo}, {package.weightTwo}kg")

mainTwo()


# Program 3

print("~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~")

class PackageThree:
    def __init__(self, numberThree, senderThree, recipientThree, weightThree):
        self.numberThree = numberThree
        self.senderThree = senderThree
        self.recipientThree = recipientThree
        self.weightThree = weightThree

def mainThree():

   packagesThree = [
        PackageThree(numberThree = 1, senderThree="Alice", recipientThree="Bob", weightThree=10),
        PackageThree(numberThree=2, senderThree="Bob", recipientThree="Charlie", weightThree=5)
    ]
   for packageTwo in packagesThree:
       print(packageTwo)


mainThree()


# Program 4

print("~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~")

class PackageFour:
    def __init__(self, numberFour, senderFour, recipientFour, weightFour):
        self.numberFour = numberFour
        self.senderFour = senderFour
        self.recipientFour = recipientFour
        self.weightFour = weightFour

    def __str__(self):
        return "This is a package."

def mainFour():

   packagesFour = [
        PackageFour(numberFour = 1, senderFour="Alice", recipientFour="Bob", weightFour=10),
        PackageFour(numberFour=2, senderFour="Bob", recipientFour="Charlie", weightFour=5)
    ]
   for packageThree in packagesFour:
       print(packageThree)


mainFour()

# Program 5

print("~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~")

class PackageFive:
    def __init__(self, numberFive, senderFive, recipientFive, weightFive):
        self.numberFive = numberFive
        self.senderFive = senderFive
        self.recipientFive = recipientFive
        self.weightFive = weightFive

    def __str__(self):
        return f"{self.numberFive}: {self.senderFive} to {self.recipientFive}, {self.weightFive}kg"

def mainFive():

   packagesFive = [
        PackageFive(numberFive = 1, senderFive="Alice", recipientFive="Bob", weightFive=10),
        PackageFive(numberFive=2, senderFive="Bob", recipientFive="Charlie", weightFive=5)
    ]
   for packageFour in packagesFive:
       print(packageFour)


mainFive()

# Program 6

print("~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~")

class PackageSix:
    def __init__(self, numberSix, senderSix, recipientSix, weightSix):
        self.numberSix = numberSix
        self.senderSix = senderSix
        self.recipientSix = recipientSix
        self.weightSix = weightSix

    def __str__(self):
        return f"{self.numberSix}: {self.senderSix} to {self.recipientSix}, {self.weightSix}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weightSix * cost_per_kg


def mainSix():

   packagesSix = [
        PackageSix(numberSix = 1, senderSix="Alice", recipientSix="Bob", weightSix=10),
        PackageSix(numberSix=2, senderSix="Bob", recipientSix="Charlie", weightSix=5)
    ]
   for packageFive in packagesSix:
       print(f"{packageFive} costs {packageFive.calculate_cost(cost_per_kg=2)}")


mainSix()

# Program 7

print("~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~")

class PackageSeven:
    def __init__(self, numberSeven, senderSeven, recipientSeven, weightSeven):
        self.numberSeven = numberSeven
        self.senderSeven = senderSeven
        self.recipientSeven = recipientSeven
        self.weightSeven = weightSeven

    def __str__(self):
        return f"{self.numberSeven}: {self.senderSeven} to {self.recipientSeven}, {self.weightSeven}kg"

    def calculate_cos_two(self, cost_per_kg_two):
        return self.weightSeven * cost_per_kg_two


def mainSeven():

   packagesSeven = [
        PackageSeven(numberSeven = 1, senderSeven="Alice", recipientSeven="Bob", weightSeven=10),
        PackageSeven(numberSeven=2, senderSeven="Bob", recipientSeven="Charlie", weightSeven=5)
    ]
   for packageSix in packagesSeven:
       print(f"{packageSix} costs ${packageSix.calculate_cos_two(cost_per_kg_two=2)}")


mainSeven()