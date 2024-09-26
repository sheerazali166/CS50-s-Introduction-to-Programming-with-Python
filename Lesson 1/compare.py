
# Program 1

print("~~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~~")


# if Statements
# n your terminal window, type code compare.py. This will create a brand new file called “compare.”
# In the text editor window, begin with the following:




############### Program 1 ###############
# x = int(input("what's x? "))
# y = int(input("What's y? "))

# if x < y:
    # print("x is less than y")


# Program 2

print("~~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~~")

# Control Flow, elif, and else
# Further revise your code as follows:

############### Program 2 ###############
# xTwo = int(input("What's xTwo? "))
# yTwo = int(input("What's yTwo? "))

# if xTwo < yTwo:
    # print("xTwo is less than yTwo")
# if xTwo > yTwo:
    # print("xTwo is greater than yTwo")
# if xTwo == yTwo:
    # print("xTwo is equal to yTwo")



# Notice how you are providing a series of if statements. First, the first if statement
# is evaluated. Then, the second if statement runs its evaluation. Finally, the last if statement runs its evaluation.
    
# This flow of decisions is called “control flow.”
# Our code can be represented as follows:


# Program 3

print("~~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~~")


# This program can be improved by not asking three consecutive questions. After all, not all three questions
# can have an outcome of true! Revise your program as follows:

############### Program 3 ###############
# xThree = int(input("What's xThree? "))
# yThree = int(input("What's yThree? "))

# if xThree < yThree:
    # print("xThree is less than yThree")
# elif xThree > yThree:
    # print("xThree is greater than yThree")
# elif xThree == yThree:
    # print("xThree is equal to yThree")


# Notice how the use of elif allows the program to make fewer decisions. First, the if statement is evaluated.
# If this statement is found to be true, all the elif statements will not be run at all. However, if the if statement
# is evaluated and found to be false, the first elif will be evaluated. If this is true, it will not run the final
# evaluation.

# Our code can be represented as follows:


# Program 4

print("~~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~~")

# While your computer may not notice a difference speed-wise between our first program and this revised program,
# consider how an online server running billions or trillions of these types of calculations each day could definitely
# be impacted by such a small coding decision.

# There is one final improvement we can make to our program. Notice how logically elif x == y is not a necessary
# evaluation to run. After all, if logically x is not less than y AND x is not greater than y, x MUST equal y.
# Therefore, we don’t have to run elif x == y. We can create a “catch-all,” default outcome using an else statement.
# We can revise as follows:

############### Program 4 ###############
# xFour = int(input("What's xFour? "))
# yFour = int(input("What's yFour? "))

# if xFour < yFour:
    # print("xFour is less than yFour")
# elif xFour > yFour:
    # print("xFour is greater than yFour")
# else:
    # print("xFour is equal to yFour")


# Program 5

print("~~~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~~~")

# OR
# or allows your program to decide between one or more alternatives. For example, we could further edit our program
# as follows:

############### Program 5 ###############
# xFive = int(input("What's xFive? "))
# yFive = int(input("What's yFive? "))

# if xFive < yFive or xFive > yFive:
    # print("xFive is not equal to yFive")
# else:
    # print("xFive is equal to yFive")


# Program 6

print("~~~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~~~")

# Notice that the result of our program is the same, but the complexity is decreased. The efficiency of our code
# is increased.

# At this point, our code is pretty great. However, could the design be further improved? We could further edit our
# code as follows:

############### Program 6 ###############
# xSix = int(input("What's xSix? "))
# ySix = int(input("What's ySix? "))

# if xSix != ySix:
    # print("xSix is not equal to ySix")
# else:
    # print("XSix is equal to ySix")


# Program 7

print("~~~~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~~~~")

# Notice how we removed the or entirely and simply asked, “Is x not equal to y?” We ask one and only one question.
# Very efficient!

# For the purpose of illustration, we could also change our code as follows:

xSeven = int(input("What's xSeven? "))
ySeven = int(input("What's ySeven? "))

if xSeven == ySeven:
    print("xSeven is equal to ySeven")
else:
    print("xSeven is not equal to ySeven")



