
from PIL import Image
from PIL import ImageFilter

# Program 1

print("~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~")

def main():
    with Image.open("in.jpeg") as image:
        print(image.size)
        print(image.format)

main()


# Program 2

print("~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~")

def mainTwo():
    with Image.open("in.jpeg") as imageTwo:
       imageTwo = imageTwo.rotate(180)
       imageTwo.save("out.jpeg")

mainTwo()

# Program 3

print("~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~")

def mainThree():
    with Image.open("in.jpeg") as imageThree:
       imageThree = imageThree.rotate(180)
       imageThree.filter(ImageFilter.BLUR)
       imageThree.save("out.jpeg")

mainThree()

# Program 4

print("~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~")

def mainFour():
    with Image.open("in.jpeg") as imageFour:
       imageFour = imageFour.rotate(180)
       imageFour.filter(ImageFilter.FIND_EDGES)
       imageFour.save("out.jpeg")

mainFour()


# shhhhhhhh Dog is smatter than me
# def mainTwo2():
    # with Image.open("in.jpeg") as imageTwo:
       # imageTwo = imageTwo.rotate(90)
       # imageTwo.save("outTwo.jpeg")

# mainTwo2()

# def mainTwo22():
    # with Image.open("in.jpeg") as imageTwo:
       # imageTwo = imageTwo.rotate(-90)
       # imageTwo.save("outTwo2.jpeg")

# mainTwo22()