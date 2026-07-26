def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalidhhh")


def is_valid(plate):
    if len(plate) <= 2 and plate[0].isalpha() and plate[1].isalpha():
        print("Valid")
    elif len(plate) <= 3 and plate[0].isalpha() and plate[1].isalpha() and plate[2].isalpha() or plate[2].isdecimal():
        print("Valid")
    elif len(plate) <= 4 and plate[0].isalpha() and plate[1].isalpha() and plate[2].isalpha() and plate[3].isalpha() or plate[3].isdecimal():
            print("Valid")
    elif len(plate) <= 6 and plate[0].isalpha() and plate[1].isalpha() and plate[2:5].isdecimal():
        print("Valid")
    else:
        print("Invalid")

main()
