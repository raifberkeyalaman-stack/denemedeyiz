def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if len(plate) <= 2 and plate[0:1].isalpha():
        return True
    elif len(plate) <= 3 and plate[0:2].isalpha():
        return True
    elif len(plate) <= 3 and plate[0:1].isalpha() and (plate[2].isalpha() or (plate[2].isdecimal() and plate[2] != "0")):
        return True
    elif len(plate) <= 4 and plate[0:3].isalpha():
            return True
    elif len(plate) <= 4 and plate[0:2].isalpha() and plate[3].isalpha() or plate[3].isdecimal() and plate[3] != "0":
            return True
    elif len(plate) <= 4 and plate[0:1].isalpha() and plate[2:3].isdecimal() and plate[2] != "0":
                return True
    elif len(plate) <= 5 and plate[0:4].isalpha():
            return True
    elif len(plate) <= 5 and plate[0:1].isalpha() and plate[2:4].isdecimal() and plate[2] != "0":
                    return True
    elif len(plate) <= 5 and plate[0:2].isalpha() and plate[3:4].isdecimal() and plate[3] != "0":
                    return True
    elif len(plate) <= 5 and plate[0:3].isalpha() and plate[4].isdecimal() and plate[4] != "0":
                        return True
    elif len(plate) <= 6 and plate[0:5].isalpha():
            return True
    elif len(plate) <= 6 and plate[0:1].isalpha() and plate[2:5].isdecimal() and plate[2] != "0":
        return True
    elif len(plate) <= 6 and plate[0:2].isalpha() and plate[3:5].isdecimal() and plate[3] != "0":
            return True
    elif len(plate) <= 6 and plate[0:3].isalpha() and plate[4:5].isdecimal() and plate[4] != "0":
            return True
    elif len(plate) <= 6 and plate[0:4].isalpha() and plate[5].isdecimal() and plate[5] != "0":
                return True
    else:
        return False

main()
