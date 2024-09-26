
# Program 1

print("~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~")

# Loops

# Essentially, loops are a way to do something over and over again.
# Begin by typing code cat.py in the terminal window.
# In the text editor, begin with the following code:

print("meow")
print("meow")
print("meow")

# Running this code by typing python cat.py, you’ll notice that the program meows three times.

# In developing as a programmer, you want to consider how one could improve areas of one’s code where one types the
# same thing over and over again. Imagine where one might want to “meow” 500 times. Would it be logical to type that
# same expression of print("meow") over and over again?

# Loops enable you to create a block of code that executes over and over again.

# Program 2

print("~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~")

# While Loops

# The while loop is nearly universal throughout all coding languages.
# Such a loop will repeat a block of code over and over again.
# In the text editor window, edit your code as follows:

# i = 3

# while i != 0:
    # print("meow")

# Notice how even though this code will execute print("meow") multiple times, it will never stop! It will loop forever.
# while loops work by repeatedly asking if the condition of the loop has been fulfilled. In this case, the compiler is
# asking, “does i not equal zero?” When you get stuck in a loop that executes forever, you can press control-c on your
# keyboard to break out of the loop.


# Program 3

print("~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~")

# To fix this loop that lasts forever, we can edit our code as follows

iTwo = 3
while iTwo != 0:
    print("meow")
    iTwo = iTwo - 1

# Notice that now our code executes properly, reducing i by 1 for each “iteration” through the loop. The term iteration
# has special significance within coding. By iteration, we mean one cycle through the loop. The first iteration is the
# “0th” iteration through the loop. The second is the “1st” iteration. In programming, we count starting with 0, then
# 1, then 2.


# Program 4

print("~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~")

# We can further improve our code as follows:

iThree = 1
while iThree <= 3:
    print("meow")
    iThree = iThree + 1


# Notice that when we code i = i + 1 we assign the value of i from the right to the left. Above, we are starting i at
# one, like most humans count (1, 2, 3). If you execute the code above, you’ll see it meows three times. It’s best
# practice in programming to begin counting with zero.


# Program 5

print("~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~")

# We can improve our code to start counting with zero:

iFour = 0
while iFour < 3:
    print("meow")
    iFour += 1


# Notice how changing the operator to i < 3 allows our code to function as intended. We begin by counting with 0
# and it iterates through our loop three times, producing three meows. Also, notice how i += 1 is the same as saying
# i = i + 1.


# Program 6

print("~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~")


# For Loops

# A for loop is a different type of loop.

# To best understand a for loop, it’s best to begin by talking about a new variable type called a list in Python. As in
# other areas of our lives, we can have a grocery list, a to-do list, etc.

# A for loop iterates through a list of items. For example, in the text editor window, modify your cat.py code as
# follows:

for iFive in [0, 1, 2]:
    print("meow")

# Notice how clean this code is compared to your previous while loop code. In this code, i begins with 0, meows, i is
# assigned 1, meows, and, finally, i is assigned 2, meows, and then ends.


# Program 7

print("~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~")

# While this code accomplishes what we want, there are some possibilities for improving our code for extreme cases.
# At first glance, our code looks great. However, what if you wanted to iterate up to a million? It’s best to create
# code that can work with such extreme cases. Accordingly, we can improve our code as follows:

for iSix in range(3):
    print("meow")

# Notice how range(3) provides back three values (0, 1, and 2) automatically. This code will execute and produce the
# intended effect, meowing three times.

# Program 8

print("~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~")

# Our code can be further improved. Notice how we never use i explicitly in our code. That is, while Python needs the
# i as a place to store the number of the iteration of the loop, we never use it for any other purpose. In Python, if
# such a variable does not have any other significance in our code, we can simply represent this variable as a single
# underscore _. Therefore, you can modify your code as follows:

for _ in range(3):
    print("meow")

# Notice how changing the i to _ has zero impact on the functioning of our program.

# Program 9

print("~~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~~")

print("meow" * 3)

# Notice how it will meow three times, but the program will produce meowmeowmeow as the result. Consider: How could you
# create a line break at the end of each meow?

# Program 10

print("~~~~~~~~~~~~~~~Program 10~~~~~~~~~~~~~~~")

# Indeed, you can edit your code as follows:
print("meow\n" * 3, end="")

# Notice how this code produces three meows, each on a separate line. By adding end="" and the \n we tell the compiler
# to add a line break at the end of each meow.


# Program 11

print("~~~~~~~~~~~~~~~Program 11~~~~~~~~~~~~~~~")

# Improving with User Input

# Perhaps we want to get input from our user. We can use loops as a way of validating the input of the user.
# A common paradigm within Python is to use a while loop to validate the input of the user.
# For example, let’s try prompting the user for a number greater than or equal 0:

################ Program 11 ################
# while True:
    # n = int(input("What's n? "))
    # if n < 0:
        # continue
    # else:
        # break

# Notice that we’ve introduced two new keywords in Python, continue and break. continue explicitly tells Python to go
# to the next iteration of a loop. break, on the other hand, tells Python to “break out” of a loop early before it has
# finished all of its iterations. In this case, we’ll continue to the next iteration of the loop when n is less than
# 0—ultimately reprompting the user with “What’s n?”. If, though, n is greater than or equal to 0, we’ll break out of
# the loop and allow the rest of our program to run


# Program 12

print("~~~~~~~~~~~~~~~Program 12~~~~~~~~~~~~~~~")

# It turns out that the continue keyword is redundant in this case. We can improve our code as follows:

################ Program 12 ################
# while True:
    # nTwo = int(input("What's nTwo? "))
    # if nTwo > 0:
        # break

# for _ in range(nTwo):
    # print("meow")

# Notice how this while loop will always run (forever) until n is greater than 0. When n is greater than 0, the
# loop breaks.


# Program 13

print("~~~~~~~~~~~~~~~Program 13~~~~~~~~~~~~~~~")


# Bringing in our prior learning, we can use functions to further improve our code:

def main():
    meow(get_number())

def get_number():
    while True:
        nThree = int(input("What's nThree? "))
        if nThree > 0:
            return nThree

def meow(nFour):
    for _ in range(nFour):
        print("meow")

main()

# Notice how not only did we change your code to operate in multiple functions, but we also used a return statement to
# return the value of n back to the main function.

