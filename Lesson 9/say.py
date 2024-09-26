
# Program 48

print("~~~~~~~~~~~~~~~~~Program 48~~~~~~~~~~~~~~~~~")

# This was CS50!
# Creating a final program together, type code say.py in your terminal window and code as follows:

import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")

cowsay.cow(this)
engine.say(this)
engine.runAndWait()


# Notice how running this program provides you with a spirited send-off.
# Our great hope is that you will use what you learned in this course to address real problems in the world, making
# our globe a better place.
# This was CS50!
