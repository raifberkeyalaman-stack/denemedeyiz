def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Rule 1: Length must be between 2 and 6
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Rule 2: First two characters must be letters
    if not plate[:2].isalpha():
        return False

    number_started = True

    for char in plate:
        # Rule 3: No punctuation or spaces
        if not char.isalnum():
            return False

        if char.isdigit():
            # Rule 4: First number cannot be 0
            if not number_started:
                if char == "0":
                    return False
                number_started = True

        # Rule 5: Once numbers start, no letters are allowed
        elif number_started:
            return False
            print("no letters allowed after a number")

    return True


main()
