
import csv
import numpy as np
from PIL import Image

# Program 1

print("~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~")

def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
        return brightness

main()


# Program 2

print("~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~")

def main_two():
    with open("views.csv", "r") as fileTwo:
        readerTwo = csv.DictReader(fileTwo)
        for rowTwo in readerTwo:
            print(rowTwo["id"])

def calculate_brightness_two(filenameTwo):
    with Image.open(filenameTwo) as imageTwo:
        brightnessTwo = np.mean(np.array(imageTwo.convert("L"))) / 255
        return brightnessTwo

main_two()


# Program 3

print("~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~")

def main_three():
    with open("views.csv", "r") as fileThree:
        readerThree = csv.DictReader(fileThree)
        for rowThree in readerThree:
            brightnessFour = calculate_brightness_three(f"{rowThree['id']}.jpeg")
            print(brightnessFour)

def calculate_brightness_three(filenameThree):
    with Image.open(filenameThree) as imageThreee:
        brightnessThree = np.mean(np.array(imageThreee.convert("L"))) / 255
        return brightnessThree

main_three()

# Program 4

print("~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~")

def main_four():
    with open("views.csv", "r") as fileFour:
        readerFour = csv.DictReader(fileFour)
        for rowFour in readerFour:
            brightnessFive = calculate_brightness_four(f"{rowFour['id']}.jpeg")
            print(round(brightnessFive, 2))

def calculate_brightness_four(filenameFour):
    with Image.open(filenameFour) as imageFour:
        brightnessFour = np.mean(np.array(imageFour.convert("L"))) / 255
        return brightnessFour

main_four()

# Program 5

print("~~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~~")

def main_five():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        readerFive = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=readerFive.fieldnames + ["brightness"])
        writer.writeheader()
        for rowFive in readerFive:
            brightnessSix = calculate_brightness_five(f"{rowFive['id']}.jpeg")
            print(round(brightnessSix, 2))

def calculate_brightness_five(filenameFive):
    with Image.open(filenameFive) as imageFive:
        brightnessFive = np.mean(np.array(imageFive.convert("L"))) / 255
        return brightnessFive

main_five()

# Program 6

print("~~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~~")

def main_six():
    with open("views.csv", "r") as viewsTwo, open("analysis.csv", "w") as analysisTwo:
        readerSix = csv.DictReader(viewsTwo)
        writerTwo = csv.DictWriter(analysisTwo, fieldnames=readerSix.fieldnames + ["brightness"])
        writerTwo.writeheader()
        for rowSix in readerSix:
            brightnessSeven = calculate_brightness_six(f"{rowSix['id']}.jpeg")
            writerTwo.writerow({
                "id": rowSix["id"],
                "english_title": rowSix["english_title"],
                "japanese_title": rowSix["japanese_title"],
                "brightness": brightnessSeven
            })

def calculate_brightness_six(filenameSix):
    with Image.open(filenameSix) as imageSix:
        brightnessSix = np.mean(np.array(imageSix.convert("L"))) / 255
        return brightnessSix

main_six()

# Program 7

print("~~~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~~~")

def main_seven():
    with open("views.csv", "r") as viewsThree, open("analysis.csv", "w") as analysisThree:
        readerSeven = csv.DictReader(viewsThree)
        writerThree = csv.DictWriter(analysisThree, fieldnames=readerSeven.fieldnames + ["brightness"])
        writerThree.writeheader()
        for rowSeven in readerSeven:
            brightnessNine = calculate_brightness_seven(f"{rowSeven['id']}.jpeg")
            writerThree.writerow({
                "id": rowSeven["id"],
                "english_title": rowSeven["english_title"],
                "japanese_title": rowSeven["japanese_title"],
                "brightness": round(brightnessNine, 2)
            })

def calculate_brightness_seven(filenameSeven):
    with Image.open(filenameSeven) as imageSeven:
        brightnessEight = np.mean(np.array(imageSeven.convert("L"))) / 255
        return brightnessEight

main_seven()

# Program 8

print("~~~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~~~")

def main_eight():
    with open("views.csv", "r") as viewsFour, open("analysis.csv", "w") as analysisFour:
        readerEight = csv.DictReader(viewsFour)
        writerFour = csv.DictWriter(analysisFour, fieldnames=readerEight.fieldnames + ["brightness"])
        writerFour.writeheader()
        for rowEight in readerEight:
            rowEight["brightness"] = calculate_brightness_eight(f"{rowEight['id']}.jpeg")
            writerFour.writerow(rowEight)


def calculate_brightness_eight(filenameEight):
    with Image.open(filenameEight) as imageEight:
        brightnessTen = np.mean(np.array(imageEight.convert("L"))) / 255
        return brightnessTen

main_eight()


# Program 9

print("~~~~~~~~~~~~~~~~~Program 9~~~~~~~~~~~~~~~~~")

def main_nine():
    with open("views.csv", "r") as viewsFive, open("analysis.csv", "w") as analysisFive:
        readerNine = csv.DictReader(viewsFive)
        writerFive = csv.DictWriter(analysisFive, fieldnames=readerNine.fieldnames + ["brightness"])
        writerFive.writeheader()
        for rowNine in readerNine:
            rowNine["brightness"] = round(calculate_brightness_nine(f"{rowNine['id']}.jpeg"), 2)
            writerFive.writerow(rowNine)


def calculate_brightness_nine(filenameNine):
    with Image.open(filenameNine) as imageNine:
        brightnessTwelve = np.mean(np.array(imageNine.convert("L"))) / 255
        return brightnessTwelve

main_nine()