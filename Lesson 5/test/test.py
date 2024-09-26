
from hello import hello

# Program 17

print("~~~~~~~~~~~~~~~~~Program 17~~~~~~~~~~~~~~~~~")


# Organizing Tests into Folders

# Unit testing code using multiple tests is so common that you have the ability to run a whole folder of tests
# with a single command.
# First, in the terminal window, execute mkdir test to create a folder called test
# Then, to create a test within that folder, type in the terminal window code test/test_hello.py. Notice that test/
# instructs the terminal to create test_hello.py in the folder called test.
# In the text editor window, modify the file to include the following code:

# def test_default():
    # assert  hello() == "hello, world"

 # def test_argument():
     # assert hello("David") == "hello, David"

# Notice that we are creating a test just as we did before.
# pytest will not allow us to run tests as a folder simply with this file (or a whole set of files) alone without
# a special __init__ file. In your terminal window, create this file by typing code test/__init__.py. Note the
# test/ as before, as well as the double
# underscores on either side of init. Even leaving this __init__.py file empty, pytest is informed that the whole
# folder containing __init__.py has tests that can be run.

# Now, typing pytest test in the terminal, you can run the entire test folder of code.

# You can learn more in Pytest’s documentation of import mechanisms.

# Summing Up

# Testing your code is a natural part of the programming process. Unit tests allow you to test specific aspects of
# your code. You can create your own programs that test your code. Alternatively, you can utilize frameworks like
# pytest to run your unit tests for you. In this lecture, you learned about…

# 1. Unit tests
# 2. assert
# 3. pytest







