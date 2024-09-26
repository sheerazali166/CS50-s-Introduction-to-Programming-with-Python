
# Program 25

print("~~~~~~~~~~~~~~~~Program 25~~~~~~~~~~~~~~~~")

# Class Methods

# Sometimes, we want to add functionality to a class itself, not to instances of that class.
# @classmethod is a function that we can use to add functionality to a class as a whole.
# Here’s an example of not using a class method. In your terminal window, type code hat.py and code as follows:

import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")

# Notice how when we pass the name of the student to the sorting hat, it will tell us what house is assigned to the
# student. Notice that hat = Hat() instantiates a hat. The sort functionality is always handled by the instance of the
# class Hat. By executing hat.sort("Harry"), we pass the name of the student to the sort method of the particular
# instance of Hat, which we’ve called hat.


# Program 26

print("~~~~~~~~~~~~~~~~Program 26~~~~~~~~~~~~~~~~")

# We may want, though, to run the sort function without creating a particular instance of the sorting hat (there’s
# only one, after all!). We can modify our code as follows:

import random

class HatTwo:
    housesTwo = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, nameTwo):
        print(nameTwo, "is in", random.choice(cls.housesTwo))

HatTwo.sort("Harry")

# Notice how the __init__ method is removed because we don’t need to instantiate a hat anywhere in our code. self,
# therefore, is no longer relevant and is removed. We specify this sort as a @classmethod, replacing self with cls.
# Finally, notice how Hat is capitalized by convention near the end of this code, because this is the name of
# our class.


