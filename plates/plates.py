def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate[:2].isalpha():
        return False
    number_started = False
    for char in plate:
        if char.isdigit():
            number_started = True
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False

        number_started = True



main()
