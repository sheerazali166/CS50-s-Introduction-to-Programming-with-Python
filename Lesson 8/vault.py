
# Program 28

print("~~~~~~~~~~~~~~~~Program 28~~~~~~~~~~~~~~~~")

# Operator Overloading

# Some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.
# In your terminal window, type code vault.py. Then, code as follows:

# Operator Overloading

# Some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.
# In your terminal window, type code vault.py. Then, code as follows:

class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles {self.knuts} Knuts"

    def __add__(self, other):
        galleonstwo = self.galleons + other.galleons
        sicklesTwo = self.sickles + other.sickles
        knutsTwo = self.knuts + other.knuts
        return Vault(galleonstwo, sicklesTwo, knutsTwo)

harryPotter = Vault(100, 50, 25)
print(harryPotter)

ronWeasley = Vault(25, 50, 100)
print(ronWeasley)

total = harryPotter + ronWeasley
print(total)

# This is problem 2 same values
# 125 Galleons, 100 Sickles 125 Knuts
# You are deamon

# winner can be only one if you flip a coin
# please don't use imf dogi mamas have future plans also

# Notice how the __str__ method returns a formatted string. Further, notice how the __add__ method allows for the
# addition of the values of two vaults. self is what is on the left of the + operand. other is what is right of the +.

# You can learn more in Python’s documentation of operator overloading.

# Summing Up

# Now, you’ve learned a whole new level of capability through object-oriented programming.

# Object-oriented programming
# Classes
# raise
# Class Methods
# Static Methods
# Inheritance
# Operator Overloading





