
# Program 1

print("~~~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~~~")

# distances = {
     # "Voyager 1": "163",
     # "Voyager 2": "136",
     # "Pioneer 10": "80 AU",
     # "New Horizons": "58",
     # "Pioneer 11": "44 AU"
# }

# def main():
    # spacecraft = input("Enter a spacecraft: ")
    # m = convert(distances[spacecraft])
    # print(f"{m} m away")

# def convert(au):
    # return au * 149597870700

# main()

# Program 2

print("~~~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~~~")

# distancesTwo = {
    # "Voyager 1": "163",
    # "Voyager 2": "136",
    # "Pioneer 10": "80 AU",
    # "New Horizons": "58",
    # "Pioneer 11": "44 AU"
# }

# def mainTwo():
    # spacecraftTwo = input("Enter a spacecraft: ")
    # au = float(distancesTwo[spacecraftTwo])
    # mTwo = convertTwo(au)
    # print(f"{mTwo} m away")

# def convertTwo(auTwo):
    # return auTwo * 149597870700

# mainTwo()

# Program 3

print("~~~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~~~")

# distancesThree = {
    # "Voyager 1": "163",
    # "Voyager 2": "136",
    # "Pioneer 10": "80 AU",
    # "New Horizons": "58",
    # "Pioneer 11": "44 AU"
# }

# def mainThree():

    # spacecraftThree = input("Enter a spacecraft: ")

    # try:
        # auTwo = float(distancesThree[spacecraftThree])
    # except:
        # print(f"Can't convert {distancesThree[spacecraftThree]} to a float")
        # return

    # mThree = convertThree(auTwo)
    # print(f"{mThree} m away")

# def convertThree(auThree):
    # return auThree * 149597870700

# mainThree()

# KeyError: 'James Webb Space Telescope'

# Program 4

print("~~~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~~~")

distancesFour = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def mainFour():

    spacecraftFour = input("Enter a spacecraft: ")

    try:
        auThree = float(distancesFour[spacecraftFour])
    except KeyError:
        print(f"`{spacecraftFour}` is not in dictionary")
        return
    except:
        print(f"Can't convert {distancesFour[spacecraftFour]} to a float")
        return

    mFour = convertThree(auThree)
    print(f"{mFour} m away")

def convertThree(auFour):
    return auFour * 149597870700

mainFour()


