
# Program 1

print("~~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~~")

emotion = "v.v"

def main():
    say("Is anyone there?")

def say(phrase):
    print(phrase + " " + emotion)

main()

# Program 2

print("~~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~~")


emotionTwo = "v.v"

def mainTwo():
    sayTwo("Is anyone there?")
    sayTwo("Oh, hi!")

def sayTwo(phrase):
    print(phrase + " " + emotionTwo)

mainTwo()


# Program 3

print("~~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~~")


emotionThree = "v.v"

def mainThree():
    sayThree("Is anyone there?")
    emotionThree = ":D"
    sayThree("Oh, hi!")

def sayThree(phrase):
    print(phrase + " " + emotionThree)

mainThree()

# Program 4

print("~~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~~")


emotionFour = "v.v"

def mainFour():
    global emotionFour
    sayFour("Is anyone there?")
    emotionFour = ":D"
    sayFour("Oh, hi!")

def sayFour(phrase):
    print(phrase + " " + emotionFour)

mainFour()
