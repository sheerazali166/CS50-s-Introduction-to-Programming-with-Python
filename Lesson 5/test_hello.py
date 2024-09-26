
# Program 14

print("~~~~~~~~~~~~~~~~Program 14~~~~~~~~~~~~~~~~")

# Consider the following code for test_hello.py:

# from hello import hello

# def test_hello():
    # assert hello("david") == "hello, David"
    # assert hello() == "hello, world"

# Looking at this code, do you think that this approach to testing will work well? Why might this test not work well?
# Notice that the hello function in hello.py prints something: That is, it does not return a value!

# We can change our hello function within hello.py as follows:

# Program 15

print("~~~~~~~~~~~~~~~~Program 15~~~~~~~~~~~~~~~~")

from hello import hello

def main():
    name = int(input("What's your name? "))
    print(hello(name))

if __name__ == "__main__":
    main()

# Notice that we changed our hello function to return a string. This effectively means that we can now use pytest to
# test the hello function.

# Program 16

print("~~~~~~~~~~~~~~~~Program 16~~~~~~~~~~~~~~~~")

# Running pytest test_hello.py, our code will pass all tests!
# As with our previous test case in this lesson, we can break out our tests separately:

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

# Notice that the above code separates our test into multiple functions such that they will all run, even if an error
# is produced.

# Organizing Tests into Folders





