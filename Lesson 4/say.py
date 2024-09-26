
# Program 1

print("~~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~~")


# Packages

# One of the reasons Python is so popular is that there are numerous powerful third-party libraries that add
# functionality. We call these third-party libraries, implemented as a folder, “packages”.

# PyPI is a repository or directory of all available third-party packages currently available.
# cowsay is a well-known package that allows a cow to talk to the user.

# Python has a package manager called pip that allows you to install packages quickly onto your system.

# In the terminal window, you can install the cowsay package by typing pip install cowsay. After a bit of output, you
# can now go about using this package in your code.

# In your terminal window type code say.py. In the text editor, code as follows:

import cowsay
import sys

# if len(sys.argv) == 2:
    # cowsay.cow("hello, " + sys.argv[1])

# Notice that the program first checks that the user inputted at least two arguments at the command line. Then, the
# cow should speak to the user. Type python say.py David and you’ll see a cow saying “hello” to David.


# Program 2

print("~~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~~")

# Further modify your code:

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

# Notice that a t-rex is now saying “hello”.
# You now can see how you could install third-party packages.
# You can learn more on PyPI’s entry for cowsay
# You can find other third-party packages at PyPI


# Program 3

print("~~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~~")

# Let’s see how we could implement code utilizing this package that we created. In the terminal window, type code
# say.py. In this new file in your text editor, type the following:

import sys
from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

# Notice that this code imports the abilities of goodbye from the sayings package. If the user inputed at least two
# arguments at the command line, it will say “goodbye” along with the string inputed at the command line.

# Summing Up

# Libraries extend the abilities of Python. Some libraries are included by default with Python and simply need to be
# imported. Others are third-party packages that need to be installed using pip. You can make your own packages for
# use by yourself or others! In this lecture, you learned about…

# 1. Libraries
# 2. Random
# 3. Statistics
# 4. Command-Line Arguments
# 5. Slice
# 6. Packages
# 7. APIs
# 8. Making Your Own Libraries

