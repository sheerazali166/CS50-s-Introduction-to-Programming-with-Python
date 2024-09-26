
# Program 1

print("~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~")

# Unit Tests

# Up until now, you have been likely testing your own code using print statements.
# Alternatively, you may have been relying upon CS50 to test your code for you!
# It’s most common in industry to write code to test your own programs.

# In your console window, type code calculator.py. Note that you may have previously coded this file in a previous
# lecture. In the text editor, make sure that your code appears as follows:

def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return n * n

# def square(n):
    # return n + n

if __name__ == "__main__":
    main()


