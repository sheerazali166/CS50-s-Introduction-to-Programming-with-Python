
# Program 13

print("~~~~~~~~~~~~~~~Program 13~~~~~~~~~~~~~~~")

# Testing Strings

# Going back in time, consider the following code hello.py:

def main():
    name = input("What's your name? ")
    hello(name)

# def hello(to = "world"):
    # print("hello,", to)

if __name__ == "__main__":
    main()

# Notice that we may wish to test the result of the hello function.

# We can change our hello function within hello.py as follows:
def hello(to = "world"):
    return f"hello, {to}"
