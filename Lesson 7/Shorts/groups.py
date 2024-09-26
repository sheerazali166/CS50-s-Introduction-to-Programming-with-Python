
# Program 1

print("~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~")

# import re

# locations = {"1+": "United States and Canada", "+62": "Indonesia", "+505": "Nicargua"}

# def main():
    # pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
    # number = input("Number: ")

    # match = re.search(pattern, number)
    # if match:
        # print("Valid")
    # else:
        # print("Invalid")
# main()

# Program 2

print("~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~")

import re

# locationsTwo = {"1+": "United States and Canada", "+62": "Indonesia", "+505": "Nicargua"}

# def mainTwo():
    # patternTwo = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    # numberTwo = input("Number: ")

    # matchTwo = re.search(patternTwo, numberTwo)
    # if matchTwo:
        # country_code = matchTwo.group(1)
        # print(country_code)
    # else:
        # print("Invalid")
# mainTwo()

# Program 3

print("~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~")

# import re

# locationsThree = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicargua"}

# def mainThree():
    # patternThree = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    # numberThree = input("Number: ")

    # matchThree = re.search(patternThree, numberThree)
    # if matchThree:
        # country_code = matchThree.group(1)
        # print(locationsThree[country_code])
    # else:
        # print("Invalid")

# mainThree()

# Program 4

print("~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~")

import re

locationsFour = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicargua"}

def mainFour():
    patternFour = r"(?P<country_code_two>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    numberFour = input("Number: ")

    matchFour = re.search(patternFour, numberFour)
    if matchFour:
        country_code_three = matchFour.group("country_code_two")
        print(locationsFour[country_code_three])
    else:
        print("Invalid")

mainFour()