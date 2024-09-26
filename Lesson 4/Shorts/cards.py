

# Program 1

print("~~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~~")

import random

cards = ["jack", "queen", "king"]

def main():
    print(random.choice(cards))

main()


# Program 2

print("~~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~~")

import random

cardsTwo = ["jack", "queen", "king"]

def mainTwo():
    print(random.sample(cardsTwo, k=2))

mainTwo()


# Program 3

print("~~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~~")

import random

cardsThree = ["jack", "queen", "king"]

def mainThree():
    print(random.choices(cardsThree, weights=[100, 0, 0], k=2))

mainThree()


# Program 4

print("~~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~~")

import random

cardsFour = ["jack", "queen", "king"]

def mainFour():
    print(random.choices(cardsThree, weights=[75, 20, 5], k=2))

mainFour()


# Program 5

print("~~~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~~~")

import random

cardsFive = ["jack", "queen", "king"]

def mainFive():
    random.seed(0)
    print(random.choices(cardsThree,k=2))

mainFive()


# Program 6

print("~~~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~~~")

import random

cardsSix = ["jack", "queen", "king"]

def mainSix():
    random.seed(1)
    print(random.choices(cardsThree,k=2))

mainSix()
