
# Program 1

print("~~~~~~~~~~~~~~~~Program 1~~~~~~~~~~~~~~~~")

def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========== REPORT ==========
    
    Name: TODO
    Distance: TODO     
              
    ============================            
    """

main()


# Program 2

print("~~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~~")


def main_two():
    spacecraft_two = {"name": "Voyager 1", "distance": 163}
    print(create_report_two(spacecraft_two))


def create_report_two(spacecraft_two):
    return f"""
    ========== REPORT ==========

    Name: {spacecraft_two["name"]}
    Distance: {spacecraft_two["distance"]} AU    

    ============================            
    """


main_two()

# Program 3

print("~~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~~")


# def main_three():
    # spacecraft_three = {"name": "James Webb Space Telescope"}
    # print(create_report_three(spacecraft_three))


# def create_report_three(spacecraft_three):
    # return f"""
    # ========== REPORT ==========

    # Name: {spacecraft_three["name"]}
    # Distance: {spacecraft_three["distance"]} AU

    # ============================
    # """

# main_three()

# Distance: {spacecraft_three["distance"]} AU
# KeyError: 'distance'

# Program 4

print("~~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~~")


def main_four():
    spacecraft_four = {"name": "James Webb Space Telescope"}
    spacecraft_four["distance"] = 0.01
    print(create_report_four(spacecraft_four))


def create_report_four(spacecraft_four):
    return f"""
    ========== REPORT ==========

    Name: {spacecraft_four["name"]}
    Distance: {spacecraft_four["distance"]} AU

    ============================
    """

main_four()


# Program 5

print("~~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~~")


def main_five():
    spacecraft_five = {"name": "James Webb Space Telescope"}
    print(create_report_five(spacecraft_five))


def create_report_five(spacecraft_five):
    return f"""
    ========== REPORT ==========

    Name: {spacecraft_five.get("name", "Unknown")}
    Distance: {spacecraft_five.get("distance", "Unknown")} AU

    ============================
    """

main_five()


# Program 6

print("~~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~~")


def main_six():
    spacecraft_six = {"name": "James Webb Space Telescope"}
    spacecraft_six.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report_six(spacecraft_six))


def create_report_six(spacecraft_six):
    return f"""
    ========== REPORT ==========

    Name: {spacecraft_six.get("name", "Unknown")}
    Distance: {spacecraft_six.get("distance", "Unknown")} AU
    Orbit: {spacecraft_six.get("orbit", "Unknown")}
    ============================
    """

main_six()

