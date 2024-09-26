
# Program 1

print("~~~~~~~~~~~~Program 1~~~~~~~~~~~~")

# import re

# def main():
    # code = input("Hexadecimal color code: ")

    # pattern = r"#"
    # match = re.search(pattern, code)

    # if match:
        # print(f"Valid. Matched with {match.group()}")
    # else:
        # print("Invalid.")

# main()

# Program 2

print("~~~~~~~~~~~~Program 2~~~~~~~~~~~~")

# import re

# def mainTwo():
    # codeTwo = input("Hexadecimal color code: ")

    # patternTwo = r"#[abcdefABCDEF0123456789]"
    # matchTwo = re.search(patternTwo, codeTwo)

    # if matchTwo:
        # print(f"Valid. Matched with {matchTwo.group()}")
    # else:
        # print("Invalid.")

# mainTwo()

# Program 3

print("~~~~~~~~~~~~Program 3~~~~~~~~~~~~")

# import re

# def mainThree():
    # codeThree = input("Hexadecimal color code: ")

    # patternThree = r"#[abcdefABCDEF0123456789]{6}"
    # matchThree = re.search(patternThree, codeThree)

    # if matchThree:
        # print(f"Valid. Matched with {matchThree.group()}")
    # else:
        # print("Invalid.")

# mainThree()


# Program 4

print("~~~~~~~~~~~~Program 4~~~~~~~~~~~~")

# import re

# def mainFour():
    # codeFour = input("Hexadecimal color code: ")

    # patternFour = r"^#[abcdefABCDEF0123456789]{6}"
    # matchFour = re.search(patternFour, codeFour)

    # if matchFour:
        # print(f"Valid. Matched with {matchFour.group()}")
    # else:
        # print("Invalid.")

# mainFour()


# Program 5

print("~~~~~~~~~~~~Program 5~~~~~~~~~~~~")

import re

def mainFive():
    codeFive = input("Hexadecimal color code: ")

    patternFive = r"^#[a-fA-F0-9]{6}$"
    matchFive = re.search(patternFive, codeFive)

    if matchFive:
        print(f"Valid. Matched with {matchFive.group()}")
    else:
        print("Invalid.")

mainFive()