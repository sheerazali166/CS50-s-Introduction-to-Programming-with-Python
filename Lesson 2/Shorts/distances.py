
# Program 1

print("~~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~~")

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

# still problem in anushka

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")

main()

# Program 2

print("~~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~~")

distances_two = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}



def main_two():
    for distance in distances.values():
        print(f"{distance} is {convert(distance)} m")


def convert(au):
    return au * 149597870700

main_two()


