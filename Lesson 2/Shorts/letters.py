

# Program 1

print("~~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~~")

def main():
    print(write_letter("Mario", "Princess Peach"))
    print(write_letter("Luigi", "Princess Peach"))
    print(write_letter("Daisy", "Princess Peach"))
    print(write_letter("Yoshi", "Princess Peach"))


def write_letter(reciever, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {reciever},
        
        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.
        
        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+       
    """

main()

# Program 2

print("~~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~~")


def main_two():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(names)):
        print(names[i])



def write_letter_two(recieverTwo, senderTwo):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {recieverTwo},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {senderTwo}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+       
    """


main_two()


# Program 3

print("~~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~~")


def main_three():
    namesTwo = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for iTwo in range(len(namesTwo)):
        print(write_letter_three(namesTwo[iTwo], "Princess Peach"))



def write_letter_three(recieverThree, senderThree):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {recieverThree},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {senderThree}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+       
    """


main_three()

# Program 4

print("~~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~~")


def main_four():
    namesThree = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in namesThree:
        print(write_letter_four(name, "Princess Peach"))



def write_letter_four(recieverFour, senderFour):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {recieverFour},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {senderFour}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+       
    """


main_four()