from calculator import square

# from calculator import square

# Program 2

print("~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~")

# Notice that you could plausibly test the above code on your own using some obvious numbers such as 2. However
# , consider why you might want to create a test that ensures that the above code functions appropriately.

# Following convention, let’s create a new test program by typing code test_calculator.py and modify your code in the
# text editor as follows:

# def main():
    # test_square()


# def test_square():
    # if square(2) != 4:
        # print("2 Squared was not 4")
    # if square(3) != 9:
        # print("3 squared was not 9")

# if __name__ == "__main__":
    # main()


# Notice that we are importing the square function from square.py on the first line of code. By convention, we are
# creating a function called test_square. Inside that function, we define some conditions to test.

# In the console window, type python test_calculator.py. You’ll notice that nothing is being outputted. It could be
# that everything is running fine! Alternatively, it could be that our test function did not discover one of the
# “corner cases” that could produce an error.

# Right now, our code tests two conditions. If we wanted to test many more conditions, our test code could easily
# become bloated. How could we expand our test capabilities without expanding our test code?

# Program 3

print("~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~")

# assert

# Python’s assert command allows us to tell the compiler that something, some assertion, is true. We can apply this to
# our test code as follows:

# def mainTwo():
    # test_square_two()

# def test_square_two():
    # assert square(2) == 4
    # assert square(3) == 9


# mainTwo()

# Notice that we are definitively asserting what square(2) and square(3) should equal. Our code is reduced from four
# test lines down to two.

# Program 4

print("~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~")

# We can purposely break our calculator code by modifying it as follows:

# def mainThree():
    # x = int(input("What's x? "))
    # print("x squared is", square_two(x))

# def square_two(n):
    # return n + n

# mainThree()

# Notice that we have changed the * operator to a + in the square function.


# Program 5

print("~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~")

# Now running python test_square.py in the console window, you will notice that an AssertionError is raised by the
# compiler. Essentially, this is the compiler telling us that one of our conditions was not met.

# One of the challenges that we are now facing is that our code could become even more burdensome if we wanted to
# provide more descriptive error output to our users. Plausibly, we could code as follows:

# from calculator import square

# def main():
    # test_square()

# def test_square():
    # try:
        # assert square(2) == 4
    # except AssertionError:
        # print("2 squared is not 4")
    # try:
        # assert square(3) == 9
    # except AssertionError:
        # print("3 squared is not 9")
    # try:
        # assert square(-2) == 4
    # except AssertionError:
        # print("-2 squared is not 4")
    # try:
        # assert square(-3) == 9
    # except AssertionError:
        # print("-3 squared is not 9")
    # try:
        # assert square(0) == 0
    # except AssertionError:
        # print("0 squared is not 0")

# if __name__ == "__main__":
    # main()

# Notice that running this code will produce multiple errors. However, it’s not producing all the errors above. This
# is a good illustration that it’s worth testing multiple cases such that you might catch situations where there
# are coding mistakes.

# The above code illustrates a major challenge: How could we make it easier to test your code without dozens of
# lines of code like the above?

# You can learn more in Python’s documentation of assert.


# Program 6

print("~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~")

# pytest

# pytest is a third-party library that allows you to unit test your program. That is, you can test your functions
# within your program.

# To utilize pytest please type pip install pytest into your console window.

# Before applying pytest to our own program, modify your test_calculator function as follows:

# from calculator import square

# def test_assert():
    # assert square(2) == 4
    # assert square(3) == 9
    # assert square(-2) == 4
    # assert square(-3) == 9
    # assert square(-3) == 9
    # assert square(0) == 0

# test_assert()
# Notice how the above code asserts all the conditions that we want to test.


# Program 7

print("~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~")

# pytest allows us to run our program directly through it, such that we can more easily view the results of our
# test conditions.

# In the terminal window, type pytest test_calculator.py. You’ll immediately notice that output will be provided.
# Notice the red

# F near the top of the output, indicating that something in your code failed. Further, notice that the red E provides
# some hints about the errors in your calculator.py program. Based upon the output, you can imagine a scenario where
# 3 * 3 has outputted 6 instead of 9. Based on the results of this test, we can go correct our calculator.py
# code as follows:

# def main():
    # x = int(input("What's x? "))
    # print("x squared is", square(x))

# def square(n):
    # return n * n

# if __name__ == "__main__":
    # main()

# Notice that we have changed the + operator to a * in the square function, returning it to a working state.


# Program 8

print("~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~")


# Re-running pytest test_calculator.py, notice how no errors are produced. Congratulations!

# At the moment, it is not ideal that pytest will stop running after the first failed test. Again, let’s return
# our calculator.py code back to its broken state:

# def main():
    # x = int(input("What's x? "))
    # print("x squared is", square(x))

# def square(n):
    # return n + n

# if __name__ == "__main__":
    # main()

# Notice that we have changed the * operator to a + in the square function, returning it to a broken state.


# Program 9

print("~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~")

# To improve our test code, let’s modify test_calculator.py to divide the code into different groups of tests:

# from calculator import square

# def test_positive():
    # assert square(2) == 4
    # assert square(3) == 9

# def test_negative():
    # assert square(-2) == 4
    # assert square(-3) == 9

# def test_zero():
    # assert square(0) == 0

# Notice that we have divided the same five tests into three different functions. Testing frameworks like pytest will
# run each function, even if there was a failure in one of them. Re-running pytest test_calculator.py, you will notice
# that many more errors are being displayed. More error output allows you to further explore what might be producing
# the problems within your code.


# Program 10

print("~~~~~~~~~~~~~~Program 10~~~~~~~~~~~~~~")

# Notice that we have divided the same five tests into three different functions. Testing frameworks like pytest
# will run each function, even if there was a failure in one of them. Re-running pytest test_calculator.py, you
# will notice that many more errors are being displayed. More error output allows you to further explore what
# might be producing the problems within your code.

# Having improved our test code, return your calculator.py code to fully working order:

# def main():
    # x = int(input("What's x? "))
    # print("x squared is", square(x))

# if __name__ == "__main__":
    # main()


# Program 11

print("~~~~~~~~~~~~~~Program 11~~~~~~~~~~~~~~")

# Notice that we have changed the + operator to a * in the square function, returning it to a working state.
# Re-running pytest test_calculator.py, you will notice that no errors are found.
# Finally, we can test that our program handles exceptions. Let’s modify test_calculator.py to do just that.

# import pytest

# def test_positive():
    # assert square(2) == 4
    # assert square(3) == 9

# def test_negative():
    # assert square(-2) == 4
    # assert square(-3) == 9

# def test_zero():
    # assert square(0) == 0

# def test_str():
    # with pytest.raises(TypeError):
        # square("cat")

# Notice that instead of using assert, we are taking advantage of a function within the pytest library itself called
# raises which allows you to express that you expect an error to be raised. We need to go to the top of our program
# and add import pytest and then call pytest.raises with the type of error we are expecting.


# Program 12

print("~~~~~~~~~~~~~~Program 12~~~~~~~~~~~~~~")

# Again, re-running pytest test_calculator.py, you will notice that no errors are found.
# In summary, it’s up to you as a coder to define as many test conditions as you see fit!

# You can learn more in Pytest’s documentation of pytest.










