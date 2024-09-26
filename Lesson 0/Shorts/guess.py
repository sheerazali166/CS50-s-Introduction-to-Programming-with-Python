
# Program 1

print("~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~")

guess = 10
print(guess)

# Program 2

print("~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~")

def get_guess():
    guess = 10
    return guess

print(get_guess())

# Program 3

print("~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~")

def get_guessTwo():
    guess = input("Enter a guess: ")
    return guess

print(get_guessTwo())

# Program 4

print("~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~")

def get_guessThree():
    guess = input("Enter a guess: ")
    return guess

def main():
    get_guessThree()

main()

# Program 5

print("~~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~~")

def get_guessFour():
    guess = input("Enter a guess: ")
    return guess

def mainTwo():
    guess = get_guessFour()
    print(guess)

mainTwo()

# Program 6

print("~~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~~")

def get_guessFive():
    guess = input("Enter a guess: ")
    return guess

def mainThree():
    guess = get_guessFive()

    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")

mainThree()

# This is your Universe

# Program 6

print("~~~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~~~")

def get_guessSix():
    guess = int(input("Enter a guess: "))
    return guess

def mainFour():
    guess = get_guessSix()

    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")

mainFour()

print("~~~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~~~")

def get_guessSeven():
    guess = input("Enter a guess: ")
    return guess

def mainFive():
    guess = get_guessSeven()

    if guess == "fifty":
        print("Correct!")
    else:
        print("Incorrect!")

mainFive()