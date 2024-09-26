import re

# Program 25

print("~~~~~~~~~~~~~~~~~~Program 25~~~~~~~~~~~~~~~~~~")

# Extracting User Input

# So far, we have validated the user’s input and cleaned up the user’s input.

# Now, let’s extract some specific information from user input. In the terminal window, type code twitter.py and
# code as follows in the text editor window:

# url = input("URL: ").strip()
# print(url)

# Notice that if we type in https://twitter.com/davidjmalan, it shows exactly what the user typed. However, how would
# we be able to extract just the username and ignore the rest of the URL?

# Program 26

print("~~~~~~~~~~~~~~~~~~Program 26~~~~~~~~~~~~~~~~~~")

# You can imagine how we would simply be able to get rid of the beginning of the standard Twitter URL. We can attempt
# this as follows:

# urlTwo = input("URL: ").strip()

# username = urlTwo.replace("https://twitter.com/", "")
# print(f"Username: {username}")

# Notice how the replace method allows us to find one item and replace it with another. In this case, we are finding
# part of the URL and replacing it with nothing. Typing in the full URL https://twitter.com/davidjmalan, the program
# effectively outputs the username. However, what are some shortcomings of this current program?


# Program 27

print("~~~~~~~~~~~~~~~~~~Program 27~~~~~~~~~~~~~~~~~~")

# What if the user simply typed twitter.com instead of including the https:// and the like? You can imagine many
# scenarios where the user may input or neglect to input parts of the URL that would create strange output by this
# program. To improve this program, we can code as follows:

# urlThree = input("URL: ").strip()

# usernameTwo = urlThree.removeprefix("https://twitter.com/")
# print(f"Username: {usernameTwo}")

# Notice how we utilize the removeprefix method. This method will remove the beginning of a string.

# Program 28

print("~~~~~~~~~~~~~~~~~~Program 28~~~~~~~~~~~~~~~~~~")

# Regular expressions simply allow us to succinctly express the patterns and goals.
# Within the re library, there is a method called sub. This method allows us to substitute a pattern with something
# else.
# The signature of the sub method is as follows

# re.sub(pattern, repl, string, count=0, flags=0)

# Notice how pattern refers to the regular expression we are looking for. Then, there is a repl string that we can
# replace the pattern with. Finally, there is the string that we want to do the substitution on.

# import re

# urlFour = input("URL: ").strip()
# usernameThree = re.sub(r"https://www.twitter.com/", "", urlFour)
# print(f"Username: {usernameThree}")

# Notice how executing this program and inputting https://twitter.com/davidjmalan produces the correct outcome.
# However, there are some problems still present in our code.

# Program 29

print("~~~~~~~~~~~~~~~~~~Program 29~~~~~~~~~~~~~~~~~~")

# The protocol, subdomain, and the possibility that the user inputted any part of the URL after the username are all
# reasons that this code is still not ideal. We can further address these shortcomings as follows:

# import re

# urlFive = input("URL: ").strip()

# usernameFour = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", urlFive)
# print(f"Username: {usernameFour}")

# Notice how the ^ caret was added to the url. Notice also how the . could be interpreted improperly by the compiler.
# Therefore, we escape it using a \ to make it \. For the purpose of tolerating both http and https, we add a ? to
# the end of https?, making the s optional. Further, to accommodate www we add (www\.)? to our code. Finally, just
# in case the user decides to leave out the protocol altogether, the http:// or https:// is made optional
# using (https?://).

# Program 30

print("~~~~~~~~~~~~~~~~~~Program 30~~~~~~~~~~~~~~~~~~")

# Still, we are blindly expecting that what the user inputted a url that, indeed, has a username.
# Using our knowledge of re.search, we can further improve our code.

# urlSix = input("URL: ").strip()
# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", urlSix, re.IGNORECASE)

# if matches:
    # print("Username:", matches.group(2))

# Notice how we are searching for the regular expression above in the string provided by the user. In particular, we
# are capturing that which appears at the end of the URL using (.+)$ regular expression. Therefore, if the user fails
# to input a URL without a username, no input will be presented.

# Even further tightening up our program, we can utilize our := operator as follows:

# Program 31

print("~~~~~~~~~~~~~~~~~~Program 31~~~~~~~~~~~~~~~~~~")

# import re

# urlSeven = input("URL: ").strip()

# if matchesTwo := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", urlSeven, re.IGNORECASE):
    # print(f"Username:", matchesTwo.group(1))

# Notice that the ?: tells the compiler it does not have to capture what is in that spot in our regular expression.

# Program 32

print("~~~~~~~~~~~~~~~~~~Program 32~~~~~~~~~~~~~~~~~~")

# Still, we can be more explicit to ensure that the username inputted is correct. Using Twitter’s documentation, we
# can add the following to our regular expression:

import re

urlEight = input("URL: ").strip()

if matchesThree := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", urlEight, re.IGNORECASE):
    print("Username: ", matchesThree.group(1))

# Notice that the [a-z0-9_]+ tells the compiler to only expect a-z, 0-9, and _ as part of the regular expression.
# The + indicates that we are expecting one or more characters.

# You can learn more in Python’s documentation of re.

# Summing Up

# Now, you’ve learned a whole new language of regular expressions that can be utilized to validate, clean up, and
# extract user input.

# 1. Regular Expressions
# 2. Case Sensitivity
# 3. Cleaning Up User Input
# 4. Extracting User Input











