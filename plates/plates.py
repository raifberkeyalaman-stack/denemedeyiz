def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    #check the length
    if len(plate) < 2 or len(plate) > 6:
        return False

    #check first two letters
    if not plate[:2].isalpha():
        return False

    number_started = False

    for char in plate:
        if not char.isalnum():
            return False

        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False

                number_started = True
        elif number_started:
            return False
    return True


main()
